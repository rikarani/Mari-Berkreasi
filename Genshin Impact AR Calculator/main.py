# Tools Sederhana Untuk Menghitung Berapa AR EXP yang dibutuhkan & Perkiraan Harinya untuk sampai ke AR Sekian

# Konstanta
EXP_Per_20_Resin = 100
Bonus_Commision = 500 # Didapatkan jika menyelesaikan 4 daily komisi

def hitung_AR() :
    pass

def hitung_perkiraan_hari() :
    pass

def main() :
    # Input Data Player (AR Sekarang & AR EXP Sekarang)
    AR_Sekarang = int(input("Masukkan AR Sekarang : "))
    AR_EXP_Sekarang = int(input("Masukkan AR EXP Sekarang : "))

    # Input Target AR (mau ke AR berapa)
    Target_AR = int(input("Masukkan Target AR : "))
    print()

    # Input Progress Daily Player
    Commision = int(input("Masukkan Daily Commision yang sudah dikerjakan : "))
    Resin = int(input("Masukkan Jumlah Resin yang sudah dihabiskan : "))
    print("---------------------------------------------------")

    # Output Hasil Perhitungan
    print(f"Kamu Butuh sekian AR EXP untuk mencapai Target AR-mu")
    print(f"Kamu Butuh kira-kira sekian hari untuk mencapai Target AR mu")

if __name__ == "__main__" :
    main()