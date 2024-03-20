import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px
# from numerize import numerize
import warnings 
warnings.filterwarnings('ignore')


st.set_page_config(layout='centered')

# read csv
df = pd.read_csv('dataset_pertamaa.csv')
print(df.head())

# df['order_date'] = pd.to_datetime(df['order_date'])
# df['ship_date'] = pd.to_datetime(df['ship_date'])

# df['order_year'] = df['order_date'].dt.year

# CURR_YEAR = max(df['order_date'].dt.year)
# PREV_YEAR = CURR_YEAR - 1

st.title("Stunting Kabupaten Jayapura Tahun 2021/2022")

# import streamlit as st

# Data
data_text = """
STUNTING ADALAH PROGRAM PRIORITAS NASIONAL, DIMANA PADA TAHUN 2024 MEMILIKI TARGET PENURUNAN HINGGA 14%. STUNTING ATAU SERING DISEBUT KERDIL ATAU PENDEK ADALAH KONDISI GAGAL TUMBUH PADA ANAK BERUSIA DIBAWAH LIMA TAHUN AKIBAT KEKURANGAN GIZI KRONIS DAN INFEKSI BERULANG TERUTAMA DALAM 1000 HARI PERTAMA KEHIDUPAN (HPK) YAITU DARI JANIN HINGGA ANAK BERUSIA 23 BULAN. 
AKSI KONVERGENSI MERUPAKAN UPAYA PEMERINTAH DAERAH BERSAMA OPD TERKAIT DAN SEMUA PELAKU PERCEPATAN PENURUNAN STUNTING, MULAI DARI TINGKAT PEMERINTAH DAERAH SAMPAI TINGKAT PEMERINTAH KAMPUNG, DALAM MENGAMBIL LANGKAH-LANGKAH UPAYA PERCEPATAN PENURUNAN STUNTING DI KABUPATEN JAYAPURA . DATA STUNTING YANG DI BAHAS ADALAH BERDASARKAN DISTRIK ATAU KECAMATAN YANG ADA DI KABUPATEN JAYAPURA SEBANYAK 19 DISTRIK YAITU Sentani", "Sentani Timur", "Depapre", "Sentani Barat", "Kemtuk", "Kemtuk Gresi", "Nimboran", "Nimbokrang", "Unurum Guay", "Demta","Kaureh" "Ebungfao", "Waibu", "Namblong", "Yapsi", "Airu", "Raveni Rara", "Yokari"
"""

# Menampilkan teks
st.write(data_text)


# paramemter start ke 1
# Fungsi untuk membuat diagram batang
def create_bar_chart(kecamatan, stunting):
    fig, ax = plt.subplots(figsize=(10, 6))  # Membuat objek gambar dan sumbu
    ax.bar(kecamatan, stunting)  # Melakukan plotting di sumbu
    ax.set_xlabel('Kecamatan')  # Mengatur label sumbu x
    ax.set_ylabel('Stunting')   # Mengatur label sumbu y
    ax.set_title('Diagram Batang Stunting per Kecamatan')  # Memberi judul plot
    plt.xticks(rotation=90)  # Memutar label kecamatan agar tegak
    st.pyplot(fig)  # Menampilkan plot menggunakan st.pyplot()

# Daftar kecamatan dan data stunting (contoh)
kecamatan = ["Sentani", "Sentani Timur", "Depapre", "Sentani Barat", "Kemtuk", "Kemtuk Gresi", "Nimboran", "Nimbokrang", "Unurum Guay", "Demta","Kaureh" "Ebungfao", "Waibu", "Namblong", "Yapsi", "Airu", "Raveni Rara", "Yokari"]
stunting = [10, 20, 15, 25, 30, 35, 20, 15, 10, 5, 10, 20, 15, 10, 20, 25, 15]
resiko_stunting = ["Beresiko Stunting","Tidak Beresiko stunting"]

# Menampilkan judul dan deskripsi
st.header('Aplikasi Diagram Batang Stunting per Kecamatan')
st.write('Aplikasi ini menampilkan diagram batang yang menunjukkan tingkat stunting di setiap kecamatan.')

# Menambahkan parameter menggunakan sidebar
with st.sidebar:
    st.title('Parameter')
    # Tambahkan slider untuk mengatur tingkat stunting
    stunting_threshold = st.slider('Batas Stunting', min_value=0, max_value=50, value=20, step=5)

# Filter kecamatan berdasarkan batas stunting
filtered_kecamatan = [kecamatan[i] for i in range(len(kecamatan)) if stunting[i] > stunting_threshold]
filtered_stunting = [stunting[i] for i in range(len(kecamatan)) if stunting[i] > stunting_threshold]

# Memanggil fungsi untuk membuat diagram batang
create_bar_chart(filtered_kecamatan, filtered_stunting)
# parameter end

# parameter start

# Menampilkan data storytelling berdasarkan kecamatan
st.write("## Data Storytelling Berdasarkan Kecamatan")

