nominal = {
    1 : 'Satu',
    2 : 'Dua',
    3 : 'Tiga',
    4 : 'Empat',
    5 : 'Lima',
    6 : 'Enam',
    7 : 'Tujuh',
    8 : 'Delapan',
    9 : 'Sembilan'
}

# ----------------- Input -------------------
uang = int(input()) # Max 11000 (Sebelas Ribu)
# -------------------------------------------

# ----------------------------
puluh_ribu = uang // 10000
sisa_uang = uang % 10000

ribuan = sisa_uang // 1000
sisa_uang = sisa_uang % 1000

ratusan = sisa_uang // 100
sisa_uang = sisa_uang % 100

puluhan = sisa_uang // 10
sisa_uang = sisa_uang % 10

satuan = sisa_uang // 1
# ----------------------------

# ------------------------- Pemilihan -----------------------------
if puluh_ribu == 1 and (ribuan == 1 and ratusan == 0 and puluhan == 0 and satuan == 0) :
    print("Sebelas Ribu")

# 10000
elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 0 and puluhan == 0 and satuan == 0) :
    print("Sepuluh Ribu")

elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 0 and puluhan == 0 and satuan != 0) :
    print(f"Sepuluh Ribu {nominal[satuan]}")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 0 and puluhan == 1 and satuan == 0) :
    print("Sepuluh Ribu Sepuluh")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 0 and puluhan == 1 and satuan == 1) :
    print("Sepuluh Ribu Sebelas")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 0 and puluhan == 1 and satuan != 1) :
    print(f"Sepuluh Ribu {nominal[satuan]} Belas")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 0 and puluhan != 1 and satuan == 0) :
    print(f"Sepuluh Ribu {nominal[puluhan]} Puluh")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 0 and puluhan != 1 and satuan != 0) :
    print(f"Sepuluh Ribu {nominal[puluhan]} Puluh {nominal[satuan]}")

elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 1 and puluhan == 0 and satuan == 0) :
    print(f"Sepuluh Ribu Seratus")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 1 and puluhan == 0 and satuan != 0) :
    print(f"Sepuluh Ribu Seratus {nominal[satuan]}")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 1 and puluhan == 1 and satuan == 0) :
    print(f"Sepuluh Ribu Seratus Sepuluh")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 1 and puluhan == 1 and satuan == 1) :
    print(f"Sepuluh Ribu Seratus Sebelas")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 1 and puluhan == 1 and satuan != 1) :
    print(f"Sepuluh Ribu Seratus {nominal[satuan]} Belas")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 1 and puluhan != 1 and satuan == 0) :
    print(f"Sepuluh Ribu Seratus {nominal[puluhan]} Puluh")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan == 1 and puluhan != 1 and satuan != 0) :
    print(f"Sepuluh Ribu Seratus {nominal[puluhan]} Puluh {nominal[satuan]}")

elif puluh_ribu == 1 and (ribuan == 0 and ratusan != 1 and puluhan == 0 and satuan == 0) :
    print(f"Sepuluh Ribu {nominal[ratusan]} Ratus")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan != 1 and puluhan == 0 and satuan != 0) :
    print(f"Sepuluh Ribu {nominal[ratusan]} Ratus {nominal[satuan]}")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan != 1 and puluhan == 1 and satuan == 0) :
    print(f"Sepuluh Ribu {nominal[ratusan]} Ratus Sepuluh")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan != 1 and puluhan == 1 and satuan == 1) :
    print(f"Sepuluh Ribu {nominal[ratusan]} Ratus Sebelas")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan != 1 and puluhan == 1 and satuan != 1) :
    print(f"Sepuluh Ribu {nominal[ratusan]} Ratus {nominal[satuan]} Belas")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan != 1 and puluhan != 1 and satuan == 0) :
    print(f"Sepuluh Ribu {nominal[ratusan]} Ratus {nominal[puluhan]} Puluh")
elif puluh_ribu == 1 and (ribuan == 0 and ratusan != 1 and puluhan != 1 and satuan != 0) :
    print(f"Sepuluh Ribu {nominal[ratusan]} Ratus {nominal[puluhan]} Puluh {nominal[satuan]}")

# 4 Digit (1000 ~ 9999)
elif ribuan == 1 and (ratusan == 0 and puluhan == 0 and satuan == 0) :
    print("Seribu")

elif ribuan == 1 and (ratusan == 0 and puluhan == 0 and satuan != 0) :
    print(f"Seribu {nominal[satuan]}")
elif ribuan == 1 and (ratusan == 0 and puluhan == 1 and satuan == 0) :
    print(f"Seribu Sepuluh")
elif ribuan == 1 and (ratusan == 0 and puluhan == 1 and satuan == 1) :
    print(f"Seribu Sebelas")
elif ribuan == 1 and (ratusan == 0 and puluhan == 1 and satuan != 1) :
    print(f"Seribu {nominal[satuan]} Belas")

elif ribuan == 1 and (ratusan == 0 and puluhan != 1 and satuan == 0) :
    print(f"Seribu {nominal[puluhan]} Puluh")
