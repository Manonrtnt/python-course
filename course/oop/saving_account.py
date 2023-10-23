from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name: str = 'John', balance: float = 1000, interest_rate: float = 0.003) -> None:
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def set_rate(self, value: float) -> None:
        self.interest_rate = value

    def capitalization(self, month_count: int) -> float:
        for _ in range(month_count):
            self.balance += self.balance * self.interest_rate
        return self.balance

# Exemple d'utilisation
account1 = SavingsAccount("Alice", 2000, 0.003)  # Taux d'intérêt mensuel de 0,3%
account2 = SavingsAccount("Bob", 3000, 0.004)    # Taux d'intérêt mensuel de 0,4%

print("Avant capitalisation :")
print(account1)
print(account2)

account1.set_rate(0.004)  # Modification du taux d'intérêt mensuel
account2.set_rate(0.005)

account1.capitalization(12)  # Capitalisation des intérêts composés pendant 12 mois
account2.capitalization(6)

print("\nAprès capitalisation :")
print(account1)
print(account2)