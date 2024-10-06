number = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")




my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for num in my_list[::-1]:
    print(num)




num = 7


for i in range(1, num + 1):
    print(i ** 3)
