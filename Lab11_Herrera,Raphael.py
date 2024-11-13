gradelist = []
studentGrade = 1

while studentGrade < 6:
    gradeInput = float(input(f"Enter Grade {studentGrade}: "))
    
    if 40 <= gradeInput <= 100: 
            gradelist.append(gradeInput) 
            studentGrade += 1
    else:
        print("Invalid input.")
print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
gradeAverage = sum(gradelist) / len(gradelist)

passing = 0
for gradeInput in gradelist:
    if gradeInput >= 75:
        passing += 1
        
passingPercent = (passing / len(gradelist)) * 100

print(f"Grades: " , gradelist)
print(f"Grade Average: " , gradeAverage)
print(f"Passed Grade: " , passing)
print(f"Percentage: " , passingPercent)
        