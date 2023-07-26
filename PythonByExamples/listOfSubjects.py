#!/usr/bin/python3

subjects = [
    "english","maths","science","social studies","ict","economics","rme"
]

print("Remove a Subject")
for s in subjects:
    print(f"{subjects.index(s)} - {s.upper()}")

while True:
    print("q - Quit")

    subject = input("Which subject do you want to remove: ")
    subject = subject.lower()

    if subject == 'q':
        break

    elif subject in subjects: # Remove subject
        subjects.remove(subject)
        for s in subjects:  # Display subject
            print(f"{subjects.index(s)} - {s.upper()}")

    elif int(subject) <= 0 or int(subject) > 0:
        if int(subject) >= len(subjects):
            print(f"{subject} not in list")
        else:
            subjects.pop(int(subject))
            for s in subjects:  # Display subject
                print(f"{subjects.index(s)} - {s.upper()}")
    else:
        print(f"{subject} not in list")