print('Enter Quiz 1')
quiz1 = input()
print('Enter Quiz 2')
quiz2 = input()
print('Enter Quiz 3')
quiz3 = input()
print('Enter Quiz 4')
quiz4 = input()
print('Enter Quiz 5')
quiz5 = input()
print('Enter Quiz 6')
quiz6 = input()

print('Quiz Grade')
QuizGrade = (int(quiz1) + int(quiz2) + int(quiz3) + int(quiz4) + int(quiz5) + int(quiz6)) / int(6)
print(QuizGrade)

print('Enter Lab 1')
lab1 = input()
print('Enter Lab 2')
lab2 = input()
print('Enter Lab 3')
lab3 = input()
print('Enter Lab 4')
lab4 = input()
print('Enter Lab 5')
lab5 = input()
print('Enter Lab 6')
lab6 = input()
print('Enter Lab 7')
lab7 = input()
print('Enter Lab 8')
lab8 = input()
print('Enter Lab 9')
lab9 = input()
print('Enter Lab 10')
lab10 = input()

print('Lab Grade' )
LabGrade = (int(lab1) + int(lab2) + int(lab3) + int(lab4) + int(lab5) + int(lab6) + int(lab7) + int(lab8) + int(lab9) + int(lab10)) / int(10)
print(LabGrade)

print('Enter Project 1')
project1 = input()
print('Enter Project 2')
project2 = input()

print('Project Grade')
ProjectGrade = (int(project1) + int(project2)) / int(2)
print(ProjectGrade)

print('Final Grade')
print()
FinalGrade = ((QuizGrade * .3) + (LabGrade * .4) + (ProjectGrade * .3))
print(FinalGrade)
print()

if FinalGrade >= 90:
    print('A')
if FinalGrade >= 80:
    print('B')
if FinalGrade >= 70:
    print('C')
if FinalGrade >= 60:
    print('D')
if FinalGrade < 60:
    print('F')
else:
    print('You did not qualify to receive a grade')
