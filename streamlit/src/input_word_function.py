# Streamlit
import streamlit as st


def input_word(key_argument):

    text_input = st.text_input(f'Try {key_argument}:')

    return text_input
        