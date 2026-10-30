# Kiambu Dairy Co-op Price Checker

A clean, non-technical terminal application for calculating weekly farmer milk payouts.

## 🛠 Setup & Run

1. Make sure Python 3 is installed on your computer.
2. Put `dairy_calculator.py` and `price.txt` inside the exact same folder.
3. Open your terminal or command prompt, navigate to the folder, and run:
   ```bash
   python dairy_calculator.py
   ```

## ⚙️ Updating the Weekly Price
To change the active buying rate, open the `price.txt` file, overwrite the existing number with the new price (e.g., `58.50`), and save. The application updates automatically.

## 📊 Example System Output
```text
======================================
 Kiambu Dairy Co-op Payment Calculator
======================================
Active Buying Price: KES 55.00 per litre

Enter Farmer Name: John Kamau
Enter Litres Supplied: 120.5

--------------------------------------
Farmer Statement Summary
--------------------------------------
Farmer Name : John Kamau
Supply Vol. : 120.50 Litres
Rate Applied: KES 55.00/Litre
Total Owed  : KES 6,627.50
--------------------------------------
```
