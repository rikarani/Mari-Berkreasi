# Tools Sederhana Untuk Menghitung Berapa AR EXP yang dibutuhkan & Perkiraan Harinya untuk sampai ke AR Sekian

# Konstanta
EXP_Per_Commision = 250
EXP_Per_20_Resin = 100
Bonus_Commision = 500 # Didapatkan jika menyelesaikan 4 daily komisi

def hitung_AR(AR_Sekarang, AR_EXP_Sekarang, Target_AR) :
    # Tabel AR EXP
    AR_EXP = {
    1 : 0,          21 : 30950,     41 : 155950,
    2 : 375,        22 : 34375,     42 : 167475,
    3 : 875,        23 : 38100,     43 : 179950,
    4 : 1500,       24 : 42100,     44 : 193400,
    5 : 2225,       25 : 46400,     45 : 207800,
    6 : 3075,       26 : 50975,     46 : 223150,
    7 : 4025,       27 : 55850,     47 : 239475,
    8 : 5100,       28 : 61000,     48 : 256750,
    9 : 6300,       29 : 66450,     49 : 275000,
    10 : 7600,      30 : 72175,     50 : 294200,
    11 : 9025,      31 : 78200,     51 : 320600,
    12 : 10550,     32 : 84500,     52 : 349400,
    13 : 12200,     33 : 91100,     53 : 380600,
    14 : 13975,     34 : 98000,     54 : 414200,
    15 : 15850,     35 : 105175,    55 : 450200,
    16 : 17850,     36 : 112650,    56 : 682550,
    17 : 20225,     37 : 120400,    57 : 941500,
    18 : 22725,     38 : 128450,    58 : 1227250,
    19 : 25350,     39 : 136775,    59 : 1540075,
    20 : 28125,     40 : 145400,    60 : 1880200
    }

    AR_EXP_yang_dibutuhkan = (AR_EXP[Target_AR] - AR_EXP[AR_Sekarang]) - AR_EXP_Sekarang

    return AR_EXP_yang_dibutuhkan

def hitung_EXP_Per_Hari(Commision, Resin) :
    # Nilai EXP per Commision bisa disesuaikan di bagian Konstanta
    if Commision >= 4 :
        AR_EXP_per_hari = (EXP_Per_Commision * 4) + Bonus_Commision + (EXP_Per_20_Resin * (Resin // 20))
    else :
        AR_EXP_per_hari = (EXP_Per_Commision * Commision) + (EXP_Per_20_Resin * (Resin // 20))

    return AR_EXP_per_hari

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
    # Output Hasil Hitung AR EXP
    if hitung_AR(AR_Sekarang, AR_EXP_Sekarang, Target_AR) < 0 :
        print("Input Terbalik, Tidak bisa menghitung dari AR Tinggi ke AR Rendah")
    else :
        print(f"Kamu Butuh {hitung_AR(AR_Sekarang, AR_EXP_Sekarang, Target_AR)} AR EXP untuk mencapai AR {Target_AR}")
    
    # Output Hasil Hitung Perkiraan Hari
    print(f"Butuh kira-kira {hitung_AR(AR_Sekarang, AR_EXP_Sekarang, Target_AR) // hitung_EXP_Per_Hari(Commision, Resin)} Hari untuk mencapai AR {Target_AR}")

if __name__ == "__main__" :
    main()