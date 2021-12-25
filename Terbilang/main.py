def terbilang(uang) :
    tabel = []

    triliun = uang // 1_000_000_000_000
    sisa_uang = uang % 1_000_000_000_000
    if triliun > 0 :
        tabel += [tiga_digit(triliun), "Triliun"]

    milyar = sisa_uang // 1_000_000_000
    sisa_uang = sisa_uang % 1_000_000_000
    if milyar > 0 :
        tabel += [tiga_digit(milyar), "Milyar"]

    juta = sisa_uang // 1_000_000
    sisa_uang = sisa_uang % 1_000_000
    if juta > 0 :
        tabel += [tiga_digit(juta), "Juta"]

    ribu = sisa_uang // 1_000
    sisa_uang = sisa_uang % 1_000
    if ribu == 1 :
        tabel += ["Seribu"]
    elif ribu > 1 :
        tabel += [tiga_digit(ribu), "Ribu"]

    satu = sisa_uang // 1
    sisa_uang = sisa_uang % 1
    if satu > 0 :
        tabel += [tiga_digit(satu)]

    return " ".join(tabel)

def tiga_digit(angka) :
    nominal = {
        1 : "Satu",
        2 : "Dua",
        3 : "Tiga",
        4 : "Empat",
        5 : "Lima",
        6 : "Enam",
        7 : "Tujuh",
        8 : "Delapan",
        9 : "Sembilan",
    }
    hasil = []

    ratusan = angka // 100
    sisa_angka = angka % 100
    if ratusan == 1 :
        hasil.append("Seratus")
    elif ratusan > 1 :
        hasil.append(f"{nominal[ratusan]} Ratus")

    puluhan = sisa_angka // 10
    satuan = sisa_angka % 10
    if puluhan == 1 :
        if satuan == 0 :
            hasil.append("Sepuluh")
        elif satuan == 1 :
            hasil.append("Sebelas")
        else :
            hasil.append(f"{nominal[satuan]} Belas")
            satuan = 0
    elif puluhan > 1 :
        hasil.append(f"{nominal[puluhan]} Puluh")

    if satuan > 0 :
        hasil.append(nominal[satuan])

    return " ".join(hasil)

def main() :
    jumlahUang = int(input("Masukkan Jumlah Uang : "))

    print(f"Terbilang : {terbilang(jumlahUang)}")

if __name__ == "__main__" :
    main()
