import pathlib
import utils.display as udisp

import streamlit as st
import core.imageprocessing.streamlit_app as ScikitEngine

def write():
    udisp.title_awesome("Image Processing")
    ScikitEngine.calc_main("Scikit Image", "A Scikit Image Demo")

    st.write("@Aditya")