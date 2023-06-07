import streamlit as st
import torch
import numpy as np

def main():
    # set page layout
    st.set_page_config(layout='wide')
    # info
    st.markdown(readme())
    st.markdown(np.__version__)

@st.cache()
def readme():
    with open('README.md', 'r') as f:
        return f.read()


if __name__ == "__main__":
    main()
