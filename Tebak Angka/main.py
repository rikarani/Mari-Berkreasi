def batas_bawah() :
    a = int(input("Masukkan Batas Bawah : "))

    return a

def batas_atas() :
    b = int(input("Masukkan Batas Atas  : "))

    return b

def main() :
    import random

    # Tentukan Angka Misteri secara Random
    print("-------------------------")
    angka_misteri = random.randint(batas_bawah(),batas_atas()) # Nilai Randomnya dari Batas Bawah sampai Batas Atas
    print("-------------------------")

    # Angka Tebakan & Counter
    angka_tebakan = 0
    counter = 0

    # Perulangan
    while angka_tebakan != angka_misteri :
        counter += 1

        angka_tebakan = int(input("Masukkan Angka Tebakan Anda : "))

        if angka_tebakan < angka_misteri :
            print("Tebakan Anda Terlalu Kecil")
            print()
        elif angka_tebakan > angka_misteri :
            print("Tebakan Anda Terlalu Besar")
            print()
        else :
            print(f"Tebakan Anda Benar, Angka Misteri Adalah {angka_misteri}, Anda Mencoba sebanyak {counter} kali")


if __name__ == "__main__" :
    main()