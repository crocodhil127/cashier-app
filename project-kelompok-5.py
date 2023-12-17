import os,time 
BG_RED = '\033[101m'
BG_GREEN = '\033[102m'
BG_CYAN = '\033[106m'
RESET = '\033[0m'

def namaBarang(data):
    with open('namaBarang.txt','w') as file:
        for i in data : 
            file.write(f'{i[0]},{i[1]}\n')

def loadBarang():
    try:
        with open('namaBarang.txt', 'r') as file:
            baca = file.readlines()
            return [lines.strip().split(",") for lines in baca]
    except:
        return []

barang = loadBarang()

def tampilkan_tabel(items):
    print('+' + '-' * 4 + '+' + '-' * 14 + '+' + '-' * 14 + '+')
    print('|' + 'ID  ' + '|' + ' Nama Barang'.ljust(14) + '|' + 'Harga'.center(14) + '|')
    print('+' + '-' * 4 + '+' + '-' * 14 + '+' + '-' * 14 + '+')
    id_counter = 0
    for i in items:
        id_counter += 1 
        print(f'| {str(id_counter).center(2)} |  {i[0].ljust(11)} |  Rp.{str(i[1]).ljust(9)}|')


def admin(items):
    try:
        while True:
            print(BG_CYAN + 'Selamat Datang Admin!' + RESET)
            print('1. Tambah Menu')
            print('2. Hapus Menu')
            inp = input('Masukkan pilihan anda (0 untuk berhenti) : ')

            if inp == '0':
                tampilkan_tabel(items)
                break
            elif inp == '1':
                addMenu(items)
            elif inp == '2':
                deleteMenu(items)
            else:
                print("masukkan inputan yang benar!!")

    except ValueError:
        print('Mohon masukkan Input yang Benar!')


def addMenu(items):
    namaMenu = input('Masukkan Nama Menu Baru : ')
    hargaMenu = int(input('Masukkan Harga Menu : '))
    barangBaru = [namaMenu, hargaMenu]
    items.append(barangBaru)
    namaBarang(items)


def deleteMenu(items):
    tampilkan_tabel(items)
    choice = input('Masukkan ID Yang Ingin dihapus : ')
    if int(choice) > len(items):
        print("masukkan ID yang benar!")
        time.sleep(2)
        os.system('cls')
        deleteMenu(items)
    elif int(choice) <= 0: 
        print("masukkan ID yang benar!!")
        deleteMenu(items)
    else:
        items.pop(int(choice) - 1)
        namaBarang(items)
        # namaBarang(items)
    # index = -1
    
    # for i in range(0, len(items)):
    #     menu = items[i]
    #     if choice.lower() == menu['namaItem'].lower():
    #         index = i
    #         break

    # if index == -1:
    #     print(BG_RED + 'Menu yang anda pilih tidak ditemukan !' + RESET)
    # else:
    #     del items[index]
    #     print(BG_GREEN + 'Menu yang anda pilih berhasil dihapus' + RESET)

def namaBarang(data):
    with open('namaBarang.txt','w') as file:
        for i in data : 
            file.write(f'{i[0]}, {i[1]}\n')

def loadBarang():
    try:
        with open('namaBarang.txt', 'r') as file:
            baca = file.readlines()
            return [lines.strip().split(",") for lines in baca]
    except:
        return []

barang = loadBarang()




while True:
    finalTotal = 0
    tampilkan_tabel(barang)
    cart = []

    while True:
        try:
            inp = int(input('Pilih ID barang yang ingin anda beli (99 untuk menu admin): '))
            if inp == 0:
                break
            elif inp == 99:
                admin(barang)
            elif inp < 0 or inp > len(barang):
                print('ID barang tidak valid.')
            else:
                jumlah = int(input('Jumlah barang yang ingin anda beli: '))
                if jumlah <= 0:
                    print('Jumlah harus lebih dari 0.')
                else:
                    item = barang[inp - 1]
                    total = int(item[1]) * int(jumlah)
                    finalTotal += total
                    cart.append({'namaItem': item[0], 'jumlah': jumlah, 'total': total})
                    print(f'Anda memasukkan {item[0]} sebanyak {jumlah}')
                    lagi = input("lanjut belanja? (y/n): ")
                    if lagi == "y":
                        continue
                    elif lagi == "n":
                        os.system('cls')
                        break
                    else: 
                        print("masukkan input yang benar!")

        except ValueError:
            print('Masukkan angka yang valid.')


    if len(cart) == 0:
        print('mohon pilih id yg sesuai')
    else:
        print('+' + '-' * 4 + '+' + '-' * 14 + '+' + '-' * 14 + '+' + '-' * 14 + '+')
        print('|' + 'ID  ' + '|' + ' Nama Barang'.ljust(14) + '|' + 'Jumlah'.center(14) + '|' + 'Harga'.center(14) + '|')
        print('+' + '-' * 4 + '+' + '-' * 14 + '+' + '-' * 14 + '+' + '-' * 14 + '+')

        id_counter = 1

        for item in cart:
            nama_item = item['namaItem']
            total = item['total']
            jumlah = item['jumlah']

            print(f'| {str(id_counter).center(2)} |  {nama_item.ljust(11)} |  {str(jumlah).center(12)}| Rp.{str(total).center(9)} |')
            id_counter += 1

        print('+' + '-' * 4 + '+' + '-' * 14 + '+' + '-' * 14 + '+' + '-' * 14 + '+')

        print(f'Nominal yang harus anda bayar : Rp.{finalTotal}')
        cek = True
        while cek: 
            try:
                uang = int(input("masukkan nominal yang ingin anda bayarkan: ")) 
                if uang < finalTotal: 
                    print("uang anda tidak cukup")
                elif uang >= finalTotal:
                    break
            except ValueError:
                print("nominal yang anda masukkan tidak boleh kosong!")
                uang = int(input("masukkan nominal yang ingin anda bayarkan: ")) 
                if uang < finalTotal: 
                    print("uang anda tidak cukup")
                elif uang >= finalTotal:
                    break
        print(f"berikut kembalian anda {uang - finalTotal}")
        print("terima kasih telah berbelanja!!")
        break
                # print(f'Berikut kembalian anda {finalTotal - uang}')
        # except ValueError: 
        #         print("Nominal yang dimasukkan tidak boleh kosong!")
        #         uang = int(input('Masukkan Nominal bayar anda: '))
        #         kembalian = int(uang) - finalTotal
                
        # if kembalian >= 0:
        #     print(f'Kembalian: Rp.{kembalian}')
        #     print("Terima kasih Telah berbelanja!")
        #     break
        # else:
        #     print('Uang anda kurang!')
            # uang = int(input('Masukkan Nominal bayar anda: '))
            # print("Maaf harap kembali saat uang anda telah cukup!")
            # break


