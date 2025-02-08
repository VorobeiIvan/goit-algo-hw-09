import time
import matplotlib.pyplot as plt

# Функція для жадібного алгоритму
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]  # Доступні номінали монет
    result = {}
    
    for coin in coins:
        count = amount // coin  # Кількість монет цього номіналу
        if count > 0:
            result[coin] = count
            amount -= count * coin  # Зменшуємо суму
    
    return result

# Функція для алгоритму динамічного програмування
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]  # Доступні номінали монет
    dp = [float('inf')] * (amount + 1)  # Ініціалізуємо таблицю
    dp[0] = 0  # Для суми 0 потрібно 0 монет
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)  # Оновлюємо мінімальну кількість монет
    
    # Відновлюємо рішення
    result = {}
    while amount > 0:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                amount -= coin
                break
    
    return result

# Функція для вимірювання часу виконання
def measure_time(amount):
    start = time.time()
    find_coins_greedy(amount)
    greedy_time = time.time() - start

    start = time.time()
    find_min_coins(amount)
    dp_time = time.time() - start

    return greedy_time, dp_time

# Вимірювання часу для різних сум
amounts = [i for i in range(1, 1001)]  # Тести від 1 до 1000
greedy_times = []
dp_times = []

for amount in amounts:
    greedy_time, dp_time = measure_time(amount)
    greedy_times.append(greedy_time)
    dp_times.append(dp_time)

# Виведення результатів
plt.plot(amounts, greedy_times, label='Жадібний алгоритм')
plt.plot(amounts, dp_times, label='Динамічне програмування')
plt.xlabel('Сума (amount)')
plt.ylabel('Час виконання (секунди)')
plt.legend()
plt.title('Порівняння часу виконання алгоритмів')
plt.show()

# Виведення результату для певної суми
amount = 113
print("Час виконання жадібного алгоритму для суми", amount, ":", measure_time(amount)[0])
print("Час виконання динамічного програмування для суми", amount, ":", measure_time(amount)[1])
