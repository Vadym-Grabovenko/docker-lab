from dotenv import load_dotenv
import os

# Отримання даних зі змінних середовища
load_dotenv()

initial_amount = float(os.getenv("INITIAL_AMOUNT"))
interest_rate = float(os.getenv("INTEREST_RATE"))
periods = int(os.getenv("PERIODS"))

# Розрахунок складних відсотків
amount = initial_amount

print("Розрахунок депозиту зі складними відсотками")
print("-" * 50)
print(f"{'Рік':<10}{'Сума на початку':<20}{'Сума на кінець':<20}")

for year in range(1, periods + 1):
    start_amount = amount
    amount *= (1 + interest_rate / 100)

    print(f"{year:<10}{start_amount:<20.2f}{amount:<20.2f}")

print("-" * 50)
print(f"Початкова сума: {initial_amount:.2f}")
print(f"Відсоткова ставка: {interest_rate}%")
print(f"Кількість років: {periods}")
print(f"Кінцева сума: {amount:.2f}")
print(f"Отриманий прибуток: {amount - initial_amount:.2f}")