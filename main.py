from os import system
import pandas as pd
from csv import writer
from time import sleep
from random import shuffle

# csv file name
filename = "./data.csv"
delay = 1

class Card:
    suit = 0
    num = 0
    value = 0
    def __init__(self, num, suit):
        self.suit = suit
        if num < 10:
            self.num = num
            self.value = num
        else:
            self.num = num
            self.value = 10
    def getValue(self): return self.value
    def getNum(self): return self.num
    def display(self):
        typeSuit = ["", "CO", "RO", "CHUONG", "BICH"]
        typeNum = ["","XI (A)", "HAI (2)", "BA (3)", "BON (4)", "NAM (5)", "SAU (6)", 
        "BAY (7)", "TAM (8)", "CHIN (9)", "MUOI (10)", "BOI (J)", "DAM (Q)", "GIA (K)"]
        print(f'{typeNum[self.num]} {typeSuit[self.suit]}.')
#global variable
username = ""
password = ""
coins = 0
debt = 0
dangxuat = ""

#game variables
win = 0
bet = 0
lent = 0
denbai = False
baseDeck = []
for i in range(52): 
    baseDeck.append(Card(i // 4 + 1, i % 4 + 1))

#row_num: the index number of current account
row_num = -1

def tinhdiem(v):
    res = 0
    if len(v) >= 4:
        for i in range(len(v)):
            res += v[i].getValue()
    elif len(v) == 2:
        if v[0].getNum() == 1 or v[1].getNum == 1:
            res = v[0].getValue() + v[1].getValue() + 10
        else:
            res = v[0].getValue() + v[1].getValue()
    else:
        res += v[0].getValue() + v[1].getValue() + v[2].getValue()
        if v[0].getNum() == 1 or v[1].getNum() == 1 or v[2].getNum() == 1:
            if res <= 11: res += 10
            elif res == 12: res = 21
            else: res += 0
    return res

def yourCardInHand(v):
    print("Ban dang co:\n")
    for i in range(len(v)): 
        print(f'-- {i+1}: ', end = "") 
        v[i].display()
    print("")
def botCardInHand(v):
    print("Doi thu cua ban co:\n")
    for i in range(len(v)): 
        print(f'-- {i+1}: ', end = "") 
        v[i].display()
    print("")
    
def xidach(v):
    if len(v) > 2: return False
    if v[0].getValue() == 1 and v[1].getValue() == 10: return True
    if v[1].getValue() == 1 and v[0].getValue() == 10: return True
    return False

def xivang(v):
    if len(v) == 2 and v[0].getValue() == 1 and v[1].getValue() == 1: return True
    return False

def ngulinh(v):
    if len(v) == 5 and (v[0].getValue() + v[1].getValue() + v[2].getValue() + v[3].getValue() + v[4].getValue() <= 21): return True
    return False

def quac(v):
    sum = tinhdiem(v)
    if sum > 21: return True
    return False

def non(v):
    sum = tinhdiem(v)
    if sum < 16: return True
    return False

def dutuoi(v):
    sum = tinhdiem(v)
    if sum >= 16: return True
    return False

def showInfo():
    global username, coins, debt
    print(f'Chao {username}, ban dang co {coins} (coins) va no {debt} (coins).')

# BEGIN GAME
play = True

while play:
    system('cls')
    print('XIN CHAO!')
    sleep(delay*2)
    #login option
    login_type = input("LOGIN/REGISTER [L/R]: ")
    while login_type != 'r' and login_type != 'l' and login_type != 'R' and login_type != 'L':
        print("Vui long nhap lai!\n")
        login_type = input("LOGIN/REGISTER [L/R]: ")

    #login
    if login_type == 'l' or login_type == 'L': 
        system('cls')

        csvfile = pd.read_csv(filename)
        num_rows = csvfile.shape[0]

        access = False
        while not access: 
            username = input("Your username: ")
            password = input("Your password: ")

            for i in range(num_rows):
                row = csvfile.iloc[i]
                if str(row[0]) == username and str(row[1]) == password:
                    coins = row['no_of_coins']
                    debt = row['debt']   
                    system('cls')
                    row_num = i
                    print("Access granted!\n\nYour information:")
                    row.pop('password')
                    print(row.to_string())
                    access = True
                    break
            if not access: 
                system('cls')
                print("Wrong username or password! Please try again!")
    #regis
    else: 
        system('cls')

        username = input("Your username: ")
        
        repeat = True
        csvfile = pd.read_csv(filename)
        num_rows = csvfile.shape[0]
        
        while repeat: 
            for i in range(num_rows):
                row = csvfile.iloc[i]
                if row['name'] == username:
                    system('cls')
                    username = input("Your username has been taken. Please try another username: ")
            repeat = False


        password = input("Your password: ")
        coins = int(input("Your initial number of coins: "))
        while coins <= 0:
            coins = int(input("Invalid number of coins (above 0)! Your initial number of coins: "))
        info = [username, password, coins, debt]   

        with open(filename,'a') as fd:
            writer(fd).writerow(info)
            system('cls')

        csvfile = pd.read_csv(filename)
        num_rows = csvfile.shape[0]
        print("Account created. Please login again!")
        access = False
        while not access: 
            username = input("Your username: ")
            password = input("Your password: ")

            for i in range(num_rows):
                row = csvfile.iloc[i]
                if str(row['name']) == username and str(row['password']) == password:
                    coins = row['no_of_coins']
                    debt = row['debt']   
                    system('cls')
                    row_num = i
                    print("Access granted!\n\nYour information:")
                    row.pop('password')
                    print(row.to_string())
                    access = True
                    break
            if not access: 
                system('cls')
                print("Wrong username or password! Please try again!")
    
    sleep(delay/10)
    
    while True:
        csvfile = pd.read_csv(filename)
        info = csvfile.iloc[row_num]
        system('cls')
        showInfo()
        dangxuat = input("Dang xuat? [Y/N] ")
        if (dangxuat == 'Y' or dangxuat == 'y'): break
        if coins == 0: 
            lent = int(input("Ban dang co 0 (coins). Nhap so tien ban muon vay them: "))
            coins += lent
            debt += lent
        bet = int(input("-- Ban muon cuoc bao nhieu: "))
        while bet > coins: 
            print("-- Ban khong du tien de cuoc. Vui long nhap lai!")
            bet = int(input("-- Ban muon cuoc bao nhieu: "))
        
        print("-- Dang phat bai --") 
        sleep(delay*1.5)

        playDeck = baseDeck
        shuffle(playDeck)

        system('cls')
        showInfo()

        # lordDeck = [playDeck[48], playDeck[50]]
        # playerDeck = [playDeck[51], playDeck[49]]
        lordDeck = []
        playerDeck = []
        playerDeck.append(playDeck[-1])
        playDeck.pop()
        lordDeck.append(playDeck[-1])
        playDeck.pop()
        playerDeck.append(playDeck[-1])
        playDeck.pop()
        lordDeck.append(playDeck[-1])
        playDeck.pop()
        yourCardInHand(playerDeck)

        if xivang(playerDeck): 
            if xivang(lordDeck): win = 0
            else: 
                win = 1
                bet *= 2
        elif xidach(playerDeck):
            if xivang(lordDeck): win = -1
            elif xidach(lordDeck): win = 0
            else: win = 1
        elif xivang(lordDeck) or xidach(lordDeck): win = -1
        else:
            boctiep = input("-- Nhap \"Y\" hoac \"y\" de tiep tuc boc bai,\nhoac nhap phim bat ky khac de dung lai: ")
            while len(playerDeck) < 5 and (boctiep == 'y' or boctiep == 'Y'):
                playerDeck.append(playDeck[-1])
                playDeck.pop()
                system('cls')
                showInfo()
                yourCardInHand(playerDeck)
                if len(playerDeck) == 5 or quac(playerDeck):
                    if tinhdiem(playerDeck) >= 28:
                        denbai = True
                        bet *= 2
                    print("-- Ban khong the tiep tuc boc bai!\n")
                    break
                boctiep = input("-- Nhap \"Y\" hoac \"y\" de tiep tuc boc bai,\nhoac nhap phim bat ky khac de dung lai: ")

            print("\n-- Cho doi thu cua ban --") 
            
            while True:
                if dutuoi(lordDeck): break
                elif len(lordDeck) < 5:
                    lordDeck.append(playDeck[-1])
                    playDeck.pop()
                else: break

            if ngulinh(playerDeck): 
                if ngulinh(lordDeck): win = 0
                else: win = 1
            elif dutuoi(playerDeck) and not quac(playerDeck):
                if ngulinh(lordDeck): win = -1
                elif not quac(lordDeck):
                    if tinhdiem(playerDeck) == tinhdiem(lordDeck): win = 0
                    elif tinhdiem(playerDeck) < tinhdiem(lordDeck): win = -1
                    else: win = 1
                else: win = 1
            else:
                if quac(lordDeck): win = 0
                else: win = -1

        botCardInHand(lordDeck)
        if win == 1:
            print("KET QUA: THANG")
            coins += bet
        elif win == -1:
            print("KET QUA: THUA")
            coins -= bet
        else:
            print("KET QUA: HOA")
        temp = input("Bam phim bat ki de tiep tuc.")

    if coins > debt:
        coins -= debt
        debt = 0
    df = pd.read_csv(filename)
    df.loc[row_num, 'no_of_coins'] = coins
    df.loc[row_num, 'debt'] = debt
    df.to_csv(filename, index = False)
    play = False
# END GAME

input('\nNhan phim bat ki de thoat! ')
