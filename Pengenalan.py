import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(
    page_title="Deployment",
)

st.title("Deployment")

st.subheader("Tinjauan pengaruh jenis kelamin pada respon tubuh terhadap suplemen penunjang fisik")
st.caption("Latar belakang situasi bisnis yang menginspirasi dilakukannya analisis ini adalah adanya variasi hasil antara kondisi sebelum dan setelah seseorang mengonsumsi obat untuk meningkatkan kebugaran tubuh. Dalam upaya untuk menggali pemahaman yang lebih mendalam terkait dengan dinamika ini, fokus penelitian difokuskan pada perbedaan respons antara pria dan wanita.")

df = pd.read_csv("https://raw.githubusercontent.com/kaylaygmana/Tinjauan-pengaruh-jenis-kelamin-pada-respon-terhadap-obat-penunjang-suplemen-fisik/main/survey.csv.csv")
df = df.drop(['Age', 'Medicine1', 'Medicine2', 'Medicine3', 'SideEffects'], axis=1)

st.header("Isi dataset")
st.write(df)
st.caption("Ini merupakan dataset yang digunakan untuk melakukan penelitian ini, yang menginvestigasi pengaruh jenis kelamin terhadap respon tubuh terhadap suplemen penunjang fisik. Dataset ini berisi informasi mengenai berbagai variabel seperti jenis kelamin, usia, dan lainnya. ")
