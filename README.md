Here is a clean, comprehensive, and professional `README.md` file designed for your budget tracker script.

---

# 📊 Terminal Budget Tracker

A lightweight, interactive Command Line Interface (CLI) budget application built in Python. This tool allows users to manage multiple budget categories, log deposits and withdrawals, seamlessly transfer funds between sub-accounts, and generate a dynamic bar chart visualization of their monthly expenditures.

---

## ✨ Features

* **📦 Dynamic Categories:** Create as many customizable budget categories (e.g., Food, Clothing, Entertainment) as needed.
* **💸 Full Ledger Management:** Log standard deposits and withdrawals with optional, customizable descriptions.
* **🔄 Inter-Category Transfers:** Easily move money between budget pools while keeping detailed audit trails automatically in both ledgers.
* **🛡️ Overdraft Protection:** Built-in verification checks prevent account balances from slipping below zero.
* **📈 Spending Analytics:** Generates an ASCII bar chart displaying the proportional spending breakdown by category.
* **🖥️ OS-Agnostic Interface:** Automatically clears the console window dynamically for both Windows (`cls`) and Unix-like (`clear`) terminals.

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.x** installed on your local machine. No external, third-party libraries are required.

### Installation & Run

1. Clone or download this project file locally. Save the script as `budget.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory containing `budget.py` and execute the application:

```bash
python budget.py

```

---

## 🛠️ How to Use

When launched, the program runs an interactive terminal loop with the following numbered options:

1. **Create a Category:** Initialize a new tracking bucket (e.g., *Food*).
2. **Deposit Money:** Add positive funds into a target category.
3. **Withdraw Money:** Subtract funds with custom expense descriptions.
4. **Transfer Money:** Shift a specific dollar amount directly out of one category pool and straight into another.
5. **View Category Ledger:** Generates a clean, formatted receipt layout showing all historical transactions alongside the category's running net total.
6. **Display Spend Chart Graph:** Evaluates total withdrawals across all categories and charts percentages to visually map out major budget leaks.
7. **Exit:** Safely terminates the interactive CLI loop.

---

## 📐 Preview Examples

### 📑 Detailed Category Ledger Output

```text
*************Food*************
Initial deposit        1000.00
Groceries               -10.15
Restaurant              -35.00
Transfer to Clothing    -50.00
Total: 904.85

```

### 📊 ASCII Spending Graph View

```text
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  E  
     o  l  n  
     o  o  t  
     d  t  e  
        h  r  
        i  t  
        n     
        g     

```

---

## ⚙️ Architecture Code Breakdown

The app utilizes basic Object-Oriented Programming (OOP) concepts:

* **`Category` (Class):** Keeps individual object states like the `name` instance variable and a list-of-dicts `ledger`. Handles mathematical balances and implements the custom string representation method `__str__` for clean console logs.
* **`create_spend_chart` (Function):** Takes a list of categories, dynamically aggregates the negative transaction logs, rounds down to the nearest 10th percentile, and builds an aligned vertical string bar chart.
