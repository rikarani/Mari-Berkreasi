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
    if ribu > 0 :
        tabel += [tiga_digit(ribu), "Ribu"]

    satu = sisa_uang // 1
    sisa_uang = sisa_uang % 1
    if satu > 0 :
        tabel += [tiga_digit(satu)]

    return tabel

def tiga_digit(angka) :
    hasil = angka

    return hasil

def main() :
    jumlahUang = int(input())

    print(f"Terbilang : {terbilang(jumlahUang)}")

if __name__ == "__main__" :
    main()
