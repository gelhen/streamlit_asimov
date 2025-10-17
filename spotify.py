import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="Spotify Songs"
)

df = pd.read_csv("01 Spotify.csv")

df.set_index("Track", inplace=True)

#Atista e quantas vezes apareceu com .value_counts() e para ser unico .index
artists = df["Artist"].value_counts().index
#recebe artista selecionado do listbox
artist = st.selectbox("Artista", artists)
df_filtered = df[df["Artist"] == artist]

#faz outro filtro
albuns = df_filtered["Album"].value_counts().index
album = st.selectbox("Album", albuns)

#novo filtro baseado no album
df_filtered2 = df[df["Album"] == album]

display = st.checkbox("Display")
if display:
    st.bar_chart(df_filtered2["Stream"])

st.write(artist)

df