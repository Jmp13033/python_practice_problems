
# Square of Even Numbers:

# Given a list of integers, create a new list containing the squares of only the even numbers.

numbers = [1, 2, 3, 4, 5, 6]

numbers = [x ** 2 for x in numbers if x % 2 == 0]

print(numbers)

# Expected output: [4, 16, 36]




words = ["cat", "elephant", "dog", "rat"]

long_words = [word for word in words if len(word) > 3]

print(long_words)

# Expected output: ['elephant']



words = ["hello", "world", "python"]

capitalized_word = [ word.title() for word in words]

print(capitalized_word)

# Expected output: ['Hello', 'World', 'Python']


words = ["apple", "banana", "Avocado", "cherry", "apricot", "Blueberry"]
a_words = [a_word for a_word in words if a_word.lower().startswith("a")]

print(a_words)
# Output: ['apple', 'Avocado', 'apricot']


# Expected output: ['apple', 'Avocado', 'apricot']