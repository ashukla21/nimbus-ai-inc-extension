import streamlit as st

st.set_page_config(page_title= 'Nimbus AI Inc.',
    page_icon= '⛈')

import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('gray.jpg')

import utils.display as udisp

import src.pages.home
import src.pages.about
#import src.pages.compound
#import src.pages.crypto
#import src.pages.stocks
import src.pages.scikit_image
import src.pages.calculator

MENU = {
    "Home" : src.pages.home,
    #"Image Styler" : src.pages.compound,
    #"Stocks" : src.pages.stocks,
    #"Crypto" : src.pages.crypto,
    "Face Generator" : src.pages.scikit_image,
    "Text Editor" : src.pages.calculator,
    "Credits" : src.pages.about
}


def main():
    st.sidebar.title("Browse Our Library:")
    menu_selection = st.sidebar.radio("Choose your option...", list(MENU.keys()))

    menu = MENU[menu_selection]

    with st.spinner(f"Loading {menu_selection} ..."):
        udisp.render_page(menu)

if __name__ == "__main__":
    main()
