import logging
import random

import streamlit as st

logger = logging.getLogger(__name__)


def main():
    st.set_page_config(page_title="Home", page_icon="🏠")

def show_sidebar():
    st.sidebar.markdown('''
        <style>
            .spacer {
                display: flex;
                flex-direction: column;
                height: 50vh;  # Adjust the height percentage as needed
            }
        </style>
        <div class="spacer"></div>
    ''', unsafe_allow_html=True)

    show_trademark()


def show_trademark():
    st.sidebar.markdown("BWA Email Assistant")


if __name__ == "__main__":
    main()
    show_sidebar()
