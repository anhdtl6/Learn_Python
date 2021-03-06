# OOP buổi 2
import os
import sys
import json

class Fraction:
    minimum_balance = 50000

    def __init__(self, nr, dr):
        self.nr = nr
        self.dr = dr
        
    @property
    def nr(self):
        return self._nr

    @property
    def dr(self):
        return self._dr

    @nr.setter
    def nr(self, nr):
        self._nr = nr
        
    @dr.setter
    def dr(self, dr):
        if dr == 0:
            raise ValueError("Dr không hợp lệ, Dr phải khác 0")
        elif dr < 0:
            dr = abs(dr)
            self.nr = -self.nr
        self._dr = dr

    def display(self):
        if self.nr == 0: 
            print(0)
        elif self.dr == 1:
            print(self.nr)
        else:
            print(f"{self.nr}/{self.dr}")

    def hcf(self):
        x, y = abs(self.nr), abs(self.dr)
        hcf = x if x < y else y

        while hcf > 0:
            if x % hcf == 0 and y % hcf == 0:
                break

            hcf -= 1

        return hcf if hcf > 0 else None


    def reduce(self):
        n = self.hcf()

        if n:
            self.nr = int(self.nr / n)
            self.dr = int(self.dr / n)

fr = Fraction(2, -6)
fr.display()
fr.reduce()
fr.display()




# OOP buổi 3

class BankAccount:
    def __init__(self, account_number, owner , balance=0):
        self._account_number = account_number
        self._owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number    

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(
            f"Số tài khoản {self.account_number}\nThông tin KH: {self._owner.get_info()}\nSố dư: {self.balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance - BankAccount.minimum_balance:
            self.balance -= amount
        else:
            raise ValueError(
                f"Số tiền phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền phải lớn hơn 0")  


class SavingAccount(BankAccount):
    monthly_interest_rate = 0.005
   
    def calculate_interest(self):
        return self.monthly_interest_rate*self.balance

class Customer:
    def __init__(self, name, date_of_birth, email, phone):
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone

    def get_info(self):
        return f"{self.name}, {self.date_of_birth}, {self.email}, {self.phone}"    

cus = Customer("Do Thi Lan Anh","29/12/1991","lananhtk8@gmail.com","0969020292")
bank_account = SavingAccount("100023300000", cus, 8000000) 
bank_account.display() 
print(f"Lãi: {bank_account.calculate_interest()}")