import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import plotly.graph_objs as go

df = pd.read_csv("https://raw.githubusercontent.com/kaylaygmana/Tinjauan-pengaruh-jenis-kelamin-pada-respon-terhadap-obat-penunjang-suplemen-fisik/main/survey.csv.csv")
df = df.drop(['Age','Medicine1','Medicine2','Medicine3','SideEffects'], axis=1)

st.title("Perbandingan")

# Memproses data untuk mendapatkan selisih
female_data = df[df['Gender'] == "F"]
male_data = df[df['Gender'] == "M"]

female_KmBefore_mean = female_data['KmBefore'].mean()
male_KmBefore_mean = male_data['KmBefore'].mean()
female_KmAfter_mean = female_data['KmAfter'].mean()
male_KmAfter_mean = male_data['KmAfter'].mean()

selisihKmFemale = female_KmAfter_mean - female_KmBefore_mean
selisihKmMale = male_KmAfter_mean - male_KmBefore_mean

female_KgBefore_mean = female_data['KgBefore'].mean()
male_KgBefore_mean = male_data['KgBefore'].mean()
female_KgAfter_mean = female_data['KgAfter'].mean()
male_KgAfter_mean = male_data['KgAfter'].mean()

selisihKgFemale = female_KgAfter_mean - female_KgBefore_mean
selisihKgMale = male_KgAfter_mean - male_KgBefore_mean

female_TimeBefore_mean = female_data['TimeBefore'].mean()
male_TimeBefore_mean = male_data['TimeBefore'].mean()
female_TimeAfter_mean = female_data['TimeAfter'].mean()
male_TimeAfter_mean = male_data['TimeAfter'].mean()

selisihTimeFemale = female_TimeAfter_mean - female_TimeBefore_mean
selisihTimeMale = male_TimeAfter_mean - male_TimeBefore_mean

# Membuat line chart untuk membandingkan perbedaan antara pria dan wanita
plt.plot(['Km', 'Kg', 'Time'], [selisihKmFemale, selisihKgFemale, selisihTimeFemale], marker='o', label='Female')
plt.plot(['Km', 'Kg', 'Time'], [selisihKmMale, selisihKgMale, selisihTimeMale], marker='o', label='Male')

# Menambahkan label, judul, dan legenda
plt.xlabel('Variabel')
plt.ylabel('Selisih')
plt.title('Perbandingan Selisih Antara Pria dan Wanita setelah Mengonsumsi Suplemen')
plt.legend()
st.pyplot()

st.subheader("Insight:")
st.write("Dari analisis yang telah dilakukan, dapat dilihat bahwa perbedaan selisih antara pria dan wanita tidak begitu signifikan. Namun, terdapat keunggulan pada perubahan berat badan pada pria dibandingkan wanita, serta peningkatan waktu tempuh lari yang lebih tinggi pada pria")
st.subheader("Actionable Insight:")
st.write("Meningkatkan kegiatan aktivitas untuk wanita agar perubahan selisih sebelum dan sesudah meminum suplemen dapat seimbang antar gender.")
