# Streamlit
import streamlit as st

# Images
from PIL import Image

# My functions
from src import game_start_set_up_functions as setup
from src import input_word_function as input

st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Play', page_icon='🎲')

col1, col2, col3 = st.columns(3)

with col1:

    pass

with col2:

    chosen_letters_to_start = setup.get_letters_to_start()

    st.write(chosen_letters_to_start)

    for i in range(1,6):

        text_input = input.input_word(i)

        if text_input:

            st.write('You entered: ', text_input)

with col3:

    pass