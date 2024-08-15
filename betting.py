#Nên cài các thư viện trên để chạy code
from pyfiglet import figlet_format as ff
from colorama import init, Fore, Style
import random

init()
ascii_art = ff("B e t t i n g", font="standard")
print(Fore.RED + ascii_art + Style.RESET_ALL)

lua_chon_hop_le = ["chẵn", "lẻ"]
lua_chon_dung = ["1", "2", "3", "4"]

def menu():
    print(Fore.YELLOW + "==============================")
    print("1: ĐẶT CƯỢC")
    print("2: TỈ LỆ")
    print("3: SỐ TIỀN HIỆN TẠI")
    print("4: THOÁT")
    print(Fore.YELLOW + "==============================" + Style.RESET_ALL)

def main():
    tien = 1000
    while True:
        menu()
        a = input("Hãy nhập lựa chọn của bạn: ")
        if a not in lua_chon_dung:
            print("Hãy nhập lại")
            continue
        else:
            if a == "1":
                try:
                    tien_cuoc = int(input("Hãy nhập số tiền cược mà bạn mong muốn:"))
                except ValueError:
                    print("Số tiền cược không hợp lệ!")
                    continue
                
                if tien_cuoc > tien or tien_cuoc <= 0:
                    print("Số tiền cược không hợp lệ!")
                    continue
                
                print(f"Bạn cược {tien_cuoc}$")
                lua_chon = input("Hãy đoán số đó chẵn hay lẻ:").lower()
                
                if lua_chon not in lua_chon_hop_le:
                    print("Bạn nhập không hợp lệ!")
                    continue
                
                so = random.randint(0, 10)
                
                if so % 2 == 0:
                    dap_an = "chẵn"
                else:
                    dap_an = "lẻ"
                
                if lua_chon == dap_an:
                    print("CHÚC MỪNG! Bạn đã nhập đúng")
                    tien += tien_cuoc
                    print(f"Số tiền hiện tại tăng {tien_cuoc}$")
                else:
                    print("Bạn đã nhập sai. Số tiền sẽ bị trừ!")
                    tien -= tien_cuoc
                    print(f"Số tiền hiện tại giảm {tien_cuoc}$")
            
            elif a == "2":
                print("Tỉ lệ chẵn lẻ là 50:50")
            
            elif a == "3":
                print(f"Số tiền hiện tại của bạn là: {tien}$")
            
            elif a == "4":
                print("Cảm ơn bạn đã chơi! Hẹn gặp lại!")
                break

if __name__ == "__main__":
    main()
