for i in range(1, 11):
    print(i)



n = int(input("Enter a number: "))


if n % 2 == 0:
    print(f"{n} is an even number.")
else:
    print(f"{n} is an odd number.")


n = int(input("Enter a number: "))

sum_n = 0
for i in range(1, n):
    sum_n += i
print(f"Sum of first {n} natural numbers is: {sum_n}")



string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels in the string is: {count}")

print("a" in vowels)




