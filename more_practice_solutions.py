

# define a number
number = int(input("Enter a number to print its multiplication table: "))


# loop through the number until and including that index 
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")




# define a list 
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# loop through a lidst backwards  
for num in my_list[::-1]:
    print(num)





# define a number
num = 7

# loop through the number 
for i in range(1, num + 1):
    # 
    print(i ** 3)
