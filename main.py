import os
import pandas as pd
import csv
import core_game

# csv file name
filename = "data.csv"

#global variable
username = ""
password = ""
coins = 0
debt = 0

#login option
login_type = input("LOGIN/REGISTER [L/R]: ")
while login_type != 'r' and login_type != 'l' and login_type != 'R' and login_type != 'L':
    print("Please type again!\n")
    login_type = input("LOGIN/REGISTER [L/R]: ")

#login
if login_type == 'l' or login_type == 'L': 
    os.system('cls')

    csvfile = pd.read_csv(filename)
    num_rows = csvfile.shape[0]

    access = False
    while not access: 
        username = input("Your username: ")
        password = input("Your password: ")

        for i in range(num_rows):
            row = csvfile.iloc[i]
            if row['name'] == username and row['password'] == password:
                coins = row['no_of_coins']
                debt = row['debt']   
                os.system('cls')
                print("Access granted!\n\nYour information:")
                row.pop('password')
                print(row.to_string())
                access = True
                break
        if not access: 
            os.system('cls')
            print("Wrong username or password! Please try again!")

#regis
else: 
    os.system('cls')

    username = input("Your username: ")
    
    repeat = True
    csvfile = pd.read_csv(filename)
    num_rows = csvfile.shape[0]
    
    while repeat: 
        for i in range(num_rows):
            row = csvfile.iloc[i]
            if row['name'] == username:
                os.system('cls')
                username = input("Your username has been taken. Please try another username: ")
        repeat = False


    password = input("Your password: ")
    coins = int(input("Your initial number of coins: "))
    while coins <= 0:
        coins = int(input("Invalid number of coins (above 0)! Your initial number of coins: "))
    info = [username, password, coins, debt]   

    with open(filename,'a') as fd:
        csv.writer(fd).writerow(info)
        os.system('cls')

    csvfile = pd.read_csv(filename)
    num_rows = csvfile.shape[0]

    access = False
    while not access: 
        username = input("Your username: ")
        password = input("Your password: ")

        for i in range(num_rows):
            row = csvfile.iloc[i]
            if row['name'] == username and row['password'] == password:
                coins = row['no_of_coins']
                debt = row['debt']   
                os.system('cls')
                print("Access granted!\n\nYour information:")
                row.pop('password')
                print(row.to_string())
                access = True
                break
        if not access: 
            os.system('cls')
            print("Wrong username or password! Please try again!")
  


