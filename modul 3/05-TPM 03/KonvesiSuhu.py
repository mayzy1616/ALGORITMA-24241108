 # meminta input dari pengguna dalam fahrenheit
fahrenheit = float (input("masukkan temperatur dalam fahrenheit: "))

# mengonversi fahrenheit ke celcius
celcius = (fahrenheit - 32) * 5 / 9

# menampilkan hasil konversi
print (f"{fahrenheit} derajat fahrenheit sama dengan {celcius:.2f}derajat celcius.")