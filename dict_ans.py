grades = {
    "Alice": {
        "Math": 85,
        "Science": 92,
        "English": 88
    },
    "Bob": {
        "Math": 78,
        "Science": 81,
        "English": 74
    },
    "Charlie": {
        "Math": 90,
        "Science": 95,
        "English": 85
    }
}


alice_science_grade = grades["Alice"]["Science"]
print("Alice's Science grade:", alice_science_grade)


grades["Bob"]["History"] = 89

print("Bob's updated grades:", grades["Bob"])


grades["Charlie"]["English"] = 90
print("Charlie's updated grades:", grades["Charlie"])