elif ribuan == 1 and (ratusan == 0 and puluhan != 1 and satuan != 0) :
    print(f"Seribu {nominal[puluhan]} Puluh {nominal[satuan]}")

elif ribuan == 1 and (ratusan == 1 and puluhan == 0 and satuan == 0) :
    print(f"Seribu Seratus")
elif ribuan == 1 and (ratusan == 1 and puluhan == 0 and satuan != 0) :
    print(f"Seribu Seratus {nominal[satuan]}")
elif ribuan == 1 and (ratusan == 1 and puluhan == 1 and satuan == 0) :
    print(f"Seribu Seratus Sepuluh")
elif ribuan == 1 and (ratusan == 1 and puluhan == 1 and satuan == 1) :
    print(f"Seribu Seratus Sebelas")
elif ribuan == 1 and (ratusan == 1 and puluhan == 1 and satuan != 1) :
    print(f"Seribu Seratus {nominal[satuan]}")

elif ribuan == 1 and (ratusan == 1 and puluhan != 1 and satuan == 0) :
    print(f"Seribu Seratus {nominal[puluhan]} Puluh")
elif ribuan == 1 and (ratusan == 1 and puluhan != 1 and satuan != 0) :
    print(f"Seribu Seratus {nominal[puluhan]} Puluh {nominal[satuan]}")

elif ribuan == 1 and (ratusan != 1 and puluhan == 0 and satuan == 0) :
    print(f"Seribu {nominal[ratusan]} Ratus")

elif ribuan == 1 and (ratusan != 1 and puluhan == 0 and satuan != 0) :
    print(f"Seribu {nominal[ratusan]} Ratus {nominal[satuan]}")

elif ribuan == 1 and (ratusan != 1 and puluhan == 1 and satuan == 0) :
    print(f"Seribu {nominal[ratusan]} Ratus Sepuluh")

elif ribuan == 1 and (ratusan != 1 and puluhan == 1 and satuan == 1) :
    print(f"Seribu {nominal[ratusan]} Sebelas")
elif ribuan == 1 and (ratusan != 1 and puluhan == 1 and satuan != 1) :
    print(f"Seribu {nominal[ratusan]} Ratus {nominal[satuan]} Belas")

elif ribuan == 1 and (ratusan != 1 and puluhan != 1 and satuan == 0) :
    print(f"Seribu {nominal[ratusan]} Ratus {nominal[puluhan]} Puluh")
elif ribuan == 1 and (ratusan != 1 and puluhan != 1 and satuan != 0) :
    print(f"Seribu {nominal[ratusan]} Ratus {nominal[puluhan]} Puluh {nominal[satuan]}")

elif (ribuan != 0 and ribuan != 1) and (ratusan == 0 and puluhan == 0 and satuan == 0) :
    print(f"{nominal[ribuan]} Ribu")

elif (ribuan != 0 and ribuan != 1) and (ratusan == 0 and puluhan == 0 and satuan != 0) :
    print(f"{nominal[ribuan]} Ribu {nominal[satuan]}")

elif (ribuan != 0 and ribuan != 1) and (ratusan == 0 and puluhan == 1 and satuan == 0) :
    print(f"{nominal[ribuan]} Ribu Sepuluh")
elif (ribuan != 0 and ribuan != 1) and (ratusan == 0 and puluhan == 1 and satuan == 1) :
    print(f"{nominal[ribuan]} Ribu Sebelas")
elif (ribuan != 0 and ribuan != 1) and (ratusan == 0 and puluhan == 1 and satuan != 1) :
    print(f"{nominal[ribuan]} Ribu {nominal[satuan]} Belas")

elif (ribuan != 0 and ribuan != 1) and (ratusan == 0 and puluhan != 1 and satuan == 0) :
    print(f"{nominal[ribuan]} Ribu {nominal[puluhan]} Puluh")
elif (ribuan != 0 and ribuan != 1) and (ratusan == 0 and puluhan != 1 and satuan != 0) :
    print(f"{nominal[ribuan]} Ribu {nominal[puluhan]} Puluh {nominal[satuan]}")

elif (ribuan != 0 and ribuan != 1) and (ratusan == 1 and puluhan == 0 and satuan == 0) :
    print(f"{nominal[ribuan]} Ribu Seratus")

elif (ribuan != 0 and ribuan != 1) and (ratusan == 1 and puluhan == 0 and satuan != 0) :
    print(f"{nominal[ribuan]} Ribu Seratus {nominal[satuan]}")

elif (ribuan != 0 and ribuan != 1) and (ratusan == 1 and puluhan == 1 and satuan == 0) :
    print(f"{nominal[ribuan]} Ribu Seratus Sepuluh")
elif (ribuan != 0 and ribuan != 1) and (ratusan == 1 and puluhan == 1 and satuan == 1) :
    print(f"{nominal[ribuan]} Ribu Seratus Sebelas")
elif (ribuan != 0 and ribuan != 1) and (ratusan == 1 and puluhan == 1 and satuan != 1) :
    print(f"{nominal[ribuan]} Ribu Seratus {nominal[satuan]} Belas")

