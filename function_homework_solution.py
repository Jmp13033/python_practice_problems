import math

def area_of_circle(radius):
    return math.pi * radius ** 2


print(area_of_circle(5)) 





def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


print(celsius_to_fahrenheit(25)) 





def find_largest(numbers):
    if numbers:
        return max(numbers)
     
print(find_largest([3, 8, 2, 7, 5]))  



def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


print(count_vowels("Hello World"))  





def calculate_average_grade(students_grades):
    average_grades = {}
    for student, grades in students_grades.items():
        average_grades[student] = round(sum(grades) / len(grades), 2)
    return average_grades




students_grades = {
    "Alice": [85, 90, 78],
    "Bob": [80, 82, 84],
    "Charlie": [95, 92, 88]
}
print(calculate_average_grade(students_grades)) 







