from cProfile import label
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Mengatur tampilan aplikasi
st.title('K-means Clustering Untuk Mengidentifikasi Nilai Siswa Relatif Tinggi atau Relatif Rendah')

# Mengambil input dataset dari pengguna
st.write('Masukkan dataset siswa :')
uploaded_file = st.file_uploader("Pilih file Excel", type=["xlsx"])
if uploaded_file is not None:

    file_ext = uploaded_file.name.split(".")[-1]
    if file_ext == "xlsx":
        data_siswa = pd.read_excel(uploaded_file)
    st.write('Berikut Adalah Data Siswa Yang Akan Di Analisis:')
    st.dataframe(data_siswa)

    # Memilih jumlah klaster
    k = st.slider('Jumlah Klaster : ', min_value=2, max_value=10)

    

    # Memilih kolom nilai mata pelajaran
    selected_columns = ['Nilai_Tugas', 'Nilai_UTS', 'Nilai_UAS']

    # Melakukan klastering K-means
    kmeans = KMeans(n_clusters=k)
    matematika_data = data_siswa[selected_columns].copy()
    kmeans.fit(matematika_data)
    labels = kmeans.labels_

    # Menambahkan kolom klaster ke data siswa
    data_siswa['Klaster'] = kmeans.labels_

    # Menampilkan hasil klastering
    st.write('Hasil Klastering :')
    st.dataframe(data_siswa)


    # Menampilkan data siswa dalam klaster
    st.write("Data Klaster:")
    cluster_df = pd.DataFrame(data_siswa, columns=selected_columns)
    cluster_df["Klaster"] = labels
    for i in range(k):
        st.write(f"Klaster {i+1}:", cluster_df[cluster_df["Klaster"] == i])


    # Visualisasi hasil klastering
    fig, ax = plt.subplots()
    for cluster in range(k):
        cluster_data = data_siswa[data_siswa['Klaster'] == cluster]
        ax.scatter(cluster_data[selected_columns[0]], cluster_data[selected_columns[1]], cluster_data[selected_columns[2]], label=f'Klaster {cluster}')
    ax.set_xlabel(selected_columns[0])
    ax.set_ylabel(selected_columns[1])
    ax.set_title('K-means Clustering')
    ax.legend()
    st.pyplot(fig)
    

    
        
        

    
