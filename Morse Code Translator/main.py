# Kamus Dari Huruf Alphabet ke Kode Morse
enkrip = {
	# Alphabet
    " " : "/", # Spasi
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",

	# Angka
	"1" : ".----",
	"2" : "..---",
	"3" : "...--",
	"4" : "....-",
	"5" : ".....",
	"6" : "-....",
	"7" : "--...",
	"8" : "---..",
	"9" : "----.",
	"0" : "-----"
}

# Kamus Dari Kode Morse ke Huruf Alphabet
dekrip = {key:value for value,key in enkrip.items()}

def main() :
    kalimat = input().upper()
    sandi = [] # List buat nyimpan hasil translate nya

    if kalimat.startswith(".") or kalimat.startswith("-") : # Kode Morse tuh kan awalnya kalo nda . ya -
        print("Ini Kode Morse")
    
    # Dari Huruf Alphabet ke Kode Morse
    else :
        for kata in kalimat : # Setiap Alphabet yang ada di variabel kalimat disimpan di variabel kata, trus diulang
            sandi.append(enkrip[kata])
        
        print("Kode Morse dari", kalimat , "Adalah" , " ".join(sandi))

if __name__ == "__main__" :
    main()