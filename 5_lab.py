# Визначення ймовірностей станів
P_theta = {1: 0.2, 2: 0.4, 3: 0.4}  # ймовірності θ1, θ2, θ3

# Матриця прибутків (рішення x1, x2, x3)
profits = {
    'x1': [6.0, 3.5, 0.5],  # прибутки для x1
    'x2': [6.5, 7.0, 4.0],  # прибутки для x2
    'x3': [3.5, 3.5, 8.5]   # прибутки для x3
}

# Обчислення очікуваних прибутків
expected_profits = {}
for x, values in profits.items():
    expected_profit = sum(P_theta[i] * values[i-1] for i in range(1, 4))
    expected_profits[x] = expected_profit

# Визначення оптимальної стратегії
optimal_decision = max(expected_profits, key=expected_profits.get)  # максимізуємо прибуток
optimal_value = expected_profits[optimal_decision]  # значення оптимального прибутку

# Результат
print("Оптимальне рішення:", optimal_decision)
print("Очікуваний прибуток:", optimal_value)
