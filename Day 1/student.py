student = {
    "name": "Khushi",
    "age": 20,
    "course": "Computer Engineering",
    "skills": ["Python", "HTML", "CSS"],
    "city": "Ahmedabad",
    "semester": 5
}
print("Student Details")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Skills:", student["skills"])
print("City:", student["city"])
print("Semester:", student["semester"])
print(student)

student["skills"].append("Django")
print(student["skills"])

student["city"] = "Mumbai"
print("Updated City:", student["city"])
print(student)

