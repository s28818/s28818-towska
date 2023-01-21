import time
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import datetime

st.title("Streamlit praca domowa")

page = st.sidebar.selectbox('Wybierz zakladke', ['Ankieta', 'Staty'])

if page == 'Ankieta':
    st.header('Ankieta')
    firstname = st.text_input("Wprowadz swoje imie", "...")
    lastname = st.text_input("Wprowadz swoje nazwisko", "...")
    if st.button("Submit"):
        result = "Imie i nazwisko zostaly zapisane poprawnie, " + firstname.title() + " " + lastname.title()
        st.success(result)
else:
    st.header('Staty')
    data = st.file_uploader("Wczytaj swoj plik", type=['csv'])
    if data is not None:
        with st.spinner("Ładowanie..."):
            time.sleep(1)
        df = pd.read_csv(data)
        st.dataframe(df.head(100))
        status = st.radio("Wybierz rodzaj wykresu", ("Liniowy", "Slupkowy"))
        if status == "Liniowy":                        #zrobione dla pliku 'winequality'
            columns = df.columns.to_list()
            plot_data = df[columns[1]]
            st.line_chart(plot_data)
        else:
            columns = df.columns.to_list()
            plot_data = df[columns[1]]
            st.bar_chart(plot_data)