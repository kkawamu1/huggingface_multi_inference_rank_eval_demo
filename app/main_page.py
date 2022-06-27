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
