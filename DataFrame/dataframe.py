import pandas as pd

#1. Data Frame
data_list = [
    ['Kabupaten Tasikmalaya',753.06,2019],
    ['Kabupaten Tasikmalaya',754,2020],
    ['Kabupaten Tasikmalaya',172.26,2021],
    ['Kabupaten Ciamis',560.57,2019],
    ['Kabupaten Ciamis',564,2020],
    ['Kabupaten Ciamis',159.41,2021],
    ['Kabupaten Pangandaran',250.23,2019],
    ['Kabupaten Pangandaran',252.01,2020],
    ['Kabupaten Pangandaran',46.62,2021],
]
df = pd.DataFrame(data_list, columns=['Kabupaten/Kota', 'Produksi Sampah (Ton)', 'Tahun'])

print(df)

#2. Total produksi sampah di seluruh Kabupaten/Kota pada tahun tertentu (Tahun 2020)
tahun_tertentu = 2020
total_per_tahun = 0

for index, row in df.iterrows():
    if row['Tahun'] == tahun_tertentu:
        total_per_tahun += row['Produksi Sampah (Ton)']

print(f"Total produksi sampah di seluruh Kabupaten/Kota pada tahun {tahun_tertentu} adalah {total_per_tahun:.2f} ton.")

#3. Jumlah data per tahun
total_per_tahun = {}

for index, row in df.iterrows():
    tahun = row['Tahun']
    total_per_tahun[tahun] = total_per_tahun.get(tahun, 0) + row['Produksi Sampah (Ton)']

for tahun, total in total_per_tahun.items():
    print(f"Total produksi sampah pada tahun {tahun}: {total:.2f} ton")

#4. Jumlah data per kota/kabupaten per tahun
total_per_kabupaten = {}

for index, row in df.iterrows():
    kabupaten = row['Kabupaten/Kota']
    tahun = row['Tahun']
    key = (kabupaten, tahun)
    total_per_kabupaten[key] = total_per_kabupaten.get(key, 0) + row['Produksi Sampah (Ton)']

for (kabupaten, tahun), total in total_per_kabupaten.items():
    print(f"Total produksi sampah di {kabupaten} pada tahun {tahun}: {total:.2f} ton")

# Membuat DataFrame untuk hasil perhitungan
results_list = []

for (kabupaten, tahun), total in total_per_kabupaten.items():
    results_list.append({'Kabupaten/Kota': kabupaten, 'Tahun': tahun, 'Total Produksi Sampah (Ton)': total})

results_df = pd.DataFrame(results_list)

print(results_df)

# Ekspor DataFrame ke file CSV
results_df.to_csv('total_produksi_sampah_per_kabupaten.csv', index=False)
print("Hasil perhitungan telah diekspor ke file CSV.")

# Ekspor DataFrame ke file Excel
results_df.to_excel('total_produksi_sampah_per_kabupaten.xlsx', index=False, sheet_name='Produksi Sampah')
print("Hasil perhitungan telah diekspor ke file Excel.")




