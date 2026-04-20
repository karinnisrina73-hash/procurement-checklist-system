import streamlit as st
from PIL import Image
import pandas as pd
import os

st.set_page_config(layout="wide")

# ================= LOAD LOGO =================
logo = Image.open("Telkom-Akses-Logo-Vector.svg-.png")

# ================= HEADER =================
st.image(logo, width=200)

st.markdown("""
<h1 style='text-align: center; color:black; font-weight:bold;'>
CHECKLIST DOKUMEN MITRA / SUBKON
</h1>
<p style='text-align: center; color: black;'>
Sistem Verifikasi Dokumen Vendor - Divisi Procurement
</p>
""", unsafe_allow_html=True)

st.divider()

# ================= STYLE =================
st.markdown("""
<style>

/* Background PUTIH */
.stApp {
    background-color: white;
}

/* Card */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    border-left: 5px solid #D32F2F;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

/* Section title */
h3 {
    color: #B71C1C;
    font-weight: bold;
}

/* INPUT TEXT (merah transparan) */
.stTextInput input, 
.stTextArea textarea,
.stDateInput input {
    border-radius: 8px;
    border: none !important;
    background-color: rgba(211, 47, 47, 0.08);
}

/* Fokus */
.stTextInput input:focus, 
.stTextArea textarea:focus,
.stDateInput input:focus {
    background-color: rgba(211, 47, 47, 0.15);
    outline: none;
}

/* RADIO (dibikin clean, tanpa background) */
.stRadio > div {
    background-color: transparent !important;
    padding: 0px;
}

/* Button */
.stButton>button {
    background-color: #D32F2F;
    color: white;
    border-radius: 8px;
    height: 45px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #B71C1C;
}

</style>
""", unsafe_allow_html=True)

# ================= DATA PERUSAHAAN =================
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Data Perusahaan")

    col1, col2 = st.columns(2)

    with col1:
        nama = st.text_input("Nama Perusahaan")
        npwp = st.text_input("NPWP")
        uraian = st.text_input("Uraian Tagihan")
        kontrak = st.text_input("No Kontrak")
        po = st.text_input("No PO/SP")

    with col2:
        nilai = st.text_input("Nilai Tagihan")
        tagihan_ke = st.text_input("Tagihan Ke")
        periode = st.text_input("Periode")
        project = st.text_input("ID Project")
        apm = st.text_input("No APM")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= DATA BANK =================
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("ID Bank")

    col3, col4 = st.columns(2)

    with col3:
        bank = st.text_input("Nama Bank (sesuai kontrak)")
        rekening = st.text_input("No Rekening")

    with col4:
        atas_nama = st.text_input("Atas Nama")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= KELENGKAPAN =================
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Kelengkapan Dokumen")

    dokumen_list = [
        "Kwitansi",
        "Invoice / Faktur Penjualan",
        "Surat Permohonan Pembayaran",
        "Faktur Pajak",
        "Berita Acara Legalitas",
        "Berita Acara Quality Control (QC)",
        "Berita Acara Rekonsiliasi Material",
        "Berita Acara Uji Terima",
        "Berita Acara As-Built Drawing",
        "Berita Acara Rekonsiliasi",
        "Berita Acara Serah Terima",
        "Surat Penetapan",
        "Surat Kesanggupan",
        "Surat Pesanan",
        "Amandemen Surat Pesanan",
        "Jaminan Pemeliharaan"
    ]

    status_dokumen = []

    for doc in dokumen_list:
        col_a, col_b = st.columns([3,2])

        with col_a:
            st.write(doc)

        with col_b:
            pilihan = st.radio(
                label=doc,
                options=["Ada", "Tidak Ada"],
                horizontal=True,
                label_visibility="collapsed"
            )

        status_dokumen.append(pilihan)

    st.markdown('</div>', unsafe_allow_html=True)

