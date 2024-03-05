import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv("main_data.csv")

with st.sidebar:
    # Logo Perusahaan
    st.image("public/logo.png")
    
    name = st.text_input(label='Nama', value='')
    st.write('Selamat Datang ', name, '!')
    
    role = st.selectbox(
    label="Role",
    options=('Worker', 'Advissor', 'CEO')
    )
 
st.header('Laporan Sewa Sepeda :bike:')

st.subheader("Penjualan Musiman")
fig, ax = plt.subplots(figsize=(10, 5))
 
sns.barplot(
    y="cnt", 
    x="season",
    data=all_df,
    ax=ax
)
    
ax.set_title("Jumlah Penyewaan Sepeda berdasarkan Musim", loc="center", fontsize=26)
ax.set_ylabel("banyak_rent", fontsize="20")
ax.set_xlabel("musim", fontsize="20")
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=20)
plt.xticks(ticks=[0, 1, 2, 3], labels=["Spring", "Summer", "Fall", "Winter"])
st.pyplot(fig)

    
with st.expander("Lebih lanjut"):
 st.write(
    """Persebaran jumlah sewa sepeda tertinggi terdapat pada musim ketiga (Fall) diikuti musim kedua (Summer), musim keempat (Winter) dan terakhir musim pertama (Spring). Musim juga berpengaruh terhadap jumlah penyewaan sepeda
            """
  )
 
st.subheader("Penjualan dengan pengaruh faktor cuaca")
fig, ax = plt.subplots(figsize=(10, 5))
 
sns.barplot(
    y="cnt", 
    x="weathersit",
    data=all_df,
    ax=ax
)
    
ax.set_title("Jumlah Penyewaan Sepeda dipengaruhi Cuaca", loc="center", fontsize=26)
ax.set_ylabel("banyak_rent", fontsize="20")
ax.set_xlabel("weather", fontsize="20")
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=20)
plt.xticks(ticks=[0, 1, 2, 3], labels=["Clear", "Mist", "Light Precipitation", "Heavy Precipitation"])
st.pyplot(fig)

    
with st.expander("Lebih lanjut"):
 st.write(
    """Cuaca menjadi faktor yang berpengaruh dalam banyaknya jumlah penyewaan sepeda,hal ini terlihat pada cuaca ke-4 (Hujan lebat) dengan jumlah terendah dalam penyewaan sepeda rendah
            """
  )
 
