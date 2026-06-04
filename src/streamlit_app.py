import streamlit as st

from prompt import PROMPT_TEMPLATE
from model import get_response
from parser import parse_response

st.set_page_config(
    page_title="Social Media Post Analyzer",
    page_icon="📱"
)

st.title("📱 Social Media Post Analyzer")

st.write(
    "Analyze tone, intent, communication style, and summary of social media posts."
)

post = st.text_area(
    "Enter Social Media Post",
    height=150
)

if st.button("Analyze Post"):

    if post.strip():

        with st.spinner("Analyzing..."):

            prompt = PROMPT_TEMPLATE.format(
                post=post
            )

            response = get_response(prompt)

            result = parse_response(response)

            st.subheader("Analysis Result")

            st.json(result)

    else:
        st.warning("Please enter a social media post.")