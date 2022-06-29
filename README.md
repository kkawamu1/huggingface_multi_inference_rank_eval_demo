---
title: Huggingface Multi Inference Rank Eval
emoji: 🤔
colorFrom: yellow
colorTo: purple
sdk: streamlit
sdk_version: 1.10.0
app_file: ./app/main_page.py
pinned: false
license: cc
---

# huggingface_multi_inference_rank_eval
**This app lets the users play around with Huggingface models on a prommpted multiple choice QA inference.**

Recenet researches like [GPT-3](https://arxiv.org/abs/2005.14165), [FLAN](https://arxiv.org/abs/2109.01652), and [T0](https://arxiv.org/abs/2110.08207) showed a promising direction in zero-shot generalization via prompting. Rathern than pretraining on a huge dataset and finetuning a model on downstream task, we can directly ask a question to a model by prompting a model on a task!


<p align="center">
  <img src="assets/demo.png" width="800"/>
</p>

This app lets users interact with various models hosted on [Huggingface models](https://huggingface.co/models) and ask a multiple choice question. Models rank the choices with their log probabilities and pick the choice with highest log probability. We currently supoort [CausalLM](https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoModelForCausalLM) and [Seq2SeqLM](https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoModelForSeq2SeqLM).

e.g.
```
Question: Huggingface is awesome. True or False?
Answer choices: True, False
Prediction: True
```

**You can access the [hosted version](https://huggingface.co/spaces/kkawamu1/huggingface_multi_inference_rank_eval).**

## Setup
Clone the repository, install the required packages and run:
```bash
streamlit run ./app/main_page.py
```


## Reference
A chunk of codes used for this projects is taken and/or insipred from the following works and their related repository:
```bibtex
@inproceedings{sanh2022multitask,
    title={Multitask Prompted Training Enables Zero-Shot Task Generalization},
    author={Victor Sanh and Albert Webson and Colin Raffel and Stephen Bach and Lintang Sutawika and Zaid Alyafeai and Antoine Chaffin and Arnaud Stiegler and Arun Raja and Manan Dey and M Saiful Bari and Canwen Xu and Urmish Thakker and Shanya Sharma Sharma and Eliza Szczechla and Taewoon Kim and Gunjan Chhablani and Nihal Nayak and Debajyoti Datta and Jonathan Chang and Mike Tian-Jian Jiang and Han Wang and Matteo Manica and Sheng Shen and Zheng Xin Yong and Harshit Pandey and Rachel Bawden and Thomas Wang and Trishala Neeraj and Jos Rozen and Abheesht Sharma and Andrea Santilli and Thibault Fevry and Jason Alan Fries and Ryan Teehan and Teven Le Scao and Stella Biderman and Leo Gao and Thomas Wolf and Alexander M Rush},
    booktitle={International Conference on Learning Representations},
    year={2022}
    url={https://openreview.net/forum?id=9Vrb9D0WI4}
```
```bibtex
@software{eval-harness,
  author       = {Gao, Leo and
                  Tow, Jonathan and
                  Biderman, Stella and
                  Black, Sid and
                  DiPofi, Anthony and
                  Foster, Charles and
                  Golding, Laurence and
                  Hsu, Jeffrey and
                  McDonell, Kyle and
                  Muennighoff, Niklas and
                  Phang, Jason and
                  Reynolds, Laria and
                  Tang, Eric and
                  Thite, Anish and
                  Wang, Ben and
                  Wang, Kevin and
                  Zou, Andy},
  title        = {A framework for few-shot language model evaluation},
  month        = sep,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {v0.0.1},
  doi          = {10.5281/zenodo.5371628},
  url          = {https://doi.org/10.5281/zenodo.5371628}
}
```
For style, 
```
https://fossheim.io/writing/posts/css-text-gradient/
https://css-tricks.com/css-hover-effects-background-masks-3d/
```


