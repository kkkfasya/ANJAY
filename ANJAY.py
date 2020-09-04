from time import sleep
from os import system

cyan    = '\033[36m'
yellow  = '\033[93m'
green   = '\033[92m'
pink    = '\033[95m'
red     = '\033[91m'



def modeAnjay():
    print("1.ANJAY UNLIMITED")
    print("2.ANJAY yang menggunakan hitungan")
    user = input("~~> ")
    if user == "1":
        system("clear")
        sleep(0.1)
        ANJAY()
    
    elif user == "2":
        system("clear")
        sleep(0.1)
        anjay()
    
    else:
        print("Salah bro pilih yang betoel lah")
        sleep(0.7)
        system("clear")
        warna()



def ANJAY():
    new_normal = "patuh protokol kesehatan"
    while new_normal != "tidak patuh":
        print("A")
        sleep(0.1)
        print("AN")
        sleep(0.1)
        print("ANJ")
        sleep(0.1)
        print("ANJA")
        sleep(0.1)
        print("ANJAY")
        sleep(0.1)
        print("ANJA")
        sleep(0.1)
        print("ANJ")
        sleep(0.1)
        print("AN")
        sleep(0.1)
        print("A")
        sleep(0.1)



def anjay():
    anjay = 0
    print("ingin berapa kali Anjay nya?")
    user = int(input("~~> "))
    while anjay <= user:
        print("A")
        sleep(0.1)
        anjay += 1
        print("AN")
        sleep(0.1)
        anjay += 1
        print("ANJ")
        sleep(0.1)
        anjay += 1
        print("ANJA")
        sleep(0.1)
        anjay += 1
        print("ANJAY")
        sleep(0.1)
        anjay += 1
        print("ANJA")
        sleep(0.1)
        anjay += 1
        print("ANJ")
        sleep(0.1)
        anjay += 1
        print("AN")
        sleep(0.1)
        anjay += 1



def warna():
    system("clear")
    print(15*"="+"Anjay"+15*"=")
    print("Pilih warna dulu broo")
    print("1.Cyan\r\n2.Yellow\r\n3.Pink\r\n4.Red\r\n5.Green")
    print("Semoga paham bahasa inggris ")
    user = str(input("~~> "))

    if user == "1":
        print(cyan+"Cyan")
        sleep(0.3)
        system("clear")
        modeAnjay()
        
    elif user == "2":
        print(yellow+"Kuning mode aktif")
        sleep(0.3)
        system("clear")
        modeAnjay()
        
    elif user == "3":
        print(pink+"Pilihan yang bagus xD")
        sleep(0.3)
        system("clear")
        modeAnjay()
        
    elif user == "4":
        print(red+"Merah tanda tak punya, masih gak paham? itu referensinya ke ideologi usang")
        sleep(1.1)
        system("clear")
        modeAnjay()
        
    elif user == "5":
        print(green+"Hijau brrr")
        sleep(0.3)
        system("clear")
        modeAnjay()
        
    else:
        print("Salah bro pilih yang betoel lah")
        sleep(0.7)
        system("clear")
        warna()
        
if __name__ == "__main__":
    warna()
    
else:
    pass