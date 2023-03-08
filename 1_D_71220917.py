def ganti_kata(kalimat, cari, ganti):
    wwww = kalimat.split()
    for i in range(len(wwww)):
        if wwww[i] == cari:
            wwww[i] = ganti
    kalimat_baru = ' '.join(wwww)
    return kalimat_baru



aaaa=(input("masukkan kalimat :"))
bbbb=(input("kata yang dicari :"))
cccc=(input("kata yang diganti :"))

dddd=ganti_kata(aaaa, bbbb, cccc)
print("kalimat baru",dddd)

