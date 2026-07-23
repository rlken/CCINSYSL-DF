tasks_at = ["ASSIGNMENT1", "QUIZ1", "ACTIVITY1", "ACTIVITY2", "ACTIVITY3"]
tasks_le = ["LONG EXAM1", "LONG EXAM2"]
tasks_dexm = ["DEPARTMENTAL EXAM"]

print("👽GRADE COMPUTATION👽\n")

total_number_of_items = 0
total_scores = 0
print("📋ASSESSMENT TASKS📋")
at_weight = float(input("Assessment Tasks weight (e.g. 0.30 for 30%): "))
for task in tasks_at:
    number_of_items = float(input(f"{task} - Number of Items: "))
    score = float(input(f"{task} - Score: "))
    total_number_of_items += number_of_items
    total_scores += score
at_percentage = (total_scores / total_number_of_items) * 100
at_average = at_percentage * at_weight
print("\n✪RESULTS✪")
print(f"Total Number of Items: {total_number_of_items}")
print(f"Total Scores: {total_scores}")
print(f"ASSESSMENT TASKS AVERAGE: {at_average:.2f}%")

total_number_of_items = 0
total_scores = 0
print("\n📋LONG EXAMS📋")
le_weight = float(input("Long Exam weight (e.g. 0.40 for 40%): "))
for task in tasks_le:
    number_of_items = float(input(f"{task} - Number of Items: "))
    score = float(input(f"{task} - Score: "))
    total_number_of_items += number_of_items
    total_scores += score
le_percentage = (total_scores / total_number_of_items) * 100
le_average = le_percentage * le_weight
print("\n✪RESULTS✪")
print(f"Total Number of Items: {total_number_of_items}")
print(f"Total Scores: {total_scores}")
print(f"LONG EXAM AVERAGE: {le_average:.2f}%")

total_number_of_items = 0
total_scores = 0
print("\n📋DEPARTMENTAL EXAM📋")
dexm_weight = float(input("Departmental Exam weight (e.g. 0.20 for 20%): "))
for task in tasks_dexm:
    number_of_items = float(input(f"{task} - Number of Items: "))
    score = float(input(f"{task} - Score: "))
    total_number_of_items += number_of_items
    total_scores += score
dexm_percentage = (total_scores / total_number_of_items) * 100
dexm_average = dexm_percentage * dexm_weight
print("\n✪RESULTS✪")
print(f"Total Number of Items: {total_number_of_items}")
print(f"Total Scores: {total_scores}")
print(f"DEXM AVERAGE: {dexm_average:.2f}%")

final_grade = at_average + le_average + dexm_average
print("\n♕FINAL GRADE♕")
print(f"AT:   {at_average:.2f}%")
print(f"LEX:  {le_average:.2f}%")
print(f"DEXM: {dexm_average:.2f}%")
print(f"FINAL GRADE: {final_grade:.2f}%")