import streamlit as st

# Dados de exemplo
generos = ["Rock", "Metal", "MPB", "Reggaeton", "Sertanejo", "Internacional"]

# Dicionário relacionando gêneros aos seus livros
artista_por_genero = {
    "Rock": ["ACDC", "Guns 'n Roses", "Queen"],
    "Metal": ["Iron Maiden", "Metallica", "Megadeth"],
    "MPB": ["Natiruts", "Rita Lee", "Tribalistas"],
    "Reggaeton": ["Cris MJ", "Floyymenor"],
    "Sertanejo": ["Leandro & Leonardo", "Chitãozinho & Xororó", "Di paullo & Paulino"],
    "Internacional": ["Don Toliver", "Travis Scott"]
}

# Selectbox para escolher o gênero 
st.sidebar.image("logo.png")               
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    artista_selecionado = st.sidebar.selectbox(
        "Selecione o artista:", 
        artista_por_genero[genero_selecionado]
    )

# Mostrar apenas o artista selecionado
if genero_selecionado and artista_selecionado:
    st.write(f"**Gênero:** {genero_selecionado}")
    st.write(f"**Artista selecionado:** {artista_selecionado}")
    
# Mostrar a música 
if genero_selecionado == "Rock" and artista_selecionado == "ACDC":
    st.video("https://youtu.be/CiJeSSzu9Bo?si=4JpslvREul3SKjdF")

elif genero_selecionado == "Rock" and artista_selecionado == "Guns 'n Roses":
    st.video("https://youtu.be/Rbm6GXllBiw?si=WzkDmnWuOzj9MJBC")
    
elif genero_selecionado == "Rock" and artista_selecionado == "Queen":
    st.video("https://youtu.be/2ZBtPf7FOoM?si=XhK9r19PYLOcIqaQ")

elif genero_selecionado == "Metal" and artista_selecionado == "Iron Maiden":
    st.video("https://youtu.be/VjopV7Mamws?si=5cdqdwkYlSQisWM9")

elif genero_selecionado == "Metal" and artista_selecionado == "Metallica":
    st.video("https://youtu.be/A8MO7fkZc5o?si=7u2uujdYddvLE-nP")

elif genero_selecionado == "Metal" and artista_selecionado == "Megadeth":
    st.video("https://youtu.be/aU-dKoFZT0A?si=-vcSoC5BphPS8iD3")

elif genero_selecionado == "MPB" and artista_selecionado == "Natiruts":
    st.video("https://youtu.be/viJ0AQRuP5g?si=nJtz4pvOVWACbCzV")

elif genero_selecionado == "MPB" and artista_selecionado == "Rita Lee":
    st.video("https://youtu.be/bY0dFGo-XnQ?si=FNBarIci83TxbcHL")

elif genero_selecionado == "MPB" and artista_selecionado == "Tribalistas":
    st.video("https://youtu.be/7EylePeg4CE?si=MajOPlH9_DkpTWrA")

elif genero_selecionado == "Reggaeton" and artista_selecionado == "Cris MJ":
    st.video("https://youtu.be/JA92Akt_rQQ?si=Ov0KOtpyc_0h3G95")

elif genero_selecionado == "Reggaeton" and artista_selecionado == "Floyymenor":
    st.video("https://youtu.be/TnTfFWwf44U?si=pDdL-vRxQN8dPjc9")

elif genero_selecionado == "Sertanejo" and artista_selecionado == "Leandro & Leonardo":
    st.video("https://youtu.be/sMcmG2eLBXU?si=Viymq1Gr6J3lOrYn")

elif genero_selecionado == "Sertanejo" and artista_selecionado == "Chitãozinho & Xororó":
    st.video("https://youtu.be/8N-6CSOyCU4?si=RI6m1cxQweR99_Zx")

elif genero_selecionado == "Sertanejo" and artista_selecionado == "Di paullo & Paulino":
    st.video("https://youtu.be/dB3pltwZhVA?si=p6R1l9xlsHTu8wQA")

elif genero_selecionado == "Internacional" and artista_selecionado == "Don Toliver":
    st.video("https://youtu.be/4IahvCIqeOc?si=uU9dLuYJbnuQQVse")

elif genero_selecionado == "Internacional" and artista_selecionado == "Travis Scott":
    st.video("https://youtu.be/tfSS1e3kYeo?si=065jnR1OOXAuvRy1")


