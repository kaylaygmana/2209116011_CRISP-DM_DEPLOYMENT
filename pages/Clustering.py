import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import plotly.graph_objs as go
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler



df2 = pd.read_csv("https://raw.githubusercontent.com/kaylaygmana/Tinjauan-pengaruh-jenis-kelamin-pada-respon-terhadap-obat-penunjang-suplemen-fisik/main/Data%20Cleaned.csv")
# Konversi variabel kategorikal menjadi variabel numerik
df2['Gender'] = df2['Gender'].map({'M': 0, 'F': 1})

x = df2.drop('Gender', axis=1)
y = df2['Gender']


clust = st.slider("Pilih jumlah cluster:", 2, 5, 3, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

numeric_columns = x_train.select_dtypes(include=['int', 'float']).columns

scaler = MinMaxScaler()
x_train_norm = x_train.copy()
x_train_norm[numeric_columns] = scaler.fit_transform(x_train_norm[numeric_columns])

x_test_norm = x_test.copy()
x_test_norm[numeric_columns] = scaler.transform(x_test_norm[numeric_columns])

def k_means(n_clust, x_train, y_train):
    # Prapemrosesan data
    numeric_columns = x_train.select_dtypes(include=['int', 'float']).columns
    scaler = MinMaxScaler()
    x_train_norm = x_train.copy()
    x_train_norm[numeric_columns] = scaler.fit_transform(x_train_norm[numeric_columns])

    # Melatih model KMeans
    kmn = KMeans(n_clusters=n_clust)
    kmn.fit(x_train_norm[numeric_columns], y_train)

    # Menambahkan label kluster ke dataframe
    kmn_labels = kmn.labels_
    x_train_norm['Labels'] = kmn_labels

    # Visualisasi
    plt.figure(figsize=(10,8))
    sns.scatterplot(data=x_train_norm, x=x_train_norm.columns[0], y=x_train_norm.columns[1], hue='Labels', markers=True, size=10)

    # Menambahkan teks label kluster ke plot
    for label in x_train_norm['Labels'].unique():
        plt.text(x_train_norm[x_train_norm['Labels'] == label].iloc[:,0].mean(),
                 x_train_norm[x_train_norm['Labels'] == label].iloc[:,1].mean(),
                 f'Cluster {label}',
                 horizontalalignment='center',
                 verticalalignment='center',
                 size=20,
                 weight='bold',
                 color='black')
    
    # Menampilkan plot menggunakan Streamlit
    st.title("Kluster plot")
    st.pyplot()

    # Menampilkan data kluster
    st.write(x_train_norm)

st.set_option('deprecation.showPyplotGlobalUse', False)


# Memanggil fungsi k_means
k_means(clust, x_train_norm, y_train)
