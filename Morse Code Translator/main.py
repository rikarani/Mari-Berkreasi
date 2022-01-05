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
	"0" : "-----",

    # Tanda Baca
    "." : ".-.-.-",
    "," : "--..--",
    ":" : "---...",
    "-" : "-....-",
    "/" : "-..-.",
}

# Kamus Dari Kode Morse ke Huruf Alphabet
dekrip = {key:value for value,key in enkrip.items()}

def alphabet_ke_morse(kalimat) :
    '''
    Dari Alphabet ke Kode Morse

    Contoh Inputnya "nama saya erika" (tanpa tanda petik) \n
    Outputnya adalah -. .- -- .- / ... .- -.-- .- / . .-. .. -.- .-
    '''
    sandi = []

    for kata in kalimat :
        sandi.append(enkrip[kata])

    return " ".join(sandi)

def morse_ke_alphabet(kalimat) :
    '''
    Dari Kode Morse ke Alphabet

    Contoh Inputnya -. .- -- .- / ... .- -.-- .- / . .-. .. -.- .- \n
    Outputnya adalah "NAMA SAYA ERIKA" (tanpa tanda petik)
    '''
    sandi = []

    for kata in kalimat.split(" ") :
        sandi.append(dekrip[kata])

    return "".join(sandi)

def main() :
    kalimat = input("Masukkan Teks : ").upper()

    if kalimat.startswith(".") or kalimat.startswith("-") :
        print(morse_ke_alphabet(kalimat))
    else :
        print(alphabet_ke_morse(kalimat))

if __name__ == "__main__" :
    main()