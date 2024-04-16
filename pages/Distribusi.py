import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import plotly.graph_objs as go

st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.read_csv("https://raw.githubusercontent.com/kaylaygmana/Tinjauan-pengaruh-jenis-kelamin-pada-respon-terhadap-obat-penunjang-suplemen-fisik/main/survey.csv.csv")
df = df.drop(['Age','Medicine1','Medicine2','Medicine3','SideEffects'], axis=1)

df_numeric = df[["KmBefore", "KgBefore", "TimeBefore", "KmAfter", "KgAfter", "TimeAfter"]]


st.title("Distribusi")
fig, axes = plt.subplots(3, 2, figsize=(15, 15), constrained_layout=True)
for ax, col in zip(axes.flatten(), df_numeric.columns):
    ax.hist(df[col], bins=20, color='skyblue', edgecolor='black')
    ax.set_xlabel(col)
    ax.set_ylabel('Frequency')
    ax.set_title(f'Histogram of {col}')
st.pyplot()


st.subheader("Insight:")
st.write("Dari histrogram, terlihat bahwa distribusi data dalam setiap kolom tidak menyerupai kurva bell-shaped yang biasanya terkait dengan distribusi normal. Hal ini menunjukkan bahwa data mungkin tidak terdistribusi secara normal dan mungkin mengikuti pola distribusi yang berbeda atau memiliki skewness yang signifikan.")

# Actionable Insight
st.subheader("Actionable Insight:")
st.write("Mencari tahu apa yang menjadi penyebab distribusi data seperti itu.")
