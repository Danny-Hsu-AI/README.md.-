import random

# 產生 1 到 100 的隨機整數
secret = random.randint(1, 100)
guess = 0

print("猜一個 1 到 100 的數字！")

while guess != secret:
    guess = int(input("你的猜測是："))
    if guess < secret:
        print("太小了！")
    elif guess > secret:
