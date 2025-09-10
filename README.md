# currency-converter
# 💱 Currency Converter (Python CLI)

A simple **command-line currency converter** built with Python and [FreeCurrencyAPI](https://freecurrencyapi.com/).  
It lets you **list currencies, get live exchange rates, and convert amounts** between different currencies securely.

---

## 🚀 Features
- ✅ List all available currencies with name & symbol  
- ✅ Get live exchange rates between any two currencies  
- ✅ Convert any amount from one currency to another  
- ✅ Secure API key handling using `.env` file  
- ✅ Interactive command-line interface  

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ukroy001/currency-converter.git
   cd currency-converter
2.Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3.Install dependencies
pip install -r requirements.txt

4.Create a .env file in the project root and add your API key:
CURRENCY_API_KEY=your_api_key_here

usage:
python currency_converter.py

what you will see:
Welcome to the currency converter!
List - lists the different currencies
Convert - convert from one currency to another
Rate - get the exchange rate of two currencies

The structure:
currency-converter/
│── currency_converter.py   # main script
│── .env                    # stores your API key (not pushed to GitHub)
│── requirements.txt        # Python dependencies
│── README.md               # project documentation
│── .gitignore              # ignored files (.env, venv, etc.)

