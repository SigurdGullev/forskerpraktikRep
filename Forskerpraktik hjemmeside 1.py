import streamlit as st
from PIL import Image

# Load the images (assuming they are in the same directory as the app)
image1_path = "cookie1.jpeg"
image2_path = "cookie2.jpeg"

image1 = Image.open(image1_path)

# Display the first image
st.image(image1, caption='Click below to reveal another image.', use_column_width=True)

# Check if the user clicks the button
if st.button('Show the second image'):
    image2 = Image.open(image2_path)
    st.image(image2, caption='Here is the second image.', use_column_width=True)
