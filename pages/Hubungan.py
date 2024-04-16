import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import plotly.graph_objs as go

st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.read_csv("https://raw.githubusercontent.com/kaylaygmana/Tinjauan-pengaruh-jenis-kelamin-pada-respon-terhadap-obat-penunjang-suplemen-fisik/main/survey.csv.csv")
df = df.drop(['Age','Medicine1','Medicine2','Medicine3','SideEffects'], axis=1)

st.title("Hubungan")
male_data = df[df['Gender'] == 'M']
female_data = df[df['Gender'] == 'F']

before_columns = ["KmBefore", "KgBefore", "TimeBefore"]
after_columns = ["KmAfter", "KgAfter", "TimeAfter"]

before_labels = ["KM", "KG", "TIME"]
after_labels = ["KM", "KG", "TIME"]

plt.figure(figsize=(7, 4))
bar_width = 0.35
light_ash_grey = '#d3d3d3'

# Male Before
bars_before_male = plt.bar([index - bar_width/2 for index in range(len(before_columns))],
                           male_data[before_columns].mean(), bar_width, label='Male Before', color=[light_ash_grey, light_ash_grey, light_ash_grey])

for bar, value, std in zip(bars_before_male, male_data[before_columns].mean(), male_data[before_columns].std()):
    plt.errorbar(bar.get_x() + bar.get_width() / 2, value,
                 yerr=std, color='black', capsize=5, capthick=2, fmt='none')
    plt.text(bar.get_x() + bar.get_width() / 2, value + std + 1, f"{value:.2f}", ha='center')

# Male After
bars_after_male = plt.bar([index + bar_width/2 for index in range(len(after_columns))],
                          male_data[after_columns].mean(), bar_width, label='Male After', color=['orange', 'orange', 'orange'])

for bar, value, std in zip(bars_after_male, male_data[after_columns].mean(), male_data[after_columns].std()):
    plt.errorbar(bar.get_x() + bar.get_width() / 2, value,
                 yerr=std, color='black', capsize=5, capthick=2, fmt='none')

    plt.text(bar.get_x() + bar.get_width() / 2, value + std + 1, f"{value:.2f}", ha='center')

plt.title("Male Participants - Before and After")
plt.xlabel("Variables")
plt.ylabel("Average Values")
plt.xticks(range(len(before_columns)), before_labels)
plt.legend()

st.pyplot()

plt.figure(figsize=(7, 4))

# Female Before
bars_before_female = plt.bar([index - bar_width/2 for index in range(len(before_columns))],
                             female_data[before_columns].mean(), bar_width, label='Female Before', color=[light_ash_grey, light_ash_grey, light_ash_grey])

for bar, value, std in zip(bars_before_female, female_data[before_columns].mean(), female_data[before_columns].std()):
    plt.errorbar(bar.get_x() + bar.get_width() / 2, value,
                 yerr=std, color='black', capsize=5, capthick=2, fmt='none')

    plt.text(bar.get_x() + bar.get_width() / 2, value + std + 1, f"{value:.2f}", ha='center')

# Female After
bars_after_female = plt.bar([index + bar_width/2 for index in range(len(after_columns))],
                            female_data[after_columns].mean(), bar_width, label='Female After', color=['orange', 'orange', 'orange'])

for bar, value, std in zip(bars_after_female, female_data[after_columns].mean(), female_data[after_columns].std()):
    plt.errorbar(bar.get_x() + bar.get_width() / 2, value,
                 yerr=std, color='black', capsize=5, capthick=2, fmt='none')

    plt.text(bar.get_x() + bar.get_width() / 2, value + std + 1, f"{value:.2f}", ha='center')

plt.title("Female Participants - Before and After")
plt.xlabel("Variables")
plt.ylabel("Average Values")
plt.xticks(range(len(before_columns)), before_labels)
plt.legend()

st.pyplot()

st.caption("Gambar di atas merupakan visualisasi perbandingan sebelum (abu-abu) dan sesudah (oranye) individu mengonsumsi obat suplemen penunjang fisik.")

st.subheader("Insight:")
st.write("Terdapat hubungan yang konsisten antara jarak yang ditempuh, berat badan, dan waktu yang dibutuhkan untuk peserta pria dan wanita. Peningkatan jarak yang ditempuh umumnya berhubungan dengan peningkatan berat badan dan waktu yang dibutuhkan.")

st.subheader("Actionable insight:")

st.markdown("Memperhatikan faktor-faktor lain yang mungkin memengaruhi hubungan antara jarak, berat badan, dan waktu, seperti intensitas latihan, jenis latihan, dan faktor-faktor kebugaran lainnya.")