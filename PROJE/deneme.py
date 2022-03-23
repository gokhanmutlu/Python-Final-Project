class Student:
    def __init__(self, ID, name = None, lastname = None, bookType = None, answers = None, choice1 = None, choice2 = None):
        self.name = name
        self.lastname = lastname
        self.setID(ID)
        self.bookType = bookType
        self.answers = answers
        self.choice1 = choice1
        self.choice2 = choice2

    def setID(self, ID):
        if len(str(ID))==6:
            self.__ID = str(ID)
        else:
            self.__ID = "1"
    
    def getID(self):
        return self.__ID

    def findBlank(self, recordingsOfKey):
        blank = 0
        if self.bookType == "A":
            for i in range(len(self.answers)):
                if self.answers[i] == "-":
                    blank += 1
        else:
            for j in range(len(self.answers)):
                if self.answers[j] == "-":
                    blank += 1
        return blank

    def findCorrect(self, recordingsOfKey):
        correct = 0
        if self.bookType == "A":
            for i in range(len(self.answers)):
                if self.answers[i] == recordingsOfKey[0][i]:
                    correct += 1
        else:
            for j in range(len(self.answers)):
                if self.answers[j] == recordingsOfKey[1][j]:
                    correct += 1
        return correct

    def findFalse(self, recordingsOfKey):
        return (40-self.findCorrect(recordingsOfKey)-self.findBlank(recordingsOfKey))

    def calculateScore(self, recordingsOfKey):
        return (self.findCorrect(recordingsOfKey) - (self.findFalse(recordingsOfKey)//4)) * 15


    def __str__(self):
        return str(self.__ID) + " " + self.name + " " + self.lastname 

    def displaySorted(self, recordingsOfKey):
        print(str(self.__ID) + " " + self.name + " " + self.lastname + " " + str(self.calculateScore(recordingsOfKey)))
    
    def displayResults(self,recordingsOfKey):
        print(str(self.__ID) + " " + self.name + " " + self.lastname + "\t" + self.bookType + " " + str(self.findCorrect(recordingsOfKey)) + " " + str(self.findFalse(recordingsOfKey)) + " " + str(self.findBlank(recordingsOfKey))+ " " +str((self.calculateScore(recordingsOfKey)//15))+ " " +str(self.calculateScore(recordingsOfKey))+ "\t   " + str(self.choice1) + ", " + str(self.choice2))

def readFile(fileName):
    myFile = open(fileName, "r", encoding="utf8")
    record = []
    for line in myFile:
        line = line.rstrip()
        record.append(line)
    myFile.close()
    return record

def listOfAnswers(recordingOfAnswers):
    objectList = []
    for answer in recordingOfAnswers:
        answer = answer.split()
        newAnswer = Student(int(answer[0]), bookType=answer[1], answers=answer[2], choice1=answer[3], choice2=answer[4])
        objectList.append(newAnswer)
    return objectList

def listToStudentObject(recordingOfStudents):
    objectList = []
    for student in recordingOfStudents:
        student = student.split()
        newStudent = Student(int(student[0]), " ".join(student[1:-1]), student[-1])
        objectList.append(newStudent)
    return objectList

def findStudent(objectList, ID):
    for student in objectList:
        if ID == student.getID():
            return (student.name, student.lastname)

recordingOfStudents = readFile("Student.txt")
lststudent = listToStudentObject(recordingOfStudents)
# for i in findStudent(lststudent,"124876"):
#     print(i,end=" ")

def listOfUniversity(recordingsOfUniversity):
    listOfUniversity = []
    for university in recordingsOfUniversity:
        university = university.split(",")
        listOfUniversity.append(university)
    return listOfUniversity

def findUni(listOfUniversity, No):
    for i in range(len(listOfUniversity)):
        if listOfUniversity[i][0] == No:
            return listOfUniversity[i][1]



recordingsOfKey = readFile("key.txt")
recordingofanswers = readFile("answers.txt")
recordingsOfUniversity = readFile("university.txt")
lstofuni = listOfUniversity(recordingsOfUniversity)

lstofanswers = listOfAnswers(recordingofanswers)
#print("  ID\tStudent Name   B.T|T|F|B|N|Score \t\t\tChosen University and Deparment ")

#3)e
# for answer in lstofanswers:
#     answer.name = findStudent(lststudent, answer.getID())[0]
#     answer.lastname = findStudent(lststudent, answer.getID())[1]
#     answer.choice1 = findUni(lstofuni, answer.choice1)
#     answer.choice2 = findUni(lstofuni, answer.choice2)
#     lst.append(answer)
#     answer.displayResults(recordingsOfKey)
    #print("-"*150)

#3) DOSYAYA YAZDIRMA:
# resultFile = open("results.txt","w",encoding="utf8")
# for answer in lstofanswers:
#     answer.name = findStudent(lststudent, answer.getID())[0]
#     answer.lastname = findStudent(lststudent, answer.getID())[1]
#     answer.choice1 = findUni(lstofuni, answer.choice1)
#     answer.choice2 = findUni(lstofuni, answer.choice2)
#     record = str(answer.getID()) + " " + answer.name + " " + answer.lastname + " " + answer.bookType + " " + str(answer.findCorrect(recordingsOfKey)) + " " + str(answer.findFalse(recordingsOfKey)) + " " + str(answer.findBlank(recordingsOfKey))+ " " +str((answer.calculateScore(recordingsOfKey)//15))+ " " +str(answer.calculateScore(recordingsOfKey))+ " " + str(answer.choice1) + " " + str(answer.choice2 + "\n")
#     resultFile.write(record)
# resultFile.close()

#4)NOTA GÖRE SIRALAMA:
# bütün öğrenci bilgilerini içeren liste yapabilirim. kullanışlı
#********************
# allInfoAboutStudent = []
# for answer in lstofanswers:
#     answer.name = findStudent(lststudent, answer.getID())[0]
#     answer.lastname = findStudent(lststudent, answer.getID())[1]
#     answer.choice1 = findUni(lstofuni, answer.choice1)
#     answer.choice2 = findUni(lstofuni, answer.choice2)
#     allInfoAboutStudent.append(answer)

def sortStudent(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-(i+1)):
            if lst[j].calculateScore(recordingsOfKey) < lst[j+1].calculateScore(recordingsOfKey):
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst
#4) nota göre sıralamaya yarayan...
# sortedStudent = sortStudent(allInfoAboutStudent)
# for i in sortedStudent:
#     i.displaySorted(recordingsOfKey)

# 5) öğrenci yerleştirme

def placedStudent(sortedStudent, lstofuni):
    placedlst = []
    nonplacedlst = []
    for student in sortedStudent:
        quota1 = int(lstofuni[int(student.choice1) - 1][3])
        quota2 = int(lstofuni[int(student.choice2) - 1][3])
        if (student.calculateScore(recordingsOfKey) >= int(lstofuni[int(student.choice1) - 1][2])) and (quota1 >= 1):
            print("if:q1",quota1)
            studentwhoplaced = lstofuni[int(student.choice1) - 1][1] + "--" + student.name + " " + student.lastname
            placedlst.append(studentwhoplaced)
            lstofuni[int(student.choice1) - 1][3] = int(lstofuni[int(student.choice1) - 1][3]) - 1
        elif (student.calculateScore(recordingsOfKey) >= int(lstofuni[int(student.choice2) - 1][2])) and (quota2 >= 1):
            studentwhoplaced = lstofuni[int(student.choice2) - 1][1] + "--" + student.name + " " + student.lastname
            placedlst.append(studentwhoplaced)
            lstofuni[int(student.choice2) - 1][3] = int(lstofuni[int(student.choice2) - 1][3]) - 1 
        else:
            studentwhonotplaced = "Could not be placed: " + student.name + " " + student.lastname
            nonplacedlst.append(studentwhonotplaced) 
    return (placedlst,nonplacedlst)


# Yerleştirme için atamalar
studentsToSettle = []
for answer in lstofanswers:
    answer.name = findStudent(lststudent, answer.getID())[0]
    answer.lastname = findStudent(lststudent, answer.getID())[1]
    studentsToSettle.append(answer)

sortedStudent = sortStudent(studentsToSettle)
lstPlacedandNonPlaced = placedStudent(sortedStudent, lstofuni)
# Yerleştirilen öğrenciler
for i in lstPlacedandNonPlaced[0]:
    print(i)

#6)Yerleşemeyen öğrenciler
for j in lstPlacedandNonPlaced[1]:
    print(j)

                                    




#*******************************GÖKHAN MUTLU'DAN DENEMELER********************************

# def listOfAnswersInfo(recordingsOfAnswers):
#     listOfAnswersInfo = []
#     for info in recordingsOfAnswers:
#         info = info.split(" ")
#         listOfAnswersInfo.append(info)
#     return listOfAnswersInfo

# def calculateScore(listOfAnswersInfo,recordingsOfKey):
#     correctanswer = 0
#     for index in range(len(listOfAnswersInfo)):
#         if listOfAnswersInfo[index][1] == "A":
#             for choice in range(len(listOfAnswersInfo[index])):
#                 if listOfAnswersInfo[index][choice] == recordingsOfKey[choice]:
#                     correctanswer += 1
#     print(correctanswer)


# a="İzmir Dokuz Eylül Üniversitesi Bilgisayar Mühendisliği"
# start=a.index("Üniversitesi")+11
# print(start)


#1)SEARCH STUDENT***********************************************
# def readFile(fileName):
#     myFile = open(fileName, "r", encoding="utf8")
#     studentList = []
#     for student in myFile:
#         student = student.rstrip()
#         student = student.split(" ")
#         newStudent = Student(int(student[0]), student[1], student[2])
#         studentList.append(newStudent)
#     myFile.close()

# print(readFile("student.txt"))

# myFile = open("student.txt", "r", encoding="utf8")
# studentList = []
# for student in myFile:
#     student = student.rstrip()
#     student = student.split(" ")
#     print(student)
#     newStudent = Student(int(student[0]), " ".join(student[1:-1]), student[-1])
#     studentList.append(newStudent)
# myFile.close()

#**********************************************************************************
class Student:
    def __init__(self, ID, name = None, lastname = None, bookType = None, answers = None, choice1 = None, choice2 = None):
        self.name = name
        self.lastname = lastname
        self.setID(ID)
        self.bookType = bookType
        self.answers = answers
        self.choice1 = choice1
        self.choice2 = choice2

    def setID(self, ID):
        if len(str(ID))==6:
            self.__ID = str(ID)
        else:
            self.__ID = "1"
    
    def getID(self):
        return self.__ID

    def findBlank(self, recordingsOfKey):
        blank = 0
        if self.bookType == "A":
            for i in range(len(self.answers)):
                if self.answers[i] == "-":
                    blank += 1
        else:
            for j in range(len(self.answers)):
                if self.answers[j] == "-":
                    blank += 1
        return blank

    def findCorrect(self, recordingsOfKey):
        correct = 0
        if self.bookType == "A":
            for i in range(len(self.answers)):
                if self.answers[i] == recordingsOfKey[0][i]:
                    correct += 1
        else:
            for j in range(len(self.answers)):
                if self.answers[j] == recordingsOfKey[1][j]:
                    correct += 1
        return correct

    def findFalse(self, recordingsOfKey):
        return (40-self.findCorrect(recordingsOfKey)-self.findBlank(recordingsOfKey))

    def calculateScore(self, recordingsOfKey):
        return (self.findCorrect(recordingsOfKey) - (self.findFalse(recordingsOfKey)//4)) * 15


    def __str__(self):
        return str(self.__ID) + " " + self.name + " " + self.lastname 

    def displaySorted(self, recordingsOfKey):
        print(str(self.__ID) + " " + self.name + " " + self.lastname + " " + str(self.calculateScore(recordingsOfKey)))
    
    def displayResults(self,recordingsOfKey):
        print(str(self.__ID) + " " + self.name + " " + self.lastname + "\t" + self.bookType + " " + str(self.findCorrect(recordingsOfKey)) + " " + str(self.findFalse(recordingsOfKey)) + " " + str(self.findBlank(recordingsOfKey))+ " " +str((self.calculateScore(recordingsOfKey)//15))+ " " +str(self.calculateScore(recordingsOfKey))+ "\t   " + str(self.choice1) + ", " + str(self.choice2))


def readFile(fileName):
    myFile = open(fileName, "r", encoding="utf8")
    record = []
    for line in myFile:
        line = line.rstrip()
        record.append(line)
    myFile.close()
    return record
#1)FindStudent*********************************************************************
def listToStudentObject(recordingOfStudents):
    objectList = []
    for student in recordingOfStudents:
        student = student.split()
        newStudent = Student(int(student[0]), " ".join(student[1:-1]), student[-1])
        objectList.append(newStudent)
    return objectList

def findStudent(objectList, ID):
    for student in objectList:
        if ID == student.getID():
            return (student.name, student.lastname)

# recordingOfStudents = readFile("Student.txt")
# lststudent = listToStudentObject(recordingOfStudents)
# for i in findStudent(lststudent,"124876"):
#     print(i,end=" ")
#2)find max base points university*****************************************************************************
def listOfUniversity(recordingsOfUniversity):
    listOfUniversity = []
    for university in recordingsOfUniversity:
        university = university.split(",")
        listOfUniversity.append(university)
    return listOfUniversity

def findMaxBasePointUni(listOfUniversity):
    maxpointuni = []
    maxPoint = listOfUniversity[0][2]
    for index in range(len(listOfUniversity)):
        if listOfUniversity[index][2] > maxPoint:
            maxPoint = listOfUniversity[index][2]
    for uni in range(len(listOfUniversity)):
        if listOfUniversity[uni][2] == maxPoint:
            maxpointuni.append(listOfUniversity[uni][1])
    return maxpointuni

# lstofuni = listOfUniversity(recordingsOfUniversity)
# maxpointuni = findMaxBasePointUni(lstofuni)
#3 create result txt******************************************************************
def listOfAnswers(recordingOfAnswers):
    objectList = []
    for answer in recordingOfAnswers:
        answer = answer.split()
        newAnswer = Student(int(answer[0]), bookType=answer[1], answers=answer[2], choice1=answer[3], choice2=answer[4])
        objectList.append(newAnswer)
    return objectList

def findUni(listOfUniversity, No):
    for i in range(len(listOfUniversity)):
        if listOfUniversity[i][0] == No:
            return listOfUniversity[i][1]

recordingsOfKey = readFile("key.txt")
recordingofanswers = readFile("answers.txt")
recordingsOfUniversity = readFile("university.txt")
recordingOfStudents = readFile("Student.txt")
lststudent = listToStudentObject(recordingOfStudents)
lstofuni = listOfUniversity(recordingsOfUniversity)

lstofanswers = listOfAnswers(recordingofanswers)


# resultFile = open("results.txt","w",encoding="utf8")
# for answer in lstofanswers:
#     answer.name = findStudent(lststudent, answer.getID())[0]
#     answer.lastname = findStudent(lststudent, answer.getID())[1]
#     answer.choice1 = findUni(lstofuni, answer.choice1)
#     answer.choice2 = findUni(lstofuni, answer.choice2)
#     record = str(answer.getID()) + " " + answer.name + " " + answer.lastname + " " + answer.bookType + " " + str(answer.findCorrect(recordingsOfKey)) + " " + str(answer.findFalse(recordingsOfKey)) + " " + str(answer.findBlank(recordingsOfKey))+ " " +str((answer.calculateScore(recordingsOfKey)//15))+ " " +str(answer.calculateScore(recordingsOfKey))+ " " + str(answer.choice1) + " " + str(answer.choice2 + "\n")
#     resultFile.write(record)
# resultFile.close()
#4)listsortedStudent********************************************************
def sortStudent(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-(i+1)):
            if lst[j].calculateScore(recordingsOfKey) < lst[j+1].calculateScore(recordingsOfKey):
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

# allInfoAboutStudent = []
# for answer in lstofanswers:
#     answer.name = findStudent(lststudent, answer.getID())[0]
#     answer.lastname = findStudent(lststudent, answer.getID())[1]
#     answer.choice1 = findUni(lstofuni, answer.choice1)
#     answer.choice2 = findUni(lstofuni, answer.choice2)
#     allInfoAboutStudent.append(answer)
# sortedStudent = sortStudent(allInfoAboutStudent)
# for i in sortedStudent:
#     i.displaySorted(recordingsOfKey)

#5)listplacedstudent************************************************************************
def placedStudent(sortedStudent, lstofuni):
    placedlst = []
    nonplacedlst = []
    for student in sortedStudent:
        quota1 = int(lstofuni[int(student.choice1) - 1][3])
        quota2 = int(lstofuni[int(student.choice2) - 1][3])
        if (student.calculateScore(recordingsOfKey) >= int(lstofuni[int(student.choice1) - 1][2])) and (quota1 >= 1):
            studentwhoplaced = lstofuni[int(student.choice1) - 1][1] + "--" + student.name + " " + student.lastname
            placedlst.append(studentwhoplaced)
            lstofuni[int(student.choice1) - 1][3] = int(lstofuni[int(student.choice1) - 1][3]) - 1
        elif (student.calculateScore(recordingsOfKey) >= int(lstofuni[int(student.choice2) - 1][2])) and (quota2 >= 1):
            studentwhoplaced = lstofuni[int(student.choice2) - 1][1] + "--" + student.name + " " + student.lastname
            placedlst.append(studentwhoplaced)
            lstofuni[int(student.choice2) - 1][3] = int(lstofuni[int(student.choice2) - 1][3]) - 1 
        else:
            studentwhonotplaced = "Could not be placed: " + student.name + " " + student.lastname
            nonplacedlst.append(studentwhonotplaced) 
    return (placedlst,nonplacedlst)

# studentsToSettle = []
# for answer in lstofanswers:
#     answer.name = findStudent(lststudent, answer.getID())[0]
#     answer.lastname = findStudent(lststudent, answer.getID())[1]
#     studentsToSettle.append(answer)

# sortedStudent = sortStudent(studentsToSettle)
# lstPlacedandNonPlaced = placedStudent(sortedStudent, lstofuni)

# # Yerleştirilen öğrenciler
# for i in lstPlacedandNonPlaced[0]:
#     print(i)

# #6)Yerleşemeyen öğrenciler
# for j in lstPlacedandNonPlaced[1]:
#     print(j)

#7)bonus(list the departments)***********************************************************************
def listAllDepartments(listOfUniversity):
    departmentLst = []
    for i in range(len(listOfUniversity)):
        alltext = listOfUniversity[i][1] 
        start = alltext.index("Üniversitesi") + 13
        department = alltext[start:]
        if department not in departmentLst:
            departmentLst.append(department)
    return departmentLst

# departmentlst = listAllDepartments(lstofuni)
# for department in departmentlst:
#     print(department)

YorN = "Y"
while YorN.upper() == "Y":  
    print("""–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1-)Search for a student with a given ID and display his/her name and last name.
2-)List the university/universities and departments with a maximum base points.
3-)Create a file named 'result.txt' for each student.
4-)List the students information sorted by their score.
5-)List the students placed in every university/department.
6-)List the students who were not be able to placed anywhere.
7-)List all the departments
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––""")
    recordingsOfKey = readFile("key.txt")
    recordingofanswers = readFile("answers.txt")
    recordingsOfUniversity = readFile("university.txt")
    recordingOfStudents = readFile("Student.txt")
    #********************************************************
    lststudent = listToStudentObject(recordingOfStudents)
    lstofuni = listOfUniversity(recordingsOfUniversity)
    lstofanswers = listOfAnswers(recordingofanswers)

    whichOption = input("What do you want to access: ")
    print()

    if whichOption == "1":
        studentID = input("Enter the number of the student you want to find: ")
        #gereksizmi??  lststudent = listToStudentObject(recordingOfStudents)
        for i in findStudent(lststudent, studentID):
            print(i,end=" ")

    elif whichOption == "2":
        # lstofuni = listOfUniversity(recordingsOfUniversity)
        maxpointuni = findMaxBasePointUni(lstofuni)
        for uni in maxpointuni:
            print(uni)

    elif whichOption == "3":
        #lststudent = listToStudentObject(recordingOfStudents)
        #lstofuni = listOfUniversity(recordingsOfUniversity)
        #lstofanswers = listOfAnswers(recordingofanswers)

        resultFile = open("results.txt","w",encoding="utf8")
        for answer in lstofanswers:
            answer.name = findStudent(lststudent, answer.getID())[0]
            answer.lastname = findStudent(lststudent, answer.getID())[1]
            answer.choice1 = findUni(lstofuni, answer.choice1)
            answer.choice2 = findUni(lstofuni, answer.choice2)
            record = str(answer.getID()) + " " + answer.name + " " + answer.lastname + " " + answer.bookType + " " + str(answer.findCorrect(recordingsOfKey)) + " " + str(answer.findFalse(recordingsOfKey)) + " " + str(answer.findBlank(recordingsOfKey))+ " " +str((answer.calculateScore(recordingsOfKey)//15))+ " " +str(answer.calculateScore(recordingsOfKey))+ " " + str(answer.choice1) + " " + str(answer.choice2 + "\n")
            resultFile.write(record)
        resultFile.close()
        print("results.txt was created!")

    elif whichOption == "4":
        allInfoAboutStudent = []
        for answer in lstofanswers:
            answer.name = findStudent(lststudent, answer.getID())[0]
            answer.lastname = findStudent(lststudent, answer.getID())[1]
            answer.choice1 = findUni(lstofuni, answer.choice1)
            answer.choice2 = findUni(lstofuni, answer.choice2)
            allInfoAboutStudent.append(answer)
        sortedStudent = sortStudent(allInfoAboutStudent)
        for i in sortedStudent:
            i.displaySorted(recordingsOfKey)

    elif whichOption == "5":
        studentsToSettle = []
        for answer in lstofanswers:
            answer.name = findStudent(lststudent, answer.getID())[0]
            answer.lastname = findStudent(lststudent, answer.getID())[1]
            studentsToSettle.append(answer)

        sortedStudent = sortStudent(studentsToSettle)
        lstPlacedandNonPlaced = placedStudent(sortedStudent, lstofuni)

        # Yerleştirilen öğrenciler
        for i in lstPlacedandNonPlaced[0]:
            print(i)

    elif whichOption == "6":
        studentsToSettle = []
        for answer in lstofanswers:
            answer.name = findStudent(lststudent, answer.getID())[0]
            answer.lastname = findStudent(lststudent, answer.getID())[1]
            studentsToSettle.append(answer)

        sortedStudent = sortStudent(studentsToSettle)
        lstPlacedandNonPlaced = placedStudent(sortedStudent, lstofuni)

        #6)Yerleşemeyen öğrenciler
        for j in lstPlacedandNonPlaced[1]:
            print(j)

    elif whichOption == "7":
        departmentlst = listAllDepartments(lstofuni)
        for department in departmentlst:
            print(department)

    print()
    print()
    YorN = input("Do you want to contiune yes(Y) or no(N): ")