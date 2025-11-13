import streamlit as st

st.title("ALTÉZZA")
st.subheader("Suba no salto e conquiste o mundo")

st.sidebar.image("logo dois.png")
st.sidebar.write("Sua marca mais que especial")

# --- BARRA DE NAVEGAÇÃO (menu horizontal) ---
opcao = st.radio(
    "Menu",
    ["Início", "Coleção", "Promoções", "Sobre Nós", "Contato"],
    horizontal=True  # deixa os botões na horizontal
)

# --- CONTEÚDO DINÂMICO ---
if opcao == "Início":
    st.write("✨ Bem-vinda à Altézza — onde cada passo é poder e elegância.")
    st.image("logo.png", caption=None, use_container_width=True)

elif opcao == "Coleção":
    st.write("👠 Confira nossa coleção de saltos elegantes!")
    
    # Barra para escolher tipo de salto
    tipo_salto = st.radio(
        "Escolha o tipo de salto:",
        ["Saltos Altos", "Anabelas", "Plataformas"],
        horizontal=True
    )

    # --- Mostrar imagem do tipo de salto ---
    if tipo_salto == "Saltos Altos":
        st.write("💖 Saltos Altos — elegância clássica!")
        st.image("salto alto.png", caption="Saltos Altos", use_container_width=True)

    elif tipo_salto == "Anabelas":
        st.write("🌸 Anabelas — conforto e estilo!")
        st.image("anabela.png", caption="Anabelas", use_container_width=True)

    elif tipo_salto == "Plataformas":
        st.write("✨ Plataformas — ousadia e atitude!")
        st.image("plataforma.png", caption="Plataformas", use_container_width=True)

    # --- Personalização de qualquer salto ---
    st.markdown("---")
    st.subheader("✨ Personalize seu salto")

    # Escolher marca
    marcas = ["LOUBOUTIN", "SAINT LAURENT", "GUCCI", "DIOR", "VERSACE", "VALENTINO", "VIZZANO"]
    marca = st.selectbox("Escolha a marca:", marcas)

    # Escolher tamanho
    tamanhos = [34, 35, 36, 37, 38, 39, 40]
    tamanho = st.selectbox("Escolha o tamanho:", tamanhos)

    # Preços base
    precos_base = {
        "LOUBOUTIN": 3500.0,
        "SAINT LAURENT": 3200.0,
        "GUCCI": 3000.0,
        "DIOR": 4000.0,
        "VERSACE": 2800.0,
        "VALENTINO": 3300.0,
        "VIZZANO": 250.0
    }

    # Adicionais por tamanho
    adicionais_tamanho = {
        34: 0.0,
        35: 20.0,
        36: 40.0,
        37: 60.0,
        38: 80.0,
        39: 100.0,
        40: 120.0
    }

    # Calcular preço final
    preco_final = precos_base[marca] + adicionais_tamanho[tamanho]

    st.success(f"Você escolheu um salto **{tipo_salto} {marca}** tamanho **{tamanho}**.")
    st.info(f"💎 Valor final: R$ {preco_final:.2f}")

# --- Promoções ---
elif opcao == "Promoções":
    st.write("💸 Promoções imperdíveis desta semana!")
    st.image("promoção.png", caption="Descontos", use_container_width=True)

# --- Sobre Nós ---
elif opcao == "Sobre Nós":
    st.write("💖 Altézza é feita para mulheres que caminham com confiança e estilo.")
    st.image("about me.png", caption="Nossa história", use_container_width=True)

# --- Contato ---
elif opcao == "Contato":
    st.write("📬 Entre em contato conosco pelo WhatsApp ou Instagram!")
    st.image("contato.png", caption="Fale conosco", use_container_width=True)