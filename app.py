import streamlit as st
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import time
from skin_cancer_mnist import skin_cancer_classifier

st.beta_set_page_config(
page_title="Auto Vaidya",
layout="centered",
initial_sidebar_state="collapsed",
)

# Just making sure we are not bothered by File Encoding warnings
st.set_option('deprecation.showfileUploaderEncoding', False)


def main():
    # add your own classifier name here
    menu = ['Home','Skin Cancer Classifier','Contact']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        # Let's set the title of our awesome web app
        img  = Image.open('assets/logo.png')
        covid_img = Image.open('assets/coronavirus.jpg')
        covid_img = covid_img.resize((100,100))
        diabetic_img = Image.open('assets/diabetic_retinopathy.jpeg')
        diabetic_img = diabetic_img.resize((100,100))
        heart_img = Image.open('assets/Heart-graphic.jpg')
        heart_img = heart_img.resize((100,100))
        pneu_img = Image.open('assets/pneumonia.jpg')
        pneu_img = pneu_img.resize((100,100))
        skin_img = Image.open('assets/skin-cancer.jpg')
        skin_img = skin_img.resize((100,100))
        st.image(img)
        st.image([covid_img,diabetic_img,heart_img,pneu_img,skin_img],caption=["COVID-19 Detection","Diabetic Retinopathy","Heart Disease Prediction","Pneumonia Detection","Skin Cancer Detection"])
        st.write("Illustration of the Web Application:")
        st.video('assets/demo.mp4')
        
    if choice == "Skin Cancer Classifier":
        # Now setting up a header text
        st.subheader("Skin Cancer Prediction")
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
        # When the user clicks the predict button
        if st.button("Predict"):
        # If the user uploads an image
            if uploaded_file is not None:
                # Opening our image
                image = Image.open(uploaded_file)
                # Let's see what we got
                st.image(image,use_column_width=True)
                st.write("")
                try:
                    with st.spinner("The magic of our AI has started...."):
                        label =skin_cancer_classifier(image)
                        time.sleep(8)
                    st.success("We predict this image to be: "+label)
                    rating = st.slider("Do you mind rating our service?",1,10)
                except:
                    st.error("We apologize something went wrong 🙇🏽‍♂️")
            else:
                st.error("Can you please upload an image 🙇🏽‍♂️")

    elif choice == "Contact":
        # Let's set the title of our Contact Page
        st.title('Get in touch')
        def display_team(name,path,affiliation="",email=""):
            '''
            Function to display picture,name,affiliation and name of creators
            '''
            team_img = Image.open(path)
            st.image(team_img, width=350, use_column_width=False)
            st.markdown(f"## {name}")
            st.markdown(f"#### {affiliation}")
            st.markdown(f"###### Email {email}")
            st.write("------")
        display_team("Your Awesome Name", "./assets/profile_pic.png","Your Awesome Affliation","hello@youareawesome.com")

if __name__ == "__main__":
    main()
