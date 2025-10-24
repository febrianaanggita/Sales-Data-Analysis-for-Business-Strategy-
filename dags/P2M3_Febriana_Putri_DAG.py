'''
=================================================
Milestone 3

Nama   : Febriana Putri Anggita  
Batch  : FTDS-031-HCK  

Program ini dibuat untuk melakukan automatisasi proses extract, transform, dan load (ETL) data dari PostgreSQL ke ElasticSearch. 
Adapun dataset yang dipakai adalah dataset penjualan yang berisi informasi transaksi pelanggan, produk, kategori, lokasi, serta nilai penjualan dan profit. 
Hasil akhir dari proses ini divisualisasikan dalam bentuk dashboard interaktif di Kibana untuk mendukung analisis data penjualan dan pengambilan keputusan bisnis.
=================================================
'''


import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from dateutil import parser
from elasticsearch import Elasticsearch


default_args= {
    'owner': 'Febriana',
    'start_date': datetime(2024, 11, 1), # sesuai instruksi mulai 1 Nov 2024
    "retries": 1,
}

with DAG(
    'P2M3_Febriana_Putri_DAG',
    description='from gdrive to postgres',
    schedule_interval='10-30/10 9 * * 6',
    default_args=default_args, 
    catchup=False) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    @task()
    def insert_to_db():

        '''
        Fungsi ini mengambil data dari PostgreSQL dan menyimpannya
        ke dalam file CSV mentah untuk proses lebih lanjut.

        Parameters:
         - Tidak ada parameter eksternal (konfigurasi database dihardcode di dalam function)

        Output:
         - File CSV 'M3P2_Febriana_Putri_raw.csv' di folder /opt/airflow/data

        Contoh penggunaan (dijalankan otomatis oleh DAG):
         insert_to_db()
        '''

        database = "airflow"
        username = "airflow"
        password = "airflow"
        host = "postgres"

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

        engine = create_engine(postgres_url)
        conn = engine.connect()

        df = pd.read_sql('select* from table_m3', conn)
        df.to_csv('/opt/airflow/data/M3P2_Febriana_Putri_raw.csv', index=False)
        print("Success INSERT")

    @task()
    def preprocess_data():

        '''
        Fungsi ini melakukan data cleaning pada dataset mentah:
         - Normalisasi nama kolom
         - Handling missing values (numeric → mean, categorical → 'unknown')
         - Konversi kolom datetime
         - Pembuatan kolom transaction_id sebagai primary key unik
         - Menghapus duplikasi data

        Parameters:
         - Tidak ada parameter eksternal (file input dibaca dari path default)

        Output:
         - File CSV 'M3P2_Febriana_Putri_clean.csv' di folder /opt/airflow/data

        Contoh penggunaan (dijalankan otomatis oleh DAG):
         preprocess_data()
        '''

        # pembacaan data mentah
        df = pd.read_csv('/opt/airflow/data/M3P2_Febriana_Putri_raw.csv')

        # Normalisasi nama kolom
        df.columns = (
        df.columns.str.strip()                  # hapus spasi depan/belakang
                 .str.lower()                   # ubah jadi lowercase
                 .str.replace(" ", "_")         # spasi → underscore
                 .str.replace(r"[^a-z0-9_]", "", regex=True)  # buang simbol aneh
        )

        # Handling missing values
        # numeric → isi mean
        num_cols = df.select_dtypes(include="number").columns
        df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

        # non-numeric → isi 'unknown'
        cat_cols = df.select_dtypes(exclude="number").columns
        df[cat_cols] = df[cat_cols].fillna("unknown")

        # kolom datetime
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

        # Membuat kolom baru berdasarkan kolom order_id, customername & order_date menjadi transaction_id (pk)
        df["transaction_id"] = (
            df["order_id"].astype(str) + "_" +
            df["customer_name"].astype(str).str.replace(" ", "") + "_" +
            df["order_date"].dt.strftime("%Y-%m-%d"))

        # Drop duplicate 
        df.drop_duplicates(subset=["transaction_id"], inplace=True)

        # Simpan hasil cleaning
        print(df.head())
        df.to_csv('/opt/airflow/data/M3P2_Febriana_Putri_clean.csv', index=False)

    @task()
    def load_data():

        '''
        Fungsi ini memuat data hasil cleaning dari CSV dan mengindeksnya
        ke Elasticsearch agar dapat digunakan untuk analisis lebih lanjut
        di Kibana.

        Parameters:
         - Tidak ada parameter eksternal (file input dibaca dari path default)

        Output:
         - Data terindeks di Elasticsearch index 'data_latihan'

        Contoh penggunaan (dijalankan otomatis oleh DAG):
         load_data()
        '''
        
        es = Elasticsearch("http://elasticsearch:9200")
        df = pd.read_csv('/opt/airflow/data/M3P2_Febriana_Putri_clean.csv')

        for i, row in df.iterrows():
            res = es.index(index="data_latihan", id=i+1, body=row.to_dict())

    start >> insert_to_db() >> preprocess_data() >> load_data() >> end
