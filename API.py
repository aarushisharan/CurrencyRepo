import sys
sys.path.append('C:\Users\Aarushi\microagents\myenv\CurrencyRepo')
import currency

from flask import Flask
from currency import CurrencyExchangeAgent

app = Flask(__name__)

if __name__ == "__main__":
    agent = CurrencyExchangeAgent(
        "ExchangeMonitorAgent",
        "USD",
        ["INR", "EUR"],
        {"INR": (82.55, 82.60), "EUR": (1.18, 1.19)},
        "https://api.example.com/exchange-rates"  # Replace with the actual API URL
    )
    agent.start()

if __name__ == "__main__":
    app.run()
