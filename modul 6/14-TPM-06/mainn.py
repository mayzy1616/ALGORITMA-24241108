# Input data pegawai
nama_pegawai = input("Masukkan nama pegawai: ")
status_pegawai = input("Masukkan status pegawai (tetap/tidak tetap): ").lower()
gaji_pokok = float(input("Masukkan gaji pokok: "))
durasi_lembur = float(input("Masukkan durasi lembur (jam): "))

# Perhitungan
if status_pegawai == "tetap": # Pegawai tetap
    tunjangan = 0.7 * gaji_pokok
    lembur = durasi_lembur * (0.1 * gaji_pokok)
    gaji_bersih = gaji_pokok + tunjangan + lembur
else:  # Pegawai tidak tetap
    tunjangan = 0
    lembur = durasi_lembur * (0.1 * gaji_pokok)
    gaji_bersih = gaji_pokok + lembur

# Output
print("\n--- Rincian Gaji Pegawai ---")
print(f"Nama Pegawai    : {nama_pegawai}")
print(f"Gaji Pokok      : Rp.{gaji_pokok:,.2f}")
print(f"Tunjangan       : Rp.{tunjangan:,.2f}")
print(f"Durasi Lembur   : {durasi_lembur} jam")
print(f"Gaji Bersih     : Rp.{gaji_bersih:,.2f}")