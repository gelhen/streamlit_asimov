import streamlit as st
import pandas as pd
import time

st.set_page_config(
    layout="wide",
    page_title="Spotify Songs"
)

# supondo uma leituroa pesado do arquivo .csv
# para não ficar demorando, colocar em uma função de leitura
# para proteger a função load_data contra a lentidão com cache_data
# chama uma vez e garda na cache e toda vez que chamar novamente
# retorna o que esta no cache
@st.cache_data
def load_data():
    df = pd.read_csv("01 Spotify.csv")
    time.sleep(5)
    # openração pesada
    return df

df = load_data()
# criar uma sessao para ser utilizado em outra pagina
st.session_state["df_spotify"] = df

df.set_index("Track", inplace=True)

#Atista e quantas vezes apareceu com .value_counts() e para ser unico .index
artists = df["Artist"].value_counts().index
#recebe artista selecionado do listbox e inclui side bar
artist = st.sidebar.selectbox("Artista", artists)
df_filtered = df[df["Artist"] == artist]

#faz outro filtro
albuns = df_filtered["Album"].value_counts().index
album = st.selectbox("Album", albuns)

#novo filtro baseado no album
df_filtered2 = df[df["Album"] == album]

#cria colunas
#col1, col2 = st.columns(2)
col1, col2 = st.columns([0.7, 0.3])

col1.bar_chart(df_filtered2["Stream"])
col2.line_chart(df_filtered2["Danceability"])

st.write(artist)

