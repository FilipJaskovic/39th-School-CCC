def generate_amounts(coins):
    amounts = []
    for target in range(1, 101):
        min_coins = [0] * (target + 1)
        min_coins[0] = []
        
        for i in range(1, target + 1):
            min_coins[i] = None
            for c in coins:
                if i >= c and min_coins[i - c] is not None:
                    if min_coins[i] is None or len(min_coins[i]) > len(min_coins[i - c]) + 1:
                        min_coins[i] = min_coins[i - c] + [c]
        
        amount = []
        for coin, count in sorted([(c, min_coins[target].count(c)) for c in set(min_coins[target])], reverse=True):
            amount.append(f"{count}x{coin}")
        amounts.append(' '.join(amount))
    
    return amounts


with open("level3_5.in", 'r') as file:
    N = int(file.readline())
    jkfdlsk = file.readline() 
    
    currencies = []
    for _ in range(N):
        coins = list(map(int, file.readline().split()))
        currencies.append(coins)

print(currencies)

with open("output5.txt", 'w') as file:
    for coins in currencies:
        amounts = generate_amounts(coins)
        for amount in amounts:
            file.write(amount + '\n')