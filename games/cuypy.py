import random
import main

def start():
    while True:
        cuypy_position = random.randint(1, 4)
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4
        goa = goa_kosong.copy()
        goa[cuypy_position - 1] = "|0_0|"

        while True:
            try:
                pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))
                if pilihan_user < 1 or pilihan_user > 4:
                    print("Masukkan nomor yang valid (1, 2, 3, atau 4)!")
                    continue
                break
            except ValueError:
                print("Masukkan hanya nomor yang valid dan bukan angka (1, 2, 3, atau 4)!")

        if pilihan_user == cuypy_position:
            print(f'{" ".join(goa)} \nSelamat! Kamu menang! Posisi CUYPY ada di goa nomor {cuypy_position} dan pilihanmu adalah {pilihan_user}!')
        else:
            print(f'{" ".join(goa)} \nKamu kalah! CUYPY tidak berada di situ. Ternyata CUYPY ada di goa nomor {cuypy_position}. Sedangkan kamu memilih goa nomor {pilihan_user}.')

        play_again = input("\nApakah ingin memainkan permainan lagi? [y/n]: ").lower()
        if play_again == "n":
            main.menu()
        
if __name__ == '__main__':
    start()
