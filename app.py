import streamlit as st
from PIL import Image

st.title("🎭 Emotion & ISL Demo")
st.write("Basic working version")

uploaded_file = st.file_uploader("Upload image", type=['jpg', 'png'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True)
    st.success("✅ App is working!")
    st.info("Emotion: Happy 😊")
    st.info("Gesture: Hello 👋")
