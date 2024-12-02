pip install streamlit
pip install math

import streamlit as st
import math

# Judul aplikasi
st.title("Aplikasi Penghitung Luas Lingkaran")

# Input jari-jari lingkaran
jari_jari = st.number_input("Masukkan jari-jari lingkaran:", min_value=0.0, step=0.1)

# Tombol untuk menghitung luas
if st.button("Hitung Luas"):
    luas = math.pi * jari_jari ** 2
    st.write(f"Luas lingkaran dengan jari-jari {jari_jari} adalah: {luas:.2f}")
else:
    st.write("Masukkan jari-jari dan tekan tombol 'Hitung Luas'")
