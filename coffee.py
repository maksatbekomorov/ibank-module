class CoffeeMachine:
    def __init__ (self, water, milk, beans, disposable, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.disposable = disposable
        self.money = money
        self.status = 'None'

    def fill_in(self, in_water, in_milk, in_beabs, in_disposable):
        self.water += in_water
        self.milk += in_milk
        self.beans += in_beabs
        self.disposable += in_disposable

    def resources(self):
        print("\nThe coffee machine has:")
        print(self.water,"of water")
        print(self.milk,"of milk")
        print(self.beans,"of coffee beans")
        print(self.disposable,"of disposable cups")
        print('$'+ str(self.money),"of money")

    def make_coffee(self, what_you_want):
        if what_you_want == '1':
            if self.water - 250 > 0:
                if self.beans - 16 > 0:
                    if self.disposable - 1 > 0:
                        print("I have enough resources, making you a coffee!")
                        self.money += 4
                        self.water -= 250
                        self.beans -= 16
                        self.disposable -= 1
                        self.status = 'None'
                        print("\nWrite action (buy, fill, take, remaining, exit):")
                    else:
                        print("Sorry, not enough disposable!")
                else:
                    print("Sorry, not enough beans!")
            else:
                print("Sorry, not enough water!")
        elif what_you_want == '2':
            if self.water - 350 > 0:
                if self.milk - 75 > 0:
                    if self.beans - 16 > 0:
                        if self.disposable - 1 > 0:
                            print("I have enough resources, making you a coffee!")
                            self.money += 7
                            self.water -= 350
                            self.milk -= 75
                            self.beans -= 20
                            self.disposable -= 1
                            self.status = 'None'
                            print("\nWrite action (buy, fill, take, remaining, exit):")
                        else:
                            print("Sorry, not enough disposable!")
                    else:
                        print("Sorry, not enough beans!")
                else:
                    print("Sorry, not enough milk!")
            else:
                print("Sorry, not enough water!")
        elif what_you_want == '3':
            if self.water - 200 > 0:
                if self.milk - 200 > 0:
                    if self.beans - 12 > 0:
                        if self.disposable - 1 > 0:
                            print("I have enough resources, making you a coffee!")
                            self.money += 6
                            self.water -= 200
                            self.milk -= 100
                            self.beans -= 12
                            self.disposable -= 1
                            self.status = 'None'
                            print("\nWrite action (buy, fill, take, remaining, exit):")
                        else:
                            print("Sorry, not enough disposable!")
                    else:
                        print("Sorry, not enough beans!")
                else:
                    print("Sorry, not enough milk!")
            else:
                print("Sorry, not enough water!")
        elif what_you_want == 'back':
            print("Go to main menu.")

coffee = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    print("\nWrite action (buy, fill, take, remaining, exit):")
    a = input()
    if a == 'buy':
        print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        coffee.make_coffee(input())
    elif a == 'fill':
        print("\nWrite how many ml of water do you want to add:")
        f_water = int(input())
        print("\nWrite how many ml of milk do you want to add:")
        f_milk = int(input())
        print("\nWrite how many grams of coffee beans do you want to add:")
        f_beabs = int(input())
        print("\nWrite how many disposable cups of coffee do you want to add:")
        f_disposable = int(input())
        coffee.fill_in(f_water, f_milk, f_beabs, f_disposable)
    elif a == 'take':
            print("\nI gave you $" + str(coffee.money))
            coffee.money -= coffee.money
    elif a == 'remaining':
            coffee.resources()
    else:
        break
