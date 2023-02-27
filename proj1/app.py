import streamlit as st
import pandas as pd


df = pd.read_csv("resources/data/deniro_Imdb_Ratings.csv", on_bad_lines='skip')

st.title("Hello It's Dharmendra here")
st.header("We all know mr. :red[Deniro] :sunglasses: the Big star of Hollywood" )
st.text("Table given belowe shows the ratings got by IMDB for mr.Deniro Year Wise")
st.image("resources/images/ImageOfstar.jpg", caption="Deniro", width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")
st.write(df)
