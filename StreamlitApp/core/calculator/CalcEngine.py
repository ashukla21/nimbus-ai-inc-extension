import streamlit as st
from datetime import datetime

import numpy as np

import utils.display as display
import utils.globalDefine as globalDefine

from gensim.summarization import summarize
import spacy
import spacy_streamlit
from nltk.corpus import wordnet
from textblob import TextBlob
from pattern.web import Google
import streamlit.components.v1 as components
from pattern.en import pluralize , singularize,comparative, superlative
import codecs

nlp = spacy.load('en_core_web_sm')

#custom funtion 
def summary(text):
    return summarize(text)


# Custom Components Fxn
def st_calculator(calc_html,width=1000,height=1350):
	calc_file = codecs.open(calc_html,'r')
	page = calc_file.read()
	components.html(page,width=width,height=height,scrolling=False)

def calc_main():
    st.title("Nimbus Words")   
    st.sidebar.header("Input Options") 
    expander_bar = st.beta_expander("How To Use This App")
    expander_bar.markdown("""

    **Use the Dropdown Box located within the sidebar on the left to choose 1 of the 6 AI text editing features offered by Nimbus Words.** 

    1) **Summarizer:** Paste in text that will be summarized by our AI model. The first text box will do an automated summary of our program's recommended word count, and the second box beneath that will provide a summary of the exact word count you choose using the slider located within the sidebar.  

    2) **Tokenizer:** Paste in text that will be analyzed by our AI model. The **Tokenizer** button will provide a breakdown on each word within the phrase, for example 'Google' is an organization, or 'Jeff Bezos' is a proper noun. The **NER** button will display all named entities, for example 'Steve Jobs' is a person. The **Text Relationship** button will display a visual graph of the dependency each word has within a sentence or phrase. 

    3) **Synonyms:** Paste in text that will be analyzed by our AI model. The **Synonyms** button will provide you with synonyms to the inputted attribute. The **Definition** checkbox will provide definitions for the attribute. The **Example** checkbox will provide examples of the given attribute in a sentence.

    4) **Translator:** Paste in text that will be translated by our AI model. The **Translate** button will translate the inputted text into one of the many languages that we have provided, and we will automatically detect which language the inputted text is written in.

    5) **Search:** Paste in text that will be preprcoessed by our AI model. The **Search** button will do a filtered search for your input.

    6) **Spell Correction:** Paste in text that will be spell-checked by our AI model. The **Correct** button will offer a correct spelling for any grammatical error that are detected. The **Pluralize**, **Singularize**, **Comparative** and **Superlative** checkboxes do exactly as they say, and ouput those options for the input you provided. 

    """)

    activites = ["Summary", "Tokenizer","Synonyms","Translator","Search","Spell Correction"]
    choice = st.sidebar.selectbox("Select Activity",activites)
    if choice == "Summary":
        st.title('AI Text Summarizer')
        text = st.text_area("Input Text For Summary",height=300)
        if st.button("Summarize"):
            st.success(summary(text))
        text_range= st.sidebar.slider("Summarize words Range",25,500)
        text = st.text_area("Input Text For Summary",height=250)
        if st.button("Summarize with Custom Word Count"):
           st.warning(summarize(text,word_count=text_range))
    # Tokenizer
    elif choice == "Tokenizer":
        st.title('Text Tokenizer')
        row_data = st.text_area("write Text For Tokenizer")
        docx= nlp(row_data)
        if st.button("Tokenizer"):
            spacy_streamlit.visualize_tokens(docx,attrs=['text','pos_','dep_','ent_type_'])
        if st.button("NER"):
            spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)
        if st.button("Text Relationship"):
            spacy_streamlit.visualize_parser(docx)
       # synonyms      
    elif choice == "Synonyms":
        st.title('Synonym Generator')
        text = st.text_area("Enter Text")
        if st.button("Synonyms"):
            for syn in wordnet.synsets(text):
                for i in syn.lemmas():
                    st.success(i.name())
        if st.checkbox("Definition"):
            for syn in wordnet.synsets(text):
                st.warning(syn.definition()) 
        if st.checkbox("Example"):
            for syn in wordnet.synsets(text):
                st.success(syn.examples())
      # Translator          
    elif choice == "Translator":
        st.title('Speech Tranlation')
        row_text = st.text_area("Enter Your Text For Translation",height=300)
        translation_text = TextBlob(row_text)
        list1 = ["en","ta","pa","gu","hi","ur","kn","bn","te"]
        a= st.selectbox("select",list1)
        if st.button("search"):
            #input1 = TextBlob("Simple is better than complex")
            st.success(translation_text.translate(to=a))
    #Search Bar
    elif choice == "Search":
        st.title('Web Search')
        row_text= st.text_input("Search Anything")
        google = Google(license=None)
        if st.button("search"):
            for search_result in google.search(row_text):
                st.write(search_result.text)
                st.warning(search_result.url)
    elif choice == "Spell Correction":
        st.title('AI Spell Correction')
        text_data = st.text_area("Enter Text Here")
        a = TextBlob(text_data)
        if st.button("Correct"):
            st.success(a.correct())
        st.title('Pluralize & Singularize')
        text_data1 = st.text_input("Enter a word For pluralize / singularize")
        if st.checkbox("Pluralize"):
            st.warning(pluralize(text_data1))
        if st.checkbox("Singularize"):
            st.warning(singularize(text_data1))
        
        st.title('Compartitive & Superlative')
        text2 = st.text_input("Enter Text For comparative & superlative")
        if st.checkbox("Comparative"):
            st.success(comparative(text2))
        if st.checkbox("Superlative"):
            st.success(superlative(text2))
 
    #if st.checkbox("Show source code? "):
    #    st.code(display.show_code("core/calculator/CalcEngine.py"))
