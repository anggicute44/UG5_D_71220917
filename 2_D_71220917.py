def hitung_mobil():
    jumlahSol = 0
    jumlahSur = 0
    jumlahJog = 0
    jumlahMag = 0
    
    while True:
        asal = input("Masukkan asal mobil (ketik 'done'untuk keluar)")
        if asal == 'done':
            break
        if asal == 'done':
            break
        elif asal == 'Solo':
            jumlahSol += 1
        elif asal == 'Surabaya':
            jumlahSur += 1
        elif asal == 'Jogja':
            jumlahJog += 1
        elif asal == 'Magelang':
            jumlahMag += 1
        else:
            print("mobil tidak ada")
    
    print("Jumlah mobil dari Solo: ", jumlahSol)
    print("Jumlah mobil dari Surabaya: ", jumlahSur)
    print("Jumlah mobil dari Jogja: ", jumlahJog)
    print("Jumlah mobil dari Magelang: ", jumlahMag)