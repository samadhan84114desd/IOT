"""
The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
Average Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59 F
"""
sub1=float(input("Enter sub1 marks: "))#&&8
sub2=float(input("Enter sub2 marks: "))
sub3=float(input("Enter sub3 marks: "))

average=(sub1+sub2+sub3)/3
if average>=90 and average<=100:
    grade='A'
elif average>=80 and average<=89:
    grade='B'
elif average>=70 and average<=79:
    grade='C'
elif average>=60 and average<=69:
    grade='D'
else:
    grade='F'
print(f"average={average}")
print(f"grade={grade}")