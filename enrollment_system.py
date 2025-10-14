print("===Enrollment System===")

name = input("Enter student name: ")
address = input("Enter address: ")
age = int(input("Enter age: "))

print("\nAvailable Courses:")
courses = {"BSIT": 500, "BSCS":550, "BSCPE":600}
for c in courses:
	print("-", c)
course = input("Select course:").upper()

print("\nSubjects Offered:")
subjects = {"Programming": 3, "Database": 3, "Networking": 3,"AI": 2}
for s, u in subjects.items():
	print(f"- {s} ({u} units)")

selected = input("Enter subjects(comma separted): ").split(",")
total_units = sum(subjects[sub.strip()] for sub in selected if sub.strip() in subjects)
rate = courses.get(course, 0)
total_payment = total_units * rate

print("\n===ENROLLMENT SYSTEM===")
print("Name:", name)
print("Address:", address)
print("Age:", age)
print("Course:", course)
print("Subjects:", ",".join(selected))
print("Total Units:", total_units)
print("Rate per unit:", rate)
print("Total Payment: ", total_payment)
