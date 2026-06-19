import os

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
 
    def get_balance(self): 
        return sum(item["amount"] for item in self.ledger) 

    def transfer(self, amount, category_instance):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_instance.name}")
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23].ljust(23)
            amt = f"{entry['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    spent_per_category = []
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent_per_category.append(spent)
    total_spent = sum(spent_per_category)
    
    percentages = []
    for spent in spent_per_category:
        if total_spent == 0:
            percentages.append(0)
        else:
            percentages.append(int((spent / total_spent) * 100 // 10) * 10)
            
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3d}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    max_len = max(len(category.name) for category in categories)
    padded_names = [category.name.ljust(max_len) for category in categories]
    
    for i in range(max_len):
        chart += "     "
        for name in padded_names:
            chart += name[i] + "  "
        
        if i < max_len - 1:
            chart += "\n"
            
    return chart



def clear_screen():
    """Wipes the terminal history clean depending on your Operating System."""
    
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Forces the system to wait so you can read outputs before clearing."""
    input("\nPress Enter to return to the Main Menu...")


def main():
    budget_categories = {}
    message = "Welcome to your Budget Tracker App!"

    while True:
        clear_screen()
        print("=== BUDGET APP ===")
        
        if message:
            print(f"\n📢 {message}")
            message = "" 
            
        print("\nAvailable Actions:")
        print("1. Create a Category")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. View Category Ledger (Receipt)")
        print("6. Display Spend Chart Graph")
        print("7. Exit")
        
        choice = input("\nChoose an option (1-7): ").strip()

        if choice == "1":
            clear_screen()
            print("=== CREATE CATEGORY ===")
            name = input("Enter new category name: ").strip().capitalize()
            if not name:
                message = "⚠️ Category name cannot be empty."
            elif name in budget_categories:
                message = f"⚠️ Category '{name}' already exists."
            else:
                budget_categories[name] = Category(name)
                message = f"✅ Category '{name}' successfully created!"

        elif choice in ["2", "3", "4", "5"]:
            if not budget_categories:
                message = "⚠️ Please create at least one category first."
                continue

            if choice == "2":
                clear_screen()
                print("=== DEPOSIT MONEY ===")
                print(f"Categories: {', '.join(budget_categories.keys())}\n")
                cat_name = input("Deposit to which category?: ").strip().capitalize()
                if cat_name in budget_categories:
                    try:
                        amt = float(input("Enter amount: $"))
                        desc = input("Description (optional): ").strip()
                        budget_categories[cat_name].deposit(amt, desc)
                        message = f"✅ Deposited ${amt:.2f} into {cat_name}."
                    except ValueError:
                        message = "⚠️ Invalid number format."
                else:
                    message = "⚠️ Category not found."

            elif choice == "3":
                clear_screen()
                print("=== WITHDRAW MONEY ===")
                print(f"Categories: {', '.join(budget_categories.keys())}\n")
                cat_name = input("Withdraw from which category?: ").strip().capitalize()
                if cat_name in budget_categories:
                    try:
                        amt = float(input("Enter amount: $"))
                        desc = input("Description (optional): ").strip()
                        if budget_categories[cat_name].withdraw(amt, desc):
                            message = f"✅ Withdrew ${amt:.2f} from {cat_name}."
                        else:
                            message = "❌ Transaction declined: Insufficient funds."
                    except ValueError:
                        message = "⚠️ Invalid number format."
                else:
                    message = "⚠️ Category not found."

            elif choice == "4":
                clear_screen()
                print("=== TRANSFER FUNDS ===")
                print(f"Categories: {', '.join(budget_categories.keys())}\n")
                source = input("Transfer FROM which category?: ").strip().capitalize()
                dest = input("Transfer TO which category?: ").strip().capitalize()
                
                if source in budget_categories and dest in budget_categories:
                    try:
                        amt = float(input(f"Enter amount to move: $"))
                        if budget_categories[source].transfer(amt, budget_categories[dest]):
                            message = f"✅ Moved ${amt:.2f} from {source} to {dest}."
                        else:
                            message = f"❌ Transfer declined: Insufficient funds in {source}."
                    except ValueError:
                        message = "⚠️ Invalid number format."
                else:
                    message = "⚠️ One or both categories do not exist."

            elif choice == "5":
                clear_screen()
                print("=== VIEW LEDGER ===")
                print(f"Categories: {', '.join(budget_categories.keys())}\n")
                cat_name = input("Which ledger would you like to view?: ").strip().capitalize()
                if cat_name in budget_categories:
                    clear_screen()
                    print(budget_categories[cat_name])
                    pause()
                else:
                    message = "⚠️ Category not found."

        elif choice == "6":
            if not budget_categories:
                message = "⚠️ No categories exist to chart yet."
            else:
                clear_screen()
                print(create_spend_chart(list(budget_categories.values())))
                pause()

        elif choice == "7":
            clear_screen()
            print("👋 Goodbye! Happy budgeting!")
            break
        else:
            message = "⚠️ Invalid choice. Please pick an option between 1 and 7."

if __name__ == "__main__":
    main()
