class Student:  # I created to add information about student in 'student.txt' and 'results.txt'
    def __init__(self, ID, name = None, lastname = None, bookType = None, answers = None, choice1 = None, choice2 = None): #class variables
        self.name = name
        self.lastname = lastname
        self.setID(ID)  # private variable. it is checking in setID().
        self.bookType = bookType
        self.answers = answers
        self.choice1 = choice1
        self.choice2 = choice2

    def setID(self, ID): # ID variable assignment is doing here.
        if len(str(ID))==6:# If length of ID equals 6. It assign ID.
            self.__ID = str(ID)
        else:              # If is not. Automatically '1' assigns.
            self.__ID = "1"
    
    def getID(self):      # To access ID from out of class. 
        return self.__ID

    def findBlank(self, recordingsOfKey): # To find blanks number.
        blank = 0
        if self.bookType == "A":          # If book type is 'A'. It evaluates answer of student according that.
            for i in range(len(self.answers)):
                if self.answers[i] == "*":
                    blank += 1            # For every blank it is increasing blanks number.
        else:                             # If book type is 'B'. It evaluates answer of student according that.
            for j in range(len(self.answers)):
                if self.answers[j] == "*":
                    blank += 1            # For every blank it is increasing blanks number.
        return blank

    def findCorrect(self, recordingsOfKey): # It takes recordings in 'key.txt' which has key of answer.
        correct = 0
        if self.bookType == "A":            # If book type is 'A'. It evaluates answer of student according that.
            for i in range(len(self.answers)):
                if self.answers[i] == recordingsOfKey[0][i]: # Compare the book type A and student answer which has book type 'A'.
                    correct += 1            # For every blank it is increasing corrects number.
        else:
            for j in range(len(self.answers)):  # If book type is 'B'. It evaluates answer of student according that.
                if self.answers[j] == recordingsOfKey[1][j]: # Compare the book type B and student answer which has book type 'B'.
                    correct += 1            # For every blank it is increasing corrects number.
        return correct

    def findFalse(self, recordingsOfKey):   # Finding falses numbers using findCorrect() and findBlanks() methods.
        return (40-self.findCorrect(recordingsOfKey)-self.findBlank(recordingsOfKey))

    def calculateScore(self, recordingsOfKey): # Calculating score of student with help other methods which are above.
        return (self.findCorrect(recordingsOfKey) - (self.findFalse(recordingsOfKey)/4)) * 15


    def __str__(self): # Just printing student ID, name, lastname.
        return str(self.__ID) + " " + self.name + " " + self.lastname 

    def displaySorted(self, recordingsOfKey): # Created to print some information according to the student's score.
        print(str(self.__ID) + " " + self.name + " " + self.lastname + " " + str(self.calculateScore(recordingsOfKey)))
    
def readFile(fileName): # Created to read any text file and add the each line in txt in a list as a record.
    myFile = open(fileName, "r", encoding="utf8")
    record = []         # To keep each line that is in text.
    for line in myFile:
        line = line.rstrip()  # To remove '\n' at the end of line.
        record.append(line)   
    myFile.close()
    return record
#1)FindStudent*********************************************************************
def listToStudentObject(recordingOfStudents): # It will create list of student objects.
    objectList = []
    for student in recordingOfStudents:  # recording of student is using here.
        student = student.split()        # separates each line according to spaces.
        newStudent = Student(int(student[0]), " ".join(student[1:-1]), student[-1]) # After splitting, student objects are creating as ID, name, lastname.
        objectList.append(newStudent)    # student object is adding to list.
    return objectList

def findStudent(objectList, ID):  # To find student from his/her ID.
    for student in objectList:    # for each student in object list of student. 
        if ID == student.getID(): # that checks entered ID is same with student ID or not.
            return (student.name, student.lastname) # and returns as Tuple. Because that will be used to combine txt for student object.

#2)find max base points university*****************************************************************************
def listOfUniversity(recordingsOfUniversity): # Takes recording of university as parameter and split each line.
    listOfUniversity = []
    for university in recordingsOfUniversity: 
        university = university.split(",")    # separates each line according to comma.
        listOfUniversity.append(university)
    return listOfUniversity     # returns as a list.

def findMaxBasePointUni(listOfUniversity): # to find max point university or university.
    maxpointuni = []
    maxPoint = listOfUniversity[0][2]      # it just assigned to compare other points.
    for index in range(len(listOfUniversity)): # as many as the number of elements in the list.
        if listOfUniversity[index][2] > maxPoint: # it compares the points to the max point.
            maxPoint = listOfUniversity[index][2] # if it is bigger than max point. it will be new max point.
    for uni in range(len(listOfUniversity)):      # to find if there is more than one university which has max point.
        if listOfUniversity[uni][2] == maxPoint:  # if it equals to the max point.
            maxpointuni.append(listOfUniversity[uni][1] + " " + maxPoint) # appending to the list as university name and max point.
    return maxpointuni  # returns as a list.

