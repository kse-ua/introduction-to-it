
# Напишіть програму для роботи з банківськими аккаунтами. З підтримкою команд
# додавання грошей на рахунок та зняття. Кожен рахунок має кредитний ліміт.
# Ведіть статистику, скільки сумарно грошей користувач додавав на рахунок

class BankAccount:
    def __init__(self, currency_name: str, amount: int, limit: int):
        self.currency_name = currency_name
        self.amount = amount
        self.limit = limit
        self.total_deposit = amount

    def add_to(self, value: int):
        self.total_deposit += value
        self.amount += value

    def can_withdraw(self, value: int):
        return value <= amount + self.limit

    def withdraw(self, value: int):
        self.amount -= value

    def __str__(self):
        return f"amount of {self.currency_name}: {self.amount}; total: {self.total_deposit}"


bank_accounts = {
    "UAH": BankAccount("UAH", 100, 10000),
    "EURO": BankAccount("EURO", 100, 200),
}

print(bank_accounts["UAH"])

while True:
    commands = input("Next command: ").split(" ")
    command = commands[0]
    currency = commands[1]
    amount = int(commands[2])
    account = bank_accounts[currency]

    if command == "add":
        account.add_to(amount)
    elif command == "withdraw":
        if account.can_withdraw(amount):
            account.withdraw(amount)
        else:
            print("Sorry, you've run out of money :(")
    print(bank_accounts)

