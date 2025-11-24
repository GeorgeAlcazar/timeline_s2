
import streamlit as st

st.set_page_config(page_title="Sesion 2 | ISIL", layout="centered")
st.title("Volatilidad del tipo de cambio pronosticado")
st.write("Autor: George Alcazar | ISIL")
st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia del tipo de cambio en el Peru.")

# URLs de imágenes en GitHub (RAW)
base_url = "https://raw.githubusercontent.com/GeorgeAlcazar/timeline_s2/main/"
imagenes = {
    1: base_url + "timeline1.png",
    2: base_url + "timeline2.png",
    3: base_url + "timeline3.jpg",
    4: base_url + "timeline4.jpg",
    5: base_url + "timeline5.jpg",
}

opcion = st.slider("Selecciona un punto del timeline", min_value=1, max_value=5, value=1, step=1)

st.image(imagenes[opcion], use_container_width=True)

if opcion == 1:
    st.info("Evolución del tipo de cambio dólar 1990 - 2025.")
elif opcion == 2:
    st.info("Factores externos del cambio del dólar.")
elif opcion == 3:
    st.info("Factores internos del cambio del dólar.")
elif opcion == 4:
    st.info("Modelos para pronosticar el tipo de cambio.")
elif opcion == 5:
    st.info("Herramientas de ML para pronosticar.")

