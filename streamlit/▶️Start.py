import streamlit as st
from PIL import Image

st.set_page_config(page_title='Start', page_icon='▶️', layout='wide', initial_sidebar_state='expanded')

# CSS access
with open('css/style.css') as f:
    st.markdown(
        f'<style>{f.read()}</style>',
        unsafe_allow_html=True,
    )

st.markdown('# Unlimited wordiply')

image = Image.open('images/wordiply.png')
st.image(image, use_column_width=True)

st.markdown('#### Rules')

st.write('You have five goes to get the longest word that includes the starter word.')
image = Image.open('images/rules.png')
st.image(image, use_column_width=True)

st.markdown('#### Scoring')

st.write('The closer you are to the longest word, the higher your length score.')
st.write('The more letters you use in total, the higher your letter score.')