# Narasi untuk setiap kecamatan
for kecamatan, stunting_rate in zip(filtered_kecamatan, filtered_stunting):
    st.write(f"### Kecamatan {kecamatan}")
    st.write(f"Tingkat stunting di Kecamatan {kecamatan} adalah {stunting_rate}%.")

    # Menambahkan narasi spesifik berdasarkan tingkat stunting
    if stunting_rate > 20:
        st.write(f"Tingkat stunting di Kecamatan {kecamatan} tergolong tinggi. Hal ini memerlukan perhatian khusus dari pemerintah setempat untuk mengimplementasikan program-program kesehatan yang lebih efektif.")
    elif stunting_rate > 10:
        st.write(f"Tingkat stunting di Kecamatan {kecamatan} tergolong sedang. Upaya-upaya pencegahan dan intervensi harus terus dilakukan untuk mencegah peningkatan lebih lanjut.")
    else:
        st.write(f"Tingkat stunting di Kecamatan {kecamatan} relatif rendah. Ini menunjukkan keberhasilan dari kebijakan atau program kesehatan yang telah diterapkan di wilayah ini.")

    # Menambahkan visualisasi diagram batang untuk mendukung narasi
    st.write(f"#### Diagram Batang Tingkat Stunting di Kecamatan {kecamatan}")
    create_bar_chart([kecamatan], [stunting_rate])

# parameter end

# parameter lain ending



# # start storytelling ke 2
# # Data storytelling
# st.header('Data Storytelling')

# # Narasi
# st.write("Dalam analisis ini, kita melihat distribusi populasi kepala keluarga berdasarkan profesi dan tingkat resiko stunting. Profesi yang dianalisis adalah nelayan dan pedagang.")

# # Narasi berdasarkan profesi yang dipilih
# if selected_profesi:
#     st.write(f"Kita fokus pada populasi kepala keluarga dengan profesi {selected_profesi}.")
#     if selected_profesi == 'nelayan':
#         st.write("Nelayan adalah profesi yang memiliki resiko stunting tertinggi, dengan 77% kepala keluarga dalam kategori beresiko.")
#     elif selected_profesi == 'pedagang':
#         st.write("Pedagang memiliki resiko stunting yang sedikit lebih rendah dibandingkan nelayan, dengan 57% kepala keluarga dalam kategori beresiko.")

# # Narasi berdasarkan tingkat resiko stunting yang dipilih
# if selected_resiko:
#     st.write(f"Kita juga dapat melihat distribusi populasi berdasarkan tingkat resiko stunting. Jika kita memilih resiko stunting {selected_resiko}, maka sebanyak {jumlah} kepala keluarga dalam kategori tersebut.")

# # Kesimpulan
# st.write("Dari analisis ini, kita dapat menyimpulkan bahwa nelayan memiliki resiko stunting yang lebih tinggi dibandingkan dengan pedagang. Hal ini menunjukkan perlunya perhatian khusus terhadap kesehatan dan nutrisi di kalangan nelayan.")

# # end  storytelling ke 2

# start storytelling ke-5
# Data untuk kecamatan dekat laut
data_laut = {
    'Kecamatan': ['Depapre', 'Demta','Raveni Rara','Yokari'],
    'Lokasi': ['Laut', 'Laut','Laut','Laut']
}

# Data untuk kecamatan dekat danau
data_danau = {
    'Kecamatan': ['Sentani', 'Sentani Timur','Ebungfao','Sentani Barat','Waibu'],
    'Lokasi': ['Danau', 'Danau','Danau','Danau','Danau']
}

# Data untuk kecamatan di pegunungan
data_pegunungan = {
    'Kecamatan': ['Nimboran', 'Kemtuk Gresi','Kemtuk','Nimbokrang','Kaureh','Nambluong','Yapsi'],
    'Lokasi': ['Pegunungan', 'Pegunungan','Pegunungan','Pegunungan','Pegunungan','Pegunungan','Pegunungan']
}

# Data untuk kecamatan di sepanjang sungai
data_sungai = {
    'Kecamatan': ['Airu'],
    'Lokasi': ['Sungai']
}

# Menggabungkan data dari semua lokasi ke dalam satu DataFrame
df = pd.concat([pd.DataFrame(data_laut), pd.DataFrame(data_danau), pd.DataFrame(data_pegunungan), pd.DataFrame(data_sungai)], ignore_index=True)

# Menghitung jumlah kecamatan untuk setiap lokasi
count_per_location = df['Lokasi'].value_counts()

# Membuat diagram lingkaran berdasarkan jumlah kecamatan di setiap lokasi
fig = px.pie(names=count_per_location.index, values=count_per_location.values, title='Jumlah Kecamatan per Lokasi')

# Menampilkan diagram lingkaran di Streamlit
st.plotly_chart(fig)

# ending storytelling ke-5




