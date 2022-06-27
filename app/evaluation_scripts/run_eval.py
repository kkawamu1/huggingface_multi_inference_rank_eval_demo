import torch
from accelerate import Accelerator
from transformers import (AutoModelForCausalLM, AutoModelForSeq2SeqLM,
                          AutoTokenizer, set_seed)


def multi_inference_rank_eval(model_name_or_path, auto_class, ex_answer_choices, context):
    accelerator = Accelerator()
    set_seed(42)
    model_name = model_name_or_path
    if auto_class == 'Seq2SeqLM':

        # e.g. 'google/t5-small-lm-adapt'
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    else:
        # e.g. 'gpt2'
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

    if tokenizer.pad_token is None:
        for token in [tokenizer.eos_token, tokenizer.bos_token, tokenizer.sep_token]:
            if token is not None:
                tokenizer.pad_token = token
        if tokenizer.pad_token is None:
            raise ValueError("Please define a pad token id.")

    padding = False

    if auto_class == 'Seq2SeqLM':
        def preprocess_function(context, ex_answer_choices):
            input_texts = []
            answer_choices_texts = []
            input_texts.append(context)
            answer_choices_texts.append(
                [' ' + ans for ans in ex_answer_choices])

            tokenized_inputs = tokenizer(
                input_texts,
                padding=padding,
                max_length=1024,
                truncation=True,
                add_special_tokens=False,
            )

            tokenized_targets = [
                tokenizer(
                    ans_choi,
                    padding=True,
                    max_length=256,
                    truncation=True,
                )
                for ans_choi in answer_choices_texts
            ]

            features = {
                k: [
                    [elem for _ in range(
                        len(tokenized_targets[idx]["input_ids"]))]
                    for idx, elem in enumerate(v)
                ]
                for k, v in tokenized_inputs.items()
            }

            features["labels"] = [
                tokenized_targets[0]["input_ids"]
            ]

            features["labels_attention_mask"] = [
                tokenized_targets[0]["attention_mask"]
            ]
            return features
    else:
        def preprocess_function(context, ex_answer_choices):
            input_texts = []
            answer_choices_texts = []
            input_texts.append(context)
            answer_choices_texts.append(
                [' ' + ans for ans in ex_answer_choices])

            tokenized_inputs = tokenizer(
                input_texts,
                padding=padding,
                max_length=1024,
                truncation=True,
                add_special_tokens=False,
            )

            tokenized_targets = [
                tokenizer(
                    ans_choi,
                    padding=True,
                    max_length=256,
                    truncation=True,
                )
                for ans_choi in answer_choices_texts
            ]

            features = {
                k: [
                    [elem for _ in range(
                        len(tokenized_targets[idx]["input_ids"]))]
                    for idx, elem in enumerate(v)
                ]
                for k, v in tokenized_inputs.items()
            }

            features["labels"] = [
                tokenized_targets[0]["input_ids"]
            ]

            features["labels_attention_mask"] = [
                tokenized_targets[0]["attention_mask"]
            ]

            features["labels"] = [
                [features["input_ids"][0][i][1:] + tokenized_targets[0]["input_ids"][i]
                    for i in range(len(tokenized_targets[0]["input_ids"]))]
            ]
            features["input_ids"] = [
                [features["input_ids"][0][i] + tokenized_targets[0]["input_ids"][i][:-1]
                    for i in range(len(tokenized_targets[0]["input_ids"]))]
            ]

            features["labels_attention_mask"] = [
                [[0] * (len(features["attention_mask"][0][i])-1) + tokenized_targets[0]
                 ["attention_mask"][i] for i in range(len(tokenized_targets[0]["input_ids"]))]
            ]

            features["attention_mask"] = [
                [features["attention_mask"][0][i] + tokenized_targets[0]["attention_mask"][i][:-1]
                    for i in range(len(tokenized_targets[0]["input_ids"]))]
            ]

            return features

    device = accelerator.device
    model.to(device)
    batch = preprocess_function(context, ex_answer_choices)
    batch = {
        k: torch.tensor(batch[k][0]).to(device)
        for k in batch.keys()
    }

    model.eval()
    with torch.no_grad():
        model_inputs = {
            k: batch[k]
            for k in (["input_ids", "attention_mask", "labels"] if auto_class == 'Seq2SeqLM' else ["input_ids", "attention_mask"])
        }

        logits = model(**model_inputs).logits
        masked_log_probs = batch["labels_attention_mask"].unsqueeze(
            -1) * torch.log_softmax(logits, dim=-1)
        seq_token_log_probs = torch.gather(
            masked_log_probs, -1, batch["labels"].unsqueeze(-1))
        seq_log_prob = seq_token_log_probs.squeeze(dim=-1).sum(dim=-1)
        seq_log_prob = seq_log_prob.view(1, -1)
        predictions = seq_log_prob.argmax(dim=-1)

    predictions = accelerator.gather(predictions)
    return predictions.item()


if __name__ == "__main__":
    multi_inference_rank_eval('google/t5-small-lm-adapt', 'Seq2SeqLM',
                              ['True', 'False', 'True', 'Ken'], 'I am Ken. True or False')
    # multi_inference_rank_eval('gpt2', 'CausalLM', ['True', 'False', 'True', 'Ken'], 'I am Ken. True or False')
