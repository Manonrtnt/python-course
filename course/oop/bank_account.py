from typing import Self, Type

class BankAccount : 
    def __init__(self, name: str = 'John', balance:float = 1000) -> None:
        self.name = name
        self.balance = balance
    
    def deposit(self, amount: float) -> bool:
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount > self.balance :
            print("Vous n'avez pas assez de money money")
        else :
            self.balance -= amount
            # self.balance = self.balance - amount

    def transfer(self, destination_account: Type[Self], amount: float) :
        if amount > self.balance :
            print("Vous n'avez pas assez de money money")
        else :
            self.balance -= amount
            destination_account += amount

    def display(self) -> None :
        print(f"Account Holder: {self.name}\nBalance: {self.balance}")

    # Au lieu de la méthode display()
    # Permet afficher information sur l'objet
    def __str__(self) -> str :
        return f'{self.name} - {self.balance}'

account1 = BankAccount()
print(account1.name)
print(account1.balance)

# Exemple d'utilisation
account2 = BankAccount("Alice", 2000)
account2.display()

if account2.deposit(500):
    print("Deposit successful. New balance:", account2.balance)
else:
    print("Deposit failed. Balance remains unchanged.")

if account2.withdraw(1000):
    print("Withdrawal successful. New balance:", account2.balance)
else:
    print("Withdrawal failed. Balance remains unchanged.")