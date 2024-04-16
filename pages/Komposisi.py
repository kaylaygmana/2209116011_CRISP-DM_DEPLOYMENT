import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import plotly.graph_objs as go

df = pd.read_csv("https://raw.githubusercontent.com/kaylaygmana/Tinjauan-pengaruh-jenis-kelamin-pada-respon-terhadap-obat-penunjang-suplemen-fisik/main/survey.csv.csv")
df = df.drop(['Age','Medicine1','Medicine2','Medicine3','SideEffects'], axis=1)


st.set_option('deprecation.showPyplotGlobalUse', False)
gender_distribution = df['Gender'].value_counts()
after_labels = ["Laki-laki", "Perempuan"]
colors = ['#e41a1c', '#d3d3d3']

fig = go.Figure(data=[go.Pie(labels=after_labels, values=gender_distribution.values, marker=dict(colors=colors))])



st.title("Komposisi gender pada dataset")
st.plotly_chart(fig, use_container_width=True)
st.subheader("Insight:")
st.write("Dari visualisasi, terlihat bahwa terdapat sedikit ketimpangan dalam representasi jenis kelamin dalam sampel yang digunakan dalam penelitian ini. Meskipun tidak signifikan, perbedaan antara persentase laki-laki (55.3%) dan persentase perempuan (44.7%) menunjukkan bahwa dataset cenderung sedikit lebih banyak mewakili laki-laki daripada perempuan.")

# Actionable Insight
st.subheader("Actionable Insight:")
st.write("Penting untuk memperhatikan representasi yang seimbang dari kedua jenis kelamin dalam dataset. Namun, tidak perlu melakukan tindakan khusus jika tidak ada ketimpangan yang signifikan. Dalam analisis lebih lanjut, hanya perlu memperhatikan potensi bias yang mungkin timbul akibat ketidakseimbangan tersebut.")