# ================= LAMPIRAN =================
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Lampiran")

    lampiran_list = [
        "Fotokopi Kontrak",
        "Fotokopi Amandemen Kontrak",
        "Fotokopi SBUJK",
        "Jaminan Pelaksanaan",
        "Lain-lain"
    ]

    status_lampiran = []

    for doc in lampiran_list:
        col_a, col_b = st.columns([3,2])

        with col_a:
            st.write(doc)

        with col_b:
            pilihan = st.radio(
                label=doc,
                options=["Ada", "Tidak Ada"],
                horizontal=True,
                label_visibility="collapsed"
            )

        status_lampiran.append(pilihan)

    st.markdown('</div>', unsafe_allow_html=True)

# ================= STATUS =================
# ================= STATUS =================
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Status Verifikasi")

    # ================= OPTIONAL DOKUMEN =================
    optional_dokumen = [
        "Berita Acara Legalitas",
        "Berita Acara Quality Control (QC)"
    ]

    # ================= WAJIB LAMPIRAN =================
    wajib_lampiran = [
        "Fotokopi Kontrak",
        "Fotokopi Amandemen Kontrak",
        "Fotokopi SBUJK"
    ]

    # ================= CEK DOKUMEN =================
    dokumen_wajib_status = []

    for i, doc in enumerate(dokumen_list):
        if doc not in optional_dokumen:
            if status_dokumen[i] == "Tidak Ada":
                dokumen_wajib_status.append(doc)

    # ================= CEK LAMPIRAN =================
    lampiran_wajib_status = []

    for i, doc in enumerate(lampiran_list):
        if doc in wajib_lampiran:
            if status_lampiran[i] == "Tidak Ada":
                lampiran_wajib_status.append(doc)

    # ================= HASIL =================
    if not dokumen_wajib_status and not lampiran_wajib_status:
        st.success("Semua dokumen wajib lengkap")
    else:
        total_kurang = len(dokumen_wajib_status) + len(lampiran_wajib_status)
        st.warning(f"{total_kurang} dokumen wajib belum lengkap")

        if dokumen_wajib_status:
            st.write("Dokumen wajib yang belum ada:")
            for d in dokumen_wajib_status:
                st.write(f"- {d}")

        if lampiran_wajib_status:
            st.write("Lampiran wajib yang belum ada:")
            for l in lampiran_wajib_status:
                st.write(f"- {l}")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= TANGGAL =================
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Verifikasi")

    col5, col6 = st.columns(2)

    with col5:
        tgl_terima = st.date_input("Tanggal Berkas Diterima")

    with col6:
        tgl_verifikasi = st.date_input("Tanggal Berkas Diverifikasi")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= CATATAN =================
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Catatan / Keterangan Revisi")

    catatan = st.text_area("Isi catatan")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= BUTTON =================
if st.button("Simpan Data"):

    data = {
        "Nama Perusahaan": nama,
        "NPWP": npwp,
        "Uraian Tagihan": uraian,
        "No Kontrak": kontrak,
        "No PO/SP": po,
        "Nilai Tagihan": nilai,
        "Tagihan Ke": tagihan_ke,
        "Periode": periode,
        "ID Project": project,
        "No APM": apm,
        "Nama Bank": bank,
        "No Rekening": rekening,
        "Atas Nama": atas_nama,
        "Tanggal Terima": tgl_terima,
        "Tanggal Verifikasi": tgl_verifikasi,
        "Catatan": catatan
    }

    for i, doc in enumerate(dokumen_list):
        data[doc] = status_dokumen[i]

    for i, doc in enumerate(lampiran_list):
        data[doc] = status_lampiran[i]

    df = pd.DataFrame([data])

    file_path = "data_vendor.xlsx"

    if os.path.exists(file_path):
        df_existing = pd.read_excel(file_path)
        df_final = pd.concat([df_existing, df], ignore_index=True)
    else:
        df_final = df

    df_final.to_excel(file_path, index=False)

    st.success("Data berhasil disimpan ke Excel")
    
    # ================= DOWNLOAD EXCEL =================
if os.path.exists("data_vendor.xlsx"):
    with open("data_vendor.xlsx", "rb") as file:
        st.download_button(
            label="Download Data Excel",
            data=file,
            file_name="data_vendor.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )