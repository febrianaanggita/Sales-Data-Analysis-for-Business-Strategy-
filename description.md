# Judul Project
`
Analisis Data Penjualan untuk Mendukung Strategi Bisnis`

## Repository Outline
```
1. README.md / description.md – Penjelasan umum project.

2. data/

- M3P2_Febriana_Putri_raw.csv – Dataset penjualan mentah.

- M3P2_Febriana_Putri_clean.csv – Dataset penjualan yang sudah dibersihkan.

3. dags/ – Script Airflow DAG untuk ETL pipeline.

- P2M3_Febriana_Putri_DAG.py – Script DAG utama ETL pipeline.

4. images/ – Visualisasi dashboard dan hasil eksplorasi.

- introduction & objective.png – Identitas & tujuan project.

- plot & insight 01–06.png – Hasil visualisasi dan insight dari data.

- Kesimpulan.png – Ringkasan insight dan rekomendasi bisnis.

5. gx/ – Konfigurasi Great Expectations untuk data validation.

6. notebooks/

- P2M3_Febriana_Putri_GX.ipynb – Exploratory data analysis & data validation.

7. P2M3_Febriana_Putri_ddl.txt – Struktur tabel database.

8. P2M3_Febriana_Putri_Conseptual.txt – Desain konseptual database.

9. P2M3_Febriana_Putri_DAG_graph.jpg – Ilustrasi workflow DAG.

10. airflow_ES.yaml – Konfigurasi Airflow untuk koneksi ke Elasticsearch.
```

## Problem Background
`
Dalam dunia bisnis modern, data penjualan memegang peranan penting dalam menentukan strategi perusahaan. Melalui analisis data, perusahaan dapat memahami pola pembelian pelanggan, produk dengan penjualan terbaik, serta faktor-faktor yang memengaruhi profitabilitas. Dengan adanya dataset penjualan yang memuat informasi seperti produk, pelanggan, wilayah, serta angka penjualan dan keuntungan, project ini bertujuan untuk menggali insight yang bermanfaat guna mendukung pengambilan keputusan berbasis data.`

## Project Output
`Dashboard interaktif Kibana untuk memvisualisasikan:

- Top 10 Customer dengan Profit Tertinggi

- Total Profit per Category

- Distribusi Metode Pembayaran

- Trend Penjualan Bulanan

- Distribusi Transaksi per State & Category (Heat Map)

- Detail Ringkasan Transaksi (Data Table)

- Insight bisnis dan rekomendasi yang dapat dijadikan acuan strategi perusahaan.`

## Data
`Dataset: M3P2_Febriana_Putri_raw.csv (mentah), M3P2_Febriana_Putri_clean.csv (hasil cleaning).

Isi data mencakup:

- Informasi transaksi (order_id, tanggal, customer, produk, kategori, state, city).

- Variabel numeric seperti amount dan profit.

- Ukuran data: ribuan baris dengan beberapa kolom utama.

- Proses data meliputi data cleaning, validasi dengan Great Expectations, dan ETL pipeline ke Elasticsearch.`

## Method
`Metode yang digunakan:

1. Data Cleaning – Menghapus duplikasi, menangani missing values, standarisasi field.

2. Data Validation (Great Expectations) – Memastikan data sesuai kualitas yang ditentukan.

3. ETL Pipeline (Airflow DAG) – Otomatisasi proses extract → clean → load ke Elasticsearch.

4. Dashboard Kibana – Visualisasi eksploratif untuk menemukan insight bisnis.

5. Analisis Insight – Menghubungkan hasil eksplorasi data dengan teori bisnis (customer relationship management, seasonal demand, market segmentation).`

## Stacks
`1. Bahasa & Tools: Python, SQL, Airflow, Kibana, Elasticsearch.

2. Library Python: pandas, numpy, matplotlib, seaborn, Great Expectations.

3. Deployment & Workflow: Airflow DAG, Elasticsearch, Kibana Dashboard.`

## Reference
`
1. Dokumentasi resmi: Elastic Kibana, Apache Airflow, Great Expectations`

---