elif (ribuan != 0 and ribuan != 1) and (ratusan == 1 and puluhan != 1 and satuan == 0) :
    print(f"{nominal[ribuan]} Ribu Seratus {nominal[puluhan]} Puluh")
elif (ribuan != 0 and ribuan != 1) and (ratusan == 1 and puluhan != 1 and satuan != 0) :
    print(f"{nominal[ribuan]} Ribu Seratus {nominal[puluhan]} Puluh {nominal[satuan]}")

elif (ribuan != 0 and ribuan != 1) and (ratusan != 1 and puluhan == 0 and satuan == 0) :
    print(f"{nominal[ribuan]} Ribu {nominal[ratusan]} Ratus")

elif (ribuan != 0 and ribuan != 1) and (ratusan != 1 and puluhan == 0 and satuan != 0) :
    print(f"{nominal[ribuan]} Ribu {nominal[ratusan]} Ratus {nominal[satuan]}")

elif (ribuan != 0 and ribuan != 1) and (ratusan != 1 and puluhan == 1 and satuan == 0) :
    print(f"{nominal[ribuan]} Ribu {nominal[ratusan]} Ratus Sepuluh")
elif (ribuan != 0 and ribuan != 1) and (ratusan != 1 and puluhan == 1 and satuan == 1) :
    print(f"{nominal[ribuan]} Ribu {nominal[ratusan]} Ratus Sebelas")
elif (ribuan != 0 and ribuan != 1) and (ratusan != 1 and puluhan == 1 and satuan != 1) :
    print(f"{nominal[ribuan]} Ribu {nominal[ratusan]} Ratus {nominal[satuan]} Belas")

elif (ribuan != 0 and ribuan != 1) and (ratusan != 1 and puluhan != 1 and satuan == 0) :
    print(f"{nominal[ribuan]} Ribu {nominal[ratusan]} Ratus {nominal[puluhan]} Puluh")
elif (ribuan != 0 and ribuan != 1) and (ratusan != 1 and puluhan != 1 and satuan != 0) :
    print(f"{nominal[ribuan]} Ribu {nominal[ratusan]} Ratus {nominal[puluhan]} Puluh {nominal[satuan]}")

# 3 Digit
elif ratusan == 1 and (puluhan == 0 and satuan == 0) :
    print("Seratus")

elif ratusan == 1 and (puluhan == 0 and satuan != 0) :
    print(f"Seratus {nominal[satuan]}")

elif ratusan == 1 and (puluhan == 1 and satuan == 0) :
    print(f"Seratus Sepuluh")
elif ratusan == 1 and (puluhan == 1 and satuan == 1) :
    print(f"Seratus Sebelas")
elif ratusan == 1 and (puluhan == 1 and satuan != 1) :
    print(f"Seratus {nominal[satuan]} Belas")

elif ratusan == 1 and (puluhan != 1 and satuan == 0) :
    print(f"Seratus {nominal[puluhan]} Puluh")
elif ratusan == 1 and (puluhan != 1 and satuan != 0) :
    print(f"Seratus {nominal[puluhan]} Puluh {nominal[satuan]}")

elif (ratusan != 0 and ratusan != 1) and (puluhan == 0 and satuan == 0) :
    print(f"{nominal[ratusan]} Ratus")

elif (ratusan != 0 and ratusan != 1) and (puluhan == 0 and satuan != 0) :
    print(f"{nominal[ratusan]} Ratus {nominal[satuan]}")

elif (ratusan != 0 and ratusan != 1) and (puluhan == 1 and satuan == 0) :
    print(f"{nominal[ratusan]} Ratus Sepuluh")
elif (ratusan != 0 and ratusan != 1) and (puluhan == 1 and satuan == 1) :
    print(f"{nominal[ratusan]} Ratus Sebelas")
elif (ratusan != 0 and ratusan != 1) and (puluhan == 1 and satuan != 1) :
    print(f"{nominal[ratusan]} Ratus {nominal[satuan]} Belas")

elif (ratusan != 0 and ratusan != 1) and (puluhan != 1 and satuan == 0) :
    print(f"{nominal[ratusan]} Ratus {nominal[puluhan]} Puluh")
elif (ratusan != 0 and ratusan != 1) and (puluhan != 1 and satuan != 0) :
    print(f"{nominal[ratusan]} Ratus {nominal[puluhan]} Puluh {nominal[satuan]}")

# 2 Digit
elif puluhan == 1 and (satuan == 0) :
    print("Sepuluh")

elif puluhan == 1 and (satuan == 1) :
    print("Sebelas")
elif puluhan == 1 and (satuan != 1) :
    print(f"{nominal[satuan]} Belas")

elif (puluhan != 0 and puluhan != 1) and (satuan == 0) :
    print(f"{nominal[puluhan]} Puluh")
elif (puluhan != 0 and puluhan != 1) and (satuan != 0) :
    print(f"{nominal[puluhan]} Puluh {nominal[satuan]}")

# 1 Digit
elif satuan == 0 :
    print("Nol")
elif satuan != 0 :
    print(f"{nominal[satuan]}")
# -----------------------------------------------------------------