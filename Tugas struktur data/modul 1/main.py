def main():
    data_mahasiswa = {}

    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

    for i in range(jumlah_mahasiswa):
        print(f"\nData Mahasiswa ke-{i + 1}")
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        mata_kuliah = []

        jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))
        for j in range(jumlah_mk):
            mk = input(f"  Nama Mata Kuliah ke-{j + 1}: ")
            nilai = float(input(f"  Nilai untuk {mk}: "))
            mata_kuliah.append((mk, nilai))

        data_mahasiswa[nim] = {
            'nama': nama,
            'nilai': mata_kuliah
        }

    print("\n===== Rekapitulasi Data Mahasiswa =====\n")
    for nim, info in data_mahasiswa.items():
        nama = info['nama']
        nilai_list = info['nilai']
        total_nilai = sum(nilai for _, nilai in nilai_list)
        rata_rata = total_nilai / len(nilai_list) if nilai_list else 0

        print(f"NIM: {nim}")
        print(f"Nama: {nama}")
        print("Nilai Mata Kuliah:")
        for mk, nilai in nilai_list:
            print(f"  - {mk}: {nilai}")
        print(f"Rata-rata Nilai: {rata_rata:.2f}")
        print("-" * 40)

if __name__ == "__main__":
    main()

