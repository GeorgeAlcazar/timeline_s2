import streamlit as st
st.set_page_config(page_title="Sesion 2 | ISIL", layout="centered")
st.title("Volatilidad del tipo de cambio pronosticado")
st.write("Autor: George Alcazar | ISIL")
st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia del tipo de cambio en el Peru.")
# URLs de imágenes en GitHub
base_url = "https://github.com/GeorgeAlcazar/timeline_s2/blob/main/"
imagenes = {
   1: base_url + "timeline1.jpg",
   2: base_url + "timeline2.png",
   3: base_url + "timeline3.jpg",
   4: base_url + "timeline4.jpg",
   5: base_url + "timeline5.jpg"
}
# Slider
opcion = st.slider(
 "Selecciona un punto del timeline",
 min_value=1,
 max_value=5,
 value=1,
 step=1
)
# Mostrar imagen según slider
st.image(imagenes[opcion], use_container_width=True)
if opcion == 1:
 st.info(" Evolucion del tipo de cambio dolar 1990 - 2025.")
if opcion == 2:
 st.info(" factores externos del cambio del dolar ")
if opcion == 3:
 st.info(" factores internos del cambio del dolar ")
if opcion == 4:
 st.info(" Modelos para pronosticar el tipo de cambio ")
if opcion == 5:
 st.info(" Herramientas de ML para pronosticar ")
