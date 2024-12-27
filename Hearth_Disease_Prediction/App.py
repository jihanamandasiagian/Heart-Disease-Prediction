import streamlit as st
import numpy as np
from Model import main  # Pastikan Anda memiliki fungsi `main` yang diimpor dari file Model.py

# Judul aplikasi
st.title("Heart Disease Prediction App")

# Deskripsi aplikasi
st.write("Masukkan data berikut untuk memprediksi kemungkinan penyakit jantung:")

# Form input untuk data pengguna
with st.form("prediction_form"):
    # Input numerik
    age = st.number_input("Umur (Age):", min_value=0, max_value=120, step=1, value=30)
    trestbps = st.number_input("Tekanan Darah (Trestbps):", min_value=0, step=1, value=120)
    chol = st.number_input("Kolesterol (Chol):", min_value=0, step=1, value=200)
    oldpeak = st.number_input("Depresi ST (Oldpeak):", min_value=0.0, step=0.1, value=1.0)
    ca = st.number_input("Jumlah Pembuluh Darah Berwarna (CA):", min_value=0, max_value=4, step=1, value=0)
    thalch = st.number_input("Denyut Jantung Maksimum (Thalach):", min_value=0, step=1, value=150)

    # Input kategori untuk "Chest Pain Type (CP)"
    st.write("Jenis Nyeri Dada (Chest Pain Type):")
    cp_asymptomatic = st.checkbox("Asymptomatic", key="cp_asymptomatic")
    cp_atypical_angina = st.checkbox("Atypical Angina", key="cp_atypical_angina")
    cp_non_anginal = st.checkbox("Non-Anginal Pain", key="cp_non_anginal")
    cp_typical_angina = st.checkbox("Typical Angina", key="cp_typical_angina")

    # Input kategori untuk "Resting ECG (Restecg)"
    st.write("Hasil Elektrokardiogram (Restecg):")
    restecg_lv_hypertrophy = st.checkbox("Left Ventricular Hypertrophy", key="restecg_lv_hypertrophy")
    restecg_normal = st.checkbox("Normal", key="restecg_normal")
    restecg_st_t_abnormality = st.checkbox("ST-T Wave Abnormality", key="restecg_st_t_abnormality")

    # Input kategori untuk "Gender (Sex)"
    st.write("Jenis Kelamin (Sex):")
    sex_female = st.checkbox("Female", key="sex_female")
    sex_male = st.checkbox("Male", key="sex_male")

    # Input kategori untuk "Exercise-Induced Angina (Exang)"
    st.write("Angina yang Diinduksi Olahraga (Exang):")
    exang_false = st.checkbox("False", key="exang_false")
    exang_true = st.checkbox("True", key="exang_true")

    # Input kategori untuk "Fasting Blood Sugar (FBS)"
    st.write("Gula Darah Puasa (FBS):")
    fbs_false = st.checkbox("False", key="fbs_false")
    fbs_true = st.checkbox("True", key="fbs_true")

    # Tombol submit
    submitted = st.form_submit_button("Prediksi")

# Jika tombol submit ditekan
if submitted:
    # Masukkan data input ke dalam list
    input_data = [
        float(age),
        float(trestbps),
        float(chol),
        float(oldpeak),
        int(ca),
        int(thalch),

        int(cp_asymptomatic),
        int(cp_atypical_angina),
        int(cp_non_anginal),
        int(cp_typical_angina),

        int(restecg_lv_hypertrophy),
        int(restecg_normal),
        int(restecg_st_t_abnormality),

        int(sex_female),
        int(sex_male),

        int(exang_false),
        int(exang_true),
        int(fbs_false),
        int(fbs_true)
    ]

    # Panggil fungsi prediksi
    prediction = main(input_data)

    # Tampilkan hasil prediksi
    if prediction >= 1:
        st.success(f"Prediksi: Kemungkinan penyakit jantung (Heart Disease {prediction})")
    else:
        st.success("Prediksi: Tidak ada penyakit jantung")
