class Cashier:
    a = 0
    amount = 0
    receive = 0
    change = 0
    stock = [50, 50, 50]
    
    def foods(self):
            
        print("======= MINI SUPERMARKET =======")
            
        print("1. Meat      = RM 10")
        print("2. Vegetable = RM 5")
        print("3. Fruit     = RM 5")
        print("\n4. Make payment")
        print("5. View stock")
        print("6. Exit")
            
        while True:
                
            choice = input("Choose option: ")
                
            if choice == '1':
                quantity = int(input("Enter the quantity: "))
                self.amount = self.amount + 10 * quantity
                self.stock[0] = self.stock[0] - quantity
                
            elif choice == '2':
                quantity = int(input("Enter the quantity: "))
                self.amount = self.amount + 5 * quantity
                self.stock[1] = self.stock[1] - quantity
                
            elif choice == '3':
                quantity = int(input("Enter the quantity: "))
                self.amount = self.amount + 5 * quantity
                self.stock[2] = self.stock[2] - quantity
                
            elif choice == '4':
                print("Total amount: ", self.amount)
                if self.amount > 0:
                    receive = int(input("Cash received: "))
                    print("Change: ", receive - self.amount)
                    print("Thank you, come again!")
                    
            elif choice == '5':
                print("Stock balance\n")
                print("Meat: ", self.stock[0])
                print("Vegetable: ", self.stock[1])
                print("Fruit: ", self.stock[2])
                    
            elif choice == '6':
                #save_foods() # Save the records when user exits the program (?) 
                print("Exit")
                break
                    
            else:
                print("Invalid choice!")

    def save_foods(self):
        food_record = open("foods.txt", "w")
        food_record.write("Meat stock : " + str(self.stock[0]))
        food_record.write("\nVegetable stock : " + str(self.stock[1]))
        food_record.write("\nFruit stock : " + str(self.stock[2]))
        food_record.close()

def main():
    a = Cashier()
    a.foods()
    a.save_foods()
