# Copyright 2022 Ken Kawamura
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st

st.set_page_config(layout="wide")
st.markdown(f'<p style="text-align:center;background-image: linear-gradient(to right,#d9306e, #412f8f);color:#ffffff;font-size: 4em;;border-radius:2%;-webkit-background-clip: text;-webkit-text-fill-color: transparent;">Reference</p>', unsafe_allow_html=True)

st.markdown('### A chunk of codes used for this projects is taken and insipred from the following works and their related repository:')

st.markdown("""1. @inproceedings{sanh2022multitask,
    title={Multitask Prompted Training Enables Zero-Shot Task Generalization},
    author={Victor Sanh and Albert Webson and Colin Raffel and Stephen Bach and Lintang Sutawika and Zaid Alyafeai and Antoine Chaffin and Arnaud Stiegler and Arun Raja and Manan Dey and M Saiful Bari and Canwen Xu and Urmish Thakker and Shanya Sharma Sharma and Eliza Szczechla and Taewoon Kim and Gunjan Chhablani and Nihal Nayak and Debajyoti Datta and Jonathan Chang and Mike Tian-Jian Jiang and Han Wang and Matteo Manica and Sheng Shen and Zheng Xin Yong and Harshit Pandey and Rachel Bawden and Thomas Wang and Trishala Neeraj and Jos Rozen and Abheesht Sharma and Andrea Santilli and Thibault Fevry and Jason Alan Fries and Ryan Teehan and Teven Le Scao and Stella Biderman and Leo Gao and Thomas Wolf and Alexander M Rush},
    booktitle={International Conference on Learning Representations},
    year={2022}
    url={https://openreview.net/forum?id=9Vrb9D0WI4}""")
    
st.markdown("""2. @software{eval-harness, author = {Gao, Leo and
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
}""")

st.markdown("""3. For style https://fossheim.io/writing/posts/css-text-gradient/""")
st.markdown("""4. For style https://css-tricks.com/css-hover-effects-background-masks-3d/""")
