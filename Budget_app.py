class Budget:

    def __init__(self, category):
        self.category = category
        self.amount = 0


    def check_balance(self, amount):
        if self.amount < amount:
            return False
        else:
            return True

    def deposit(self, amount):
        self.amount += amount
        return "You deposited {} into the budget".format(self.amount)


    def withdraw(self, amount):
        if self.check_balance(amount) == True:
            self.amount -= amount
            return "You withdraw {} from the budget".format(amount)
        else:
            return "You do not have enough balance to perform this withdrawal"

    
    def budget_balance(self):
        return self.amount

    
    def transfer(self, amount, category):
        if self.check_balance(amount) == True:
            self.amount -= amount
            category.amount += amount
            return "You have tranferred {} to {}".format(amount, category.category)
        else:
            return "You do not have enough balance to perform this transfer"
    


#perform deposit
food = Budget("food")
food.deposit(1000)
print("Food budget balance: #{}".format(food.budget_balance()))

clothing = Budget("clothing")
clothing.deposit(500)
print("Clothing budget balance: #{}".format(clothing.budget_balance()))         

entertainment = Budget("entertainment")
entertainment.deposit(2500)
print("Entertainment budget balance: {}".format(entertainment.budget_balance()))

#perform withdrawal
food.withdraw(200)
print("Food budget balance: #{} after performing withdrawal".format(food.budget_balance()))

print(food.transfer(100, clothing))
print("Food budget balance: #{} and Clothing budget balance: #{} after performing transfer".format(food.budget_balance(),
                                                                                                clothing.budget_balance()))
