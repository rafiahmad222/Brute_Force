import csv
import pandas as pd
from pathlib import Path
import os

def input_user():
    os.system('cls')
    with open('data_mahasiswa.csv', 'a', newline='') as file:
        tambah = csv.writer(file, delimiter=',')
        data = pd.read_csv('data_mahasiswa.csv')
        no = len(data) + 1
        nama = input("Masukkan nama mahasiswa (kosongkan untuk selesai): ")
        nim = input("Masukkan NIM mahasiswa: ")
        nilai = int(input("Masukkan nilai mahasiswa: "))
        tambah.writerow([
                no, nama, nim, nilai
                ])
        file.close()
        print("Data berhasil ditambahkan!")
        input("Tekan enter untuk kembali ke menu")
        os.system('cls')
        menu()
            
def lihat_data():
    os.system('cls')
    print("1. Data Sebelum Diurutkan")
    print("2. Data Setelah Diurutkan")
    print("3. Kembali ke menu")
    pilihan = input("Pilih menu: ")
    if pilihan == '1':
        os.system('cls')
        data = pd.read_csv('data_mahasiswa.csv')      
        print(data)
        input("Tekan enter untuk kembali ke menu")
        os.system('cls')
        lihat_data()
    elif pilihan == '2':
        os.system('cls')
        data = pd.read_csv('data_mahasiswasort.csv')      
        print(data)
        input("Tekan enter untuk kembali ke menu")
        os.system('cls')
        lihat_data()
    elif pilihan == '3':
        os.system('cls')
        menu()
    else:
        print("Menu tidak valid!")
        lihat_data()
            
def brute_force_sort():
    os.system('cls')
    data = pd.read_csv('data_mahasiswa.csv')
    data.sort_values(by='Nilai' ,inplace=True)
    data['No'] = range(1, 1+len(data))
    data.to_csv('data_mahasiswasort.csv', index=False)
    print("Data mahasiswa telah diurutkan dalam file 'data_mahasiswasort.csv'")
    input("Tekan enter untuk kembali ke menu")
    menu()

def menu():
    os.system('cls')
    print("Menu:")
    print("1. Input data mahasiswa")
    print("2. Lihat data mahasiswa")
    print("3. Urutkan data mahasiswa")
    print("4. Keluar")
    pilihan = input("Pilih menu: ")
    
    if pilihan == '1':
        if not(Path('data_mahasiswa.csv').is_file()):
            with open('data_mahasiswa.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=[
                    'No', 'Nama', 'Nim', 'Nilai'
                    ],  delimiter=',') 
                header.writeheader()
        input_user()
    elif pilihan == '2':
        lihat_data()
    elif pilihan == '3':
        if not(Path('data_mahasiswasort.csv').is_file()):
                with open('data_mahasiswasort.csv', 'w', newline='') as filecsv:
                    header = csv.DictWriter(filecsv, fieldnames=[
                        'No', 'Nama', 'Nim', 'Nilai'
                        ],  delimiter=',') 
                    header.writeheader()
        brute_force_sort()
    elif pilihan == '4':
        print("Program selesai, sampai jumpa!")
        
if __name__ == "__main__":
    menu()