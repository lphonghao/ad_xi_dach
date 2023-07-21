

username = ""
password = ""
coins = 0
debt = 0

def login(filename):

def regis(filename):  

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

    