def hitung_luas_lingkaran(jari_jari):
    luas = ( jari_jari ** 2)
    return luas 

# meminta imput dari pengguna
jari-jari = float (imput("masukkan jari-jari lingkaran: "))
luas = hitung_luas_lingkaran(jari_jari)

print (F"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")