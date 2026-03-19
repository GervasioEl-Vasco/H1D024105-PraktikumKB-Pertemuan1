import random          # Library 1: untuk menghasilkan data acak
import statistics      # Library 2: untuk perhitungan statistik
import math            # Library 3: untuk operasi matematika
from datetime import datetime       # Library 4: untuk tanggal & waktu
from collections import Counter     # Library 5: untuk menghitung frekuensi

def buat_data_nilai(jumlah_mahasiswa):
    """Membuat data nilai mahasiswa secara acak."""
    nama_depan = ["Andi", "Budi", "Citra", "Dewi", "Eko",
                  "Fitri", "Galih", "Hana", "Irfan", "Joko",
                  "Kartini", "Lukman", "Maya", "Nanda", "Oki",
                  "Putri", "Rafi", "Sari", "Toni", "Umi"]

    mata_kuliah = ("Kecerdasan Buatan", "Struktur Data", "Basis Data")  # TUPLE

    data_mahasiswa = []  # LIST

    nim_set = set()  

    counter = 0
    while counter < jumlah_mahasiswa:
        nim = f"H1D0{random.randint(20, 24)}0{random.randint(10, 150)}"

        # Gunakan SET untuk cek duplikasi NIM
        if nim in nim_set:
            continue  # skip jika NIM sudah ada
        nim_set.add(nim)

        nama = random.choice(nama_depan)
        nilai = {}
        for mk in mata_kuliah:
            nilai[mk] = random.randint(30, 100)

        data_mahasiswa.append({
            "nim": nim,
            "nama": nama,
            "nilai": nilai
        })
        counter += 1

    return data_mahasiswa, mata_kuliah, nim_set


def konversi_huruf(angka):
    if angka >= 85:
        return "A"
    elif angka >= 75:
        return "B"
    elif angka >= 60:
        return "C"
    elif angka >= 50:
        return "D"
    else:
        return "E"


def analisis_statistik(daftar_nilai):
    rata_rata = statistics.mean(daftar_nilai)
    median = statistics.median(daftar_nilai)
    stdev = statistics.stdev(daftar_nilai) if len(daftar_nilai) > 1 else 0
    variansi = statistics.variance(daftar_nilai) if len(daftar_nilai) > 1 else 0
    nilai_max = max(daftar_nilai)
    nilai_min = min(daftar_nilai)
    rentang = nilai_max - nilai_min

    return {
        "rata_rata": round(rata_rata, 2),
        "median": median,
        "std_deviasi": round(stdev, 2),
        "variansi": round(variansi, 2),
        "max": nilai_max,
        "min": nilai_min,
        "rentang": rentang
    }


def tampilkan_distribusi_grade(grades):
    freq = Counter(grades)
    urutan = ["A", "B", "C", "D", "E"]

    print("\n  Distribusi Nilai:")
    print("  " + "-" * 35)
    for grade in urutan:
        jumlah = freq.get(grade, 0)
        bar = "█" * jumlah + "░" * (20 - jumlah)
        print(f"  {grade} | {bar} ({jumlah})")
    print("  " + "-" * 35)




def main():
    jumlah = 15
    data, mata_kuliah, nim_unik = buat_data_nilai(jumlah)

    print(f"\n Data {jumlah} mahasiswa berhasil di-generate")
    print(f" Mata kuliah: {', '.join(mata_kuliah)}")
    print(f" Jumlah NIM: {len(nim_unik)}")

    print("\n" + "=" * 70)
    print(f" {'No':>3} | {'NIM':<16} | {'Nama':<10} | ", end="")
    for mk in mata_kuliah:
        singkatan = ''.join([kata[0] for kata in mk.split()])
        print(f"{singkatan:>4} ", end="")
    print(f" | {'Rata²':>6} | {'Grade'}")
    print("-" * 70)

    semua_rata = []
    semua_grade = []

    for idx, mhs in enumerate(data):
        no = idx + 1
        nilai_list = list(mhs["nilai"].values())
        rata = statistics.mean(nilai_list)
        grade = konversi_huruf(rata)

        semua_rata.append(rata)
        semua_grade.append(grade)

        print(f" {no:>3} | {mhs['nim']:<16} | {mhs['nama']:<10} | ", end="")
        for mk in mata_kuliah:
            print(f"{mhs['nilai'][mk]:>4} ", end="")
        print(f" | {rata:>6.1f} | {grade}")

    print("-" * 70)

    print("\n ANALISIS STATISTIK")
    print("=" * 45)

    for mk in mata_kuliah:
        nilai_mk = [mhs["nilai"][mk] for mhs in data]
        stats = analisis_statistik(nilai_mk)

        print(f"\n {mk}")
        print(f"     Rata-rata     : {stats['rata_rata']}")
        print(f"     Median        : {stats['median']}")
        print(f"     Std. Deviasi  : {stats['std_deviasi']}")
        print(f"     Nilai Maks    : {stats['max']}")
        print(f"     Nilai Min     : {stats['min']}")
        print(f"     Rentang       : {stats['rentang']}")

    print("\n" + "=" * 45)
    print("STATISTIK RATA-RATA KESELURUHAN")
    stats_total = analisis_statistik(semua_rata)
    print(f"     Rata-rata kelas    : {stats_total['rata_rata']}")
    print(f"     Median kelas       : {stats_total['median']}")
    print(f"     Std. Deviasi       : {stats_total['std_deviasi']}")
    print(f"     Variansi           : {stats_total['variansi']}")

    tampilkan_distribusi_grade(semua_grade)

    print("\n MAHASISWA TERBAIK:")
    nilai_tertinggi = max(semua_rata)
    for i, mhs in enumerate(data):
        if semua_rata[i] == nilai_tertinggi:
            print(f" {mhs['nama']} ({mhs['nim']}) - Rata-rata: {nilai_tertinggi:.1f}")
            break

    print("\n MAHASISWA YANG PERLU PERBAIKAN (Grade D atau E):")
    ada_perbaikan = False
    for i, mhs in enumerate(data):
        if semua_grade[i] in {"D", "E"}:  # menggunakan SET untuk pengecekan
            print(f" {mhs['nama']} ({mhs['nim']}) - Grade: {semua_grade[i]} ({semua_rata[i]:.1f})")
            ada_perbaikan = True

    if not ada_perbaikan:
        print(" Semua mahasiswa memiliki grade C atau lebih baik!")

if __name__ == "__main__":
    main()
