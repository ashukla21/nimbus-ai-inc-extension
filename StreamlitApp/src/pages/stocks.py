import pathlib
import utils.display as udisp

import streamlit as st
import core.stocks.final_application.app2 as CalcEngine

def write():
    udisp.title_awesome("Compound Interest Calclator")
    CalcEngine.calc_main("CI Calculator", "A Compound Interest Calclator")

    st.write("@avkashchauhan")