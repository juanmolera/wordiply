import streamlit as st
from PIL import Image
import random

st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Play', page_icon='🎲')

with open('../data/words_alpha.txt') as f:
    raw = f.readlines()

words = []

for i in raw:

    words.append(i.rstrip('\n'))

random_pick_of_the_game = random.choice(words)

col1, col2, col3 = st.columns(3)

with col1:

    pass

with col2:

    text_input = st.text_input('Enter some text 👇')

    if text_input:

        st.write('You entered: ', text_input)

with col3:

    pass