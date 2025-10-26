import streamlit as st 
import pandas as pd

# Vaka bilgisi
vaka = {
    "ad": "Elif Kaya",
    "yas": 60,
    "lokalizasyon": "Yüz ve boyun",
    "yuzey_alani": 35,
    "derinlik": "Tam Kalınlık",
    "crp": 85,
    "wbc": 16,
    "agri": 9,
    "oksijen": 90
}

st.title("🧑‍⚕️ Yanık Vaka Simülasyonu")
st.subheader("📍 Vaka Bilgisi")
st.write(f"{vaka['ad']}, {vaka['yas']} yaşında, {vaka['lokalizasyon']} bölgesinde % {vaka['yuzey_alani']} {vaka['derinlik']} yanık.")
st.write(f"CRP: {vaka['crp']}, WBC: {vaka['wbc']}, Ağrı: {vaka['agri']}/10, Oksijen: %{vaka['oksijen']}")

# Yanıtları saklamak için boş DataFrame
if "yanitlar" not in st.session_state:
    st.session_state.yanitlar = pd.DataFrame(columns=["Öğrenci", "Enfeksiyon Riski", "Tedavi Planı", "Ağrı Yönetimi"])

# Öğrenci adı (zorunlu alan)
ogrenci = st.text_input("👩‍🎓 Öğrenci Adı (zorunlu)")
if not ogrenci:
    st.warning("Lütfen adınızı giriniz. Yanıt kaydı için zorunludur.")

# Sorular
cevap1 = st.radio("Soru 1: Bu hastada enfeksiyon riski var mı?", ["Evet", "Hayır"])
cevap2 = st.text_input("Soru 2: Tedavi planı ne olmalı?")
cevap3 = st.text_area("Soru 3: Ağrı yönetimi için öneriniz nedir?")

# Yanıtı kaydet
if st.button("Yanıtı Kaydet"):
    if ogrenci.strip() == "":
        st.error("❌ Öğrenci adı girilmeden yanıt kaydedilemez.")
    else:
        yeni_kayit = {
            "Öğrenci": ogrenci,
            "Enfeksiyon Riski": cevap1,
            "Tedavi Planı": cevap2,
            "Ağrı Yönetimi": cevap3
        }
        st.session_state.yanitlar = pd.concat([st.session_state.yanitlar, pd.DataFrame([yeni_kayit])], ignore_index=True)
        st.success("✅ Yanıt başarıyla kaydedildi.")

# Yanıtları göster
st.subheader("📊 Kaydedilen Yanıtlar")
st.dataframe(st.session_state.yanitlar)

# CSV indirme butonu
csv = st.session_state.yanitlar.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Yanıtları CSV olarak indir", data=csv, file_name="ogrenci_yanitlari.csv", mime="text/csv")
