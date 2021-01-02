class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def log(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.money} of money')

    def change_supplies(self, coffee_type):
        print('I have enough resources, making you a coffee!')
        if coffee_type == '1':
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
        if coffee_type == '2':
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
        if coffee_type == '3':
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6

    def not_enough_supplies(self, coffee_type):
        if coffee_type == '1':
            if self.water < 250:
                print('Sorry, not enough water!')
            elif self.beans < 16:
                print('Sorry, not enough beans!')
            else:
                print('Sorry, not enough cups!')
        if coffee_type == '2':
            if self.water < 350:
                print('Sorry, not enough water!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.beans < 16:
                print('Sorry, not enough beans!')
            else:
                print('Sorry, not enough cups!')
        if coffee_type == '3':
            if self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.beans < 12:
                print('Sorry, not enough beans!')
            else:
                print('Sorry, not enough cups!')

    def buy_coffee(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        coffee_choice = input()
        if coffee_choice == '1':
            # water=250, beans=16, money=4, cups=1
            supplies = [self.water >= 250, self.beans >= 16, self.cups >= 1]
            if all(supplies):
                self.change_supplies(coffee_choice)
            else:
                self.not_enough_supplies(coffee_choice)
        if coffee_choice == '2':
            # water=350, milk=75, beans=20, money=7, cups=1
            supplies = [self.water >= 350, self.milk >= 75, self.beans >= 20, self.cups >= 1]
            if all(supplies):
                self.change_supplies(coffee_choice)
            else:
                self.not_enough_supplies(coffee_choice)
        if coffee_choice == '3':
            # water=200, milk=100, beans=12, money=6, cups=1
            supplies = [self.water >= 200, self.milk >= 100, self.beans >= 12, self.cups >= 1]
            if all(supplies):
                self.change_supplies(coffee_choice)
            else:
                self.not_enough_supplies(coffee_choice)
        if coffee_choice == 'back':
            pass

    def take_money(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def fill_supplies(self):
        print('Write how many ml of water do you want to add:')
        water_ml = int(input())
        self.water += water_ml
        print('Write how many ml of milk do you want to add:')
        milk_ml = int(input())
        self.milk += milk_ml
        print('Write how many grams of coffee beans do you want to add:')
        beans_gr = int(input())
        self.beans += beans_gr
        print('Write how many disposable cups of coffee do you want to add:')
        cups_number = int(input())
        self.cups += cups_number


coffee_machine = CoffeeMachine()
while True:
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()
    if action == 'buy':
        print()
        coffee_machine.buy_coffee()
        print()
    if action == 'fill':
        print()
        coffee_machine.fill_supplies()
        print()
    if action == 'take':
        print()
        coffee_machine.take_money()
        print()
    if action == 'remaining':
        print()
        coffee_machine.log()
        print()
    if action == 'exit':
        break
