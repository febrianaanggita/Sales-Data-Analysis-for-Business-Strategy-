<h1 align="center">Sales Data Analysis for Business Strategy
</h1>

## Problem Background

<div align="justify">

Dalam dunia bisnis modern, data penjualan memegang peranan penting dalam menentukan strategi perusahaan. Melalui analisis data, perusahaan dapat memahami pola pembelian pelanggan, produk dengan penjualan terbaik, serta faktor-faktor yang memengaruhi profitabilitas. Dengan adanya dataset penjualan yang memuat informasi seperti produk, pelanggan, wilayah, serta angka penjualan dan keuntungan, project ini bertujuan untuk menggali insight yang bermanfaat guna mendukung pengambilan keputusan berbasis data.

## Project Output

<div align="justify">

Dashboard interaktif Kibana untuk memvisualisasikan:

- Top 10 Customer dengan Profit Tertinggi

- Total Profit per Category

- Distribusi Metode Pembayaran

- Trend Penjualan Bulanan

- Distribusi Transaksi per State & Category (Heat Map)

- Detail Ringkasan Transaksi (Data Table)

- Insight bisnis dan rekomendasi yang dapat dijadikan acuan strategi perusahaan.

## Data

<div align="justify">

Dataset: M3P2_Febriana_Putri_raw.csv (mentah), M3P2_Febriana_Putri_clean.csv (hasil cleaning).

Isi data mencakup:

- Informasi transaksi (order_id, tanggal, customer, produk, kategori, state, city).

- Variabel numeric seperti amount dan profit.

- Ukuran data: ribuan baris dengan beberapa kolom utama.

- Proses data meliputi data cleaning, validasi dengan Great Expectations, dan ETL pipeline ke Elasticsearch.

## Repository Outline

<div align="justify">

 ```
  Sales Data Analysis for Business Strategy 
  |
  ├── description.md
  ├── File_ddl.txt
  ├── M3P2_Febriana_Putri_raw.csv
  ├── M3P2_Febriana_Putri_clean.csv
  ├── M3P2_Febriana_Putri_DAG.py
  ├── P2M3_Febriana_Putri_graph.jpg
  ├── P2M3_Febriana_Putri_conceptual.txt
  ├── P2M3_Febriana_Putri_GX.ipynb
  ├── README.md
  ├── /images
        ├── introduction & objective.png
        ├── plot & insight 01.png
        ├── plot & insight 02.png
        ├── plot & insight 03.png
        ├── plot & insight 04.png
        ├── plot & insight 05.png
        ├── plot & insight 06.png
        └── kesimpulan.png
  ```

---

