import numpy as np

def dajVektoreOdKorisnika():
    brojVektora = int(input("Koliko vektora zelite unijeti? :"))
    vektori = np.empty((brojVektora,3), float)
    for i in range (0, brojVektora):
        print("Unos %i. vektora:\n"% (i+1))
        for j in range(0,3):
            el = float(input("\tUnesite element %i: "% (j+1) ))
            vektori[i][j] = el
    return vektori

def provjeriOrtogonalnost(matrica):
    produkt = np.dot(matrica, matrica.T)
    np.fill_diagonal(produkt, 0)
    if(produkt.any() != 0):
        return 0
    return 1

vektori = np.array([[2,5,2],[1,1,4]])
print (vektori)
print("\t",provjeriOrtogonalnost(vektori),"\n")

vektori = np.array([[1,1,1],[1,1,1]])
print (vektori)
print("\t",provjeriOrtogonalnost(vektori),"\n")

vektori = np.array([[1,0,0],[0,1,0],[0,0,1]])
print (vektori)
print("\t",provjeriOrtogonalnost(vektori),"\n")

vektori = dajVektoreOdKorisnika()
print (vektori)
print("\t",provjeriOrtogonalnost(vektori),"\n")

