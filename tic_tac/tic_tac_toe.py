class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""
    
    def choose_name(self):
        while True:
            name = input("Enter your Name and Fight: ")
            if not name.isalpha():
                raise ValueError(f"{name} not valid, Only alphabetic characters allowed! Please try again.")
            else:
                self.name=name
                print(f"{name}, you are a fighter now!")
                break
    def choose_symbol(self):
        while True:
            symbol = input("Choose Your Weapon now (X or O): ").upper()
            if symbol not in ["X", "O"]:
                raise ValueError(f"{symbol} is not an accepted value! Please try again.")
            else:
                self.symbol = symbol  
                print("You can start the fight now, hero!")
                break

player1 = Player()   
player1.choose_name()
player1.choose_symbol()