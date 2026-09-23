marks = {
    "Ashik": 85,
    "Rahul": 35,
    "John": 70,
    "Arun": 25
}

mark_above_40 = {name : mark for name,mark in marks.items() if mark>=40 }
print(mark_above_40)

status = {name : "Pass" if mark>40 else "Fail" for name,mark in marks.items()}
print(status)

