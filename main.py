def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]  # Доступні номінали монет
    result = {}
    
    for coin in coins:
        count = amount // coin  # Кількість монет цього номіналу
        if count > 0:
            result[coin] = count
            amount -= count * coin  # Зменшуємо суму
    
    return result


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


# Приклад використання функцій
if __name__ == "__main__":
    amount = 113
    print("Жадібний алгоритм:", find_coins_greedy(amount))
    print("Динамічне програмування:", find_min_coins(amount))