#3 create result txt******************************************************************
def listOfAnswers(recordingOfAnswers): # it creates object of student from answer txt. (ID, book type, answers, choice1, choice2)
    objectList = []
    for answer in recordingOfAnswers: # for each recording.
        answer = answer.split()      # separates each recording according to blanks.
        # that will create student object which has got ID, book type, answers, choice1, choice2 attributes.
        newAnswer = Student(int(answer[0]), bookType=answer[1], answers=answer[2], choice1=answer[3], choice2=answer[4])
        objectList.append(newAnswer)  # that will append to the list.
    return objectList  # returns as a list.

def findUni(listOfUniversity, No): # It will work to combine attributes.
    for i in range(len(listOfUniversity)):  # as many as the number of elements in the list
        if listOfUniversity[i][0] == No:    # that checks entered no is same with universit no or not.
            return listOfUniversity[i][1]

#4)listsortedStudent********************************************************
def sortStudent(lst): # that will sort the student according to their scores from high to low.
    for i in range(len(lst)-1): # for any index lenght of student object list.
        for j in range(len(lst)-(i+1)): # each time that will reduce the compare numbers.
            if lst[j].calculateScore(recordingsOfKey) < lst[j+1].calculateScore(recordingsOfKey): # if the one on the right is bigger than the other. 
                temp = lst[j]  # We temporarily assign away so as not to lose.
                lst[j] = lst[j+1] # we will change of their index number.
                lst[j+1] = temp # and it will assign with temp.
    return lst 

#5)listplacedstudent ************************************************************************
def placedStudent(sortedStudent, lstofuni):  # to place the students. 
    placedlst = []
    nonplacedlst = []
    for student in sortedStudent: # for every student object in sorted student list.
        quota1 = int(lstofuni[int(student.choice1) - 1][3]) # Quota in 1st choice.
        quota2 = int(lstofuni[int(student.choice2) - 1][3]) # Quota in 2st choice.
        if (student.calculateScore(recordingsOfKey) >= int(lstofuni[int(student.choice1) - 1][2])) and (quota1 >= 1): # the student's score is both greater or equal, and if there are places available at the university.
            studentwhoplaced = lstofuni[int(student.choice1) - 1][1] + "--" + student.name + " " + student.lastname   # string which has got choisen university name, student name and last name.
            placedlst.append(studentwhoplaced)  # adding to the list.
            lstofuni[int(student.choice1) - 1][3] = int(lstofuni[int(student.choice1) - 1][3]) - 1 # after student placed it reduce the quota.
        elif (student.calculateScore(recordingsOfKey) >= int(lstofuni[int(student.choice2) - 1][2])) and (quota2 >= 1): # the student's score is both greater or equal, and if there are places available at the second chosen university.
            studentwhoplaced = lstofuni[int(student.choice2) - 1][1] + "--" + student.name + " " + student.lastname # string which has got choisen university name, student name and last name.
            placedlst.append(studentwhoplaced) # adding to the list.
            lstofuni[int(student.choice2) - 1][3] = int(lstofuni[int(student.choice2) - 1][3]) - 1 # after student placed it reduce the quota.
        else:  # If the student cannot be placed in any university of her choice. it will append to the nonplaced list. 
            studentwhonotplaced = "Could not be placed: " + student.name + " " + student.lastname
            nonplacedlst.append(studentwhonotplaced) 
    return (placedlst,nonplacedlst) # it returns tuple to access both of the lists.

#7)bonus(list the departments)***********************************************************************
def listAllDepartments(listOfUniversity): # that will list just one time for every departments.
    departmentLst = []
    for i in range(len(listOfUniversity)): # as many as the number of elements in the list.
        alltext = listOfUniversity[i][1]   # that will be university name and department.
        start = alltext.index("University") + 11 # we will determine index which comes before the department names.
        department = alltext[start:]  # and it will assign as str.
        if department not in departmentLst: # Also it will check the list if there is same department name. if there is, it will not append the list again.
            departmentLst.append(department) 
    return departmentLst

import os

