import streamlit as st
from neuron import Neuron

st.image("neurona.jpg", width=400)
# Título y descripción
st.title("Simulador de neurona")

cantidad = st.slider("Elige el número de entradas/pesos que tendrá la neurona", min_value=1, max_value=10, value=1, step=1)

st.subheader("Pesos")
pesos = []

col = st.columns(cantidad)
for i in range(cantidad):
    with col[i]:
        peso = st.number_input(f"Peso {i}", key=f"peso_{i}")
        pesos.append(peso)

st.write(f"w = {pesos}",)


st.subheader("Entradas")
entradas = []

col = st.columns(cantidad)
for i in range(cantidad):
    with col[i]:
        entrada = st.number_input(f"Entradas {i}", key=f"entrada_{i}")
        entradas.append(entrada)

st.write(f"w = {entradas}",)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Sesgo")
    sesgo = st.number_input("Introduce el valor del sesgo", key="sesgo")

with col2:
    st.subheader("Función de activación")
    func = st.selectbox("Elige la función de activación", ["Sigmoide", "ReLU", "Tangente hiperbólica", "Linear"], key="funcion_activacion")
    


if st.button("Calcular la salida", key="calcular_salida"):
    neuron = Neuron(pesos, sesgo, func)
    output = neuron.run(entradas)
    st.write(f"La salida de la neurona es {output}")
