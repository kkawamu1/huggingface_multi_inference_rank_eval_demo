
import streamlit as st
import requests
from typing import Dict
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from app.evaluation_scripts.run_eval import multi_inference_rank_eval


st.set_page_config(layout="wide")
st.markdown(f'<p style="text-align:center;background-image: linear-gradient(to right,#1aa3ff, #00ff00);color:#ffffff;font-size: 4em;;border-radius:2%;-webkit-background-clip: text;-webkit-text-fill-color: transparent;">Submit your question here</p>', unsafe_allow_html=True)


st.sidebar.markdown("# Evaluation 🤔")
st.markdown(
    '<style>div[data-testid="stHorizontalBlock"] > div:first-of-type {border:10px;padding:30px;border-radius: 10px;;background-image: linear-gradient(45deg, #1aa3ff, #234599);}</style>', unsafe_allow_html=True)
st.markdown(
    '<style>div[data-testid="stHorizontalBlock"] > div:nth-of-type(2)  {border:10px;padding:30px;border-radius: 10px;background-image: linear-gradient(45deg, #f3ec78, #023611);}</style>', unsafe_allow_html=True)



INCLUDED_USERS = ['google', 'EleutherAI',
                  "bigscience", "facebook", "openai", "microsoft"]

PIPELINE_TAG_TO_TASKS = {
    'text-generation': "CausalLM", 'text2text-generation': "Seq2SeqLM"}


@st.cache
def fetch_model_info_from_huggingface_api() -> Dict[str, Dict[str, str]]:
    requests.get("https://huggingface.co")
    response = requests.get("https://huggingface.co/api/models")
    tags = response.json()
    model_to_model_id = {}
    model_to_pipeline_tag = {}

    for model in tags:
        model_name = model['modelId']
        is_community_model = "/" in model_name
        if is_community_model:
            user = model_name.split("/")[0]
            if user not in INCLUDED_USERS:
                continue
        if "pipeline_tag" in model and model["pipeline_tag"] in list(PIPELINE_TAG_TO_TASKS.keys()):
            model_to_model_id[model['id']] = model['modelId']
            model_to_pipeline_tag[model['id']
                                  ] = PIPELINE_TAG_TO_TASKS[model["pipeline_tag"]]
    return model_to_pipeline_tag


model_to_auto_class = fetch_model_info_from_huggingface_api()

col1, col2 = st.columns([3, 2])
user_input = {}
with col1:
    st.header("Question")
    user_input['context'] = st.text_input(
        label='Write your question. You may explicity mention the answer choices in the prompt.', value='Huggingface is awesome. True or False?')
    user_input['answer_choices_texts'] = st.text_input(
        label='Add answer choices in text spearated by a comma and a space.', value='True, False')
    user_input['answer_choices_texts'] = user_input['answer_choices_texts'].split(
        ', ')


with col2:
    st.header("Model Config")
    user_input['model'] = st.selectbox(
        "Which model?", list(model_to_auto_class.keys()))
    user_input['auto_class'] = model_to_auto_class[user_input['model']]
col4, col5 = st.columns(2)
with col5:
    #style taken from https://css-tricks.com/css-hover-effects-background-masks-3d/
    st.markdown("""<style> 
    div.stButton > button:first-child  {
        width: 100%;
        border: 4px solid;
        border-image: repeating-linear-gradient(135deg,#F8CA00 0 10px,#E97F02 0 20px,#BD1550 0 30px) 8;
        -webkit-mask: 
            conic-gradient(from 180deg at top 8px right 8px, #0000 90deg,#000 0)
            var(--_i,200%) 0  /200% var(--_i,8px) border-box no-repeat,
            conic-gradient(at bottom 8px left  8px,  #0000 90deg,#000 0)
            0   var(--_i,200%)/var(--_i,8px) 200% border-box no-repeat,
            linear-gradient(#000 0 0) padding-box no-repeat;
        transition: .3s, -webkit-mask-position .3s .3s;
        
    }
    button:hover {
        --_i: 100%;
        color: #CC333F;
        transition: .3s, -webkit-mask-size .3s .3s;
    }
    </style>""", unsafe_allow_html=True)
    st.header("Submit task")
    submit = st.button('Submit')

with col4:
    st.header("Result")
    if submit:
        with st.spinner('Wait for it...'):
            prediction = multi_inference_rank_eval(
                user_input['model'], user_input['auto_class'], user_input['answer_choices_texts'], user_input['context'])
        # print(prediction)
        st.markdown(f"### {user_input['answer_choices_texts'][prediction]}")
