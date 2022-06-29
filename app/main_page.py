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
import streamlit.components.v1 as stc

st.set_page_config(
    page_title="Example",  layout="wide"
)

#style taken from https://fossheim.io/writing/posts/css-text-gradient/
stc.html("""
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        
        body {
        margin: 0;
        font-family: Arial;
        }
        .gradient-text {
        /* Fallback: Set a background color. */
        background-color: red;
        
        /* Create the gradient. */
        background-image: linear-gradient(45deg, #f3ec78, #af4261);
        
        /* Set the background size and repeat properties. */
        background-size: 100%;
        background-repeat: repeat;

        /* Use the text as a mask for the background. */
        /* This will show the gradient as a text color rather than element bg. */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent; 
        -moz-background-clip: text;
        -moz-text-fill-color: transparent;
        }



        h1 {
        font-family: "Archivo Black", sans-serif;
        font-weight: normal;
        font-size: 8em;
        text-align: center;
        margin-bottom: 0;
        margin-bottom: -0.25em;
        }
        </style>

        </head>
        <body>
        
        <h1 class="gradient-text">Multiple Choice<br>QA<br></h1>



        </body>
        </html>

        """, height=1000)

st.sidebar.markdown("# Home Page 🤗")
