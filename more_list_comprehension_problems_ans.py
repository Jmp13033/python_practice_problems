# 1. Double of Odd Numbers
numbers = [1, 2, 3, 4, 5]
result = [num * 2 for num in numbers if num % 2 != 0]
print(result)  


# 2. Remove Words Containing 'e'
words = ["tree", "book", "pen", "apple", "sky"]
result = [word for word in words if 'e' not in word]
print(result)  


# 3. Uppercase Only Long Words
words = ["happy", "sun", "joyful", "bright", "day"]
result = [word.upper() if len(word) > 4 else word for word in words]
print(result)  


# 4. Cubed Values of Numbers Greater Than 3
numbers = [1, 2, 3, 4, 5]
result = [num ** 3 for num in numbers if num > 3]
print(result)  


# 5. Filter Only Positive Numbers
numbers = [-1, 3, -2, 8, 0, -5, 7]
result = [num for num in numbers if num > 0]
print(result)  


# 6. Create List of First Letters
words = ["apple", "banana", "cherry"]
result = [word[0] for word in words]
print(result)  


# 7. Sum of Digits in Each Number
numbers = [23, 45, 67]
result = [sum(int(digit) for digit in str(num)) for num in numbers]
print(result)  


# 8. Even Length Words in Lowercase
words = ["Tiger", "Dog", "Elephant", "Cat", "Deer"]
result = [word.lower() for word in words if len(word) % 2 == 0]
print(result) 


# 9. Filter Out Numbers Divisible by 3
numbers = [1, 3, 4, 6, 7, 9, 10]
result = [num for num in numbers if num % 3 != 0]
print(result) 


# 10. Reverse Words with Odd Length
words = ["apple", "banana", "kiwi", "cherry", "mango"]
result = [word[::-1] if len(word) % 2 != 0 else word for word in words]
print(result)  