YorN = "Y"
while YorN.upper() == "Y":   # If it press (y). User can access menu how many times it wants.
    os.system("cls") # it will clear the terminal.
    print("""–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1-)Search for a student with a given ID and display his/her name and last name.
2-)List the university/universities and departments with a maximum base points.
3-)Create a file named 'result.txt' for each student.
4-)List the students information sorted by their score.
5-)List the students placed in every university/department.
6-)List the students who were not be able to placed anywhere.
7-)List all the departments
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––""")
    recordingsOfKey = readFile("key.txt")              # There are recordings of all texts.
    recordingofanswers = readFile("answers.txt")
    recordingsOfUniversity = readFile("university.txt")
    recordingOfStudents = readFile("Student.txt")
    #********************************************************
    lststudent = listToStudentObject(recordingOfStudents) # Also there are all lists that we will use.
    lstofuni = listOfUniversity(recordingsOfUniversity)
    lstofanswers = listOfAnswers(recordingofanswers)

    whichOption = int(input("What do you want to access: ")) # User can access any option what it wants
    if (whichOption < 1) or (whichOption > 7):
        print("You can only enter numbers 1-7.")
    print()

# For each operation in menu there are conditions.
    if whichOption == 1:
        studentID = input("Enter the number of the student you want to find: ")        
        try:
            for i in findStudent(lststudent, studentID):
                print(i,end=" ")
        except:
            print("Student could not found!")

    elif whichOption == 2:        
        maxpointuni = findMaxBasePointUni(lstofuni) # finding the max point university or universities.
        for uni in maxpointuni:
            print(uni)

    elif whichOption == 3:
        resultFile = open("results.txt","w",encoding="utf8")
        for answer in lstofanswers: # Here the information from two different text files is combined. and two previously written functions are used.
            answer.name = findStudent(lststudent, answer.getID())[0] # it finds the name of student.
            answer.lastname = findStudent(lststudent, answer.getID())[1] # it finds the last name of student.
            answer.choice1 = findUni(lstofuni, answer.choice1) # it finds the name of university from university number.
            answer.choice2 = findUni(lstofuni, answer.choice2) 
            record = str(answer.getID()) + " " + answer.name + " " + answer.lastname + " " + answer.bookType + " " + str(answer.findCorrect(recordingsOfKey)) + " " + str(answer.findFalse(recordingsOfKey)) + " " + str(answer.findBlank(recordingsOfKey))+ " " +str((answer.calculateScore(recordingsOfKey)//15))+ " " +str(answer.calculateScore(recordingsOfKey))+ " " + str(answer.choice1) + " " + str(answer.choice2 + "\n")
            resultFile.write(record) # it writes to the result.txt.
        resultFile.close()
        print("results.txt was created!") # information about created text.

    elif whichOption == 4:
        allInfoAboutStudent = []
        for answer in lstofanswers: # that combines two different txt to create one student object.
            answer.name = findStudent(lststudent, answer.getID())[0] # it finds the name of student.
            answer.lastname = findStudent(lststudent, answer.getID())[1] # it finds the last name of student.
            answer.choice1 = findUni(lstofuni, answer.choice1) # it finds the name of university from university number.
            answer.choice2 = findUni(lstofuni, answer.choice2)
            allInfoAboutStudent.append(answer) 
        sortedStudent = sortStudent(allInfoAboutStudent) # ranks students according to their score.
        for i in sortedStudent:
            i.displaySorted(recordingsOfKey) # method was used to print info about sorted student.

    elif whichOption == 5:
        studentsToSettle = []
        for answer in lstofanswers: # that combines two different txt 
            answer.name = findStudent(lststudent, answer.getID())[0] # it finds the name of student.
            answer.lastname = findStudent(lststudent, answer.getID())[1] # it finds the last name of student.
            studentsToSettle.append(answer)

        sortedStudent = sortStudent(studentsToSettle) # ranks students according to their score.
        lstPlacedandNonPlaced = placedStudent(sortedStudent, lstofuni) # it places students.

        # Yerleştirilen öğrenciler
        for i in lstPlacedandNonPlaced[0]: # It prints out every student placed.
            print(i)

    elif whichOption == 6:
        studentsToSettle = []
        for answer in lstofanswers:
            answer.name = findStudent(lststudent, answer.getID())[0] # it finds the name of student.
            answer.lastname = findStudent(lststudent, answer.getID())[1] # it finds the last name of student.
            studentsToSettle.append(answer)

        sortedStudent = sortStudent(studentsToSettle) # ranks students according to their score.
        lstPlacedandNonPlaced = placedStudent(sortedStudent, lstofuni) # it places students.

        #6)Yerleşemeyen öğrenciler
        for j in lstPlacedandNonPlaced[1]: # It prints out every student non-placed.
            print(j)

    elif whichOption == 7:
        departmentlst = listAllDepartments(lstofuni)
        for department in departmentlst: # it will print the unique departments.
            print(department)

    print()
    print()
    YorN = input("Do you want to continue yes(Y) or no(N): ") 

print("Thanks for using the program.")