class Bank:
    def __init__(self, name, age, money, key):
        self._name = name
        self._age = age
        self.__money = money
        self.__key = key

    # Геттер для name
    @property
    def name(self):
        return self._name

    # Сеттер для name
    @name.setter
    def name(self, name):
        self._name = name

class EnhancedBank(Bank):
    def __init__(self, name, age, money, key):
        super().__init__(name, age, money, key)

    # Геттер и сеттер для age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise ValueError("Возраст не может быть отрицательным")

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        raise AttributeError("Для изменения баланса используйте set_money с ключом")

    def set_money(self, money, key):
        if key == self._Bank__key:
            self._Bank__money = money
        else:
            raise ValueError("Неверный ключ доступа")

    @property
    def key(self):
        raise AttributeError("Прямой доступ к ключу запрещен")

    @key.setter
    def key(self, value):
        raise AttributeError("Изменение ключа запрещено")

account = EnhancedBank("Иван", 30, 1000, "secret_key")
print(account.name)  # Иван
print(account.age)   # 30

account.name = "Петр"
account.age = 35

print(account.name)  # Петр
print(account.age)   # 35

try:
    account.money = 2000
except AttributeError as e:
    print(e)

try:
    account.set_money(2000, "secret_key")
    print(account.money)  # 2000
except ValueError as e:
    print(e)

try:
    print(account.key)
except AttributeError as e:
    print(e)

try:
    account.key = "new_key"
except AttributeError as e:
    print(e)
