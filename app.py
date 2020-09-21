import streamlit as st
from PIL import Image
import numpy as np
import time


st.beta_set_page_config(
page_title="Title of the webpage",
layout="centered",
initial_sidebar_state="collapsed",
)

# Just making sure we are not bothered by File Encoding warnings
st.set_option('deprecation.showfileUploaderEncoding', False)

def main():
    menu = ['Home', 'Project1','Project2','Project3']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        # Let's set the title of our awesome web app
        st.title('Title of your Awesome App')
        # Now setting up a header text
        st.subheader("By Your Cool Dev Name")
        # adding random text
        st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        
    elif choice == "Project1":
        # Let's set the title of our Contact Page
        st.title('Project 1 !!!')
    
    elif choice == "Project2":
        # Let's set the title of our Contact Page
        st.title('Project 2 !!!')
        
    elif choice == "Project3":
        # Let's set the title of our Contact Page
        st.title('Project 3 !!!')
        
        
if __name__ == "__main__":
    main()