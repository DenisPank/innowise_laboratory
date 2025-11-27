class StudentListCorrect:           # A class that defines the functionality for the application
    def __init__(self):
        self.list_students = []     # Student list initialization function

    def addStudent(self, name: str = None) -> bool:
        self.list_students.append({         # Сreating an empty dict for the student
            "name": name,
            "list_estimate": [],
        })
        return True
    
    def showListStudents(self):         # output of the minimum average of the student's grades, 
                                        # the maximum average of the student's grades, as well as the output of the average of grades
        maxAverage = 0
        minAverage = 0
        overallAverageList = []
        for student in self.list_students:
            try:
                average = sum(student["list_estimate"]) / len(student["list_estimate"])
                if maxAverage < average : maxAverage = average
                if minAverage > average or minAverage == 0 : minAverage = average
                overallAverageList.append(student["list_estimate"])
                print(f"{student['name']}'s average grade is {average}")
            except ZeroDivisionError: 
                print(f"{student['name']}'s average grade is N/A")
        overallAverageList = sum(overallAverageList, [])
        overallAverage = sum(overallAverageList)/len(overallAverageList)
        print("--------------------------")
        print(f"Max average: {round(maxAverage, 1)}")
        print(f"Min average: {round(minAverage, 1)}")
        print(f"Overall average: {round(overallAverage, 1)}")
        return True
   
    def addEstimateStudent(self, name: str, grades: float): #Adding an array of scores to the key value "list_estimate" in the dictionary "list_students"
        for student in self.list_students:
            if student["name"] == name:
                student["list_estimate"].append(grades)
        return True

    def getTheTopStudent(self): # Determining the best student by grades
        topStudent = max(self.list_students, key = lambda x: sum(x["list_estimate"]) / len(x["list_estimate"]) if len(x["list_estimate"]) != 0 else 0 )
        return f"The student with the hights average is {topStudent["name"]} with a grade of {sum(topStudent["list_estimate"])/len(topStudent["list_estimate"])}"
        


student1 = StudentListCorrect() # creating an instance of the class

def menu(): # A function for managing work with the student assessment database
    option = ["Add a new student","Add a grades for a student","Show report (all students)","find top performer","Exit"]
    while True:
        print("--- Student Grade Analyzer ---")
        for index, opt in enumerate(option):
            print(f"{index + 1}: {opt}")
        choice = input("Enter your choice: ")
        if choice == "1":
            while True:
                name = input("Enter name: ")
                if name == "":
                    print("The student must have a name!")
                else:
                    student1.addStudent(name)
                    break
        if choice == "2":
            nameStudent = input("Enter name: ")
            while True:
              gradesStudent = input("Enter grades (or 'done' to finish): ")
              if gradesStudent.lower() == "done":
                  break
              try:
                student1.addEstimateStudent(nameStudent, float(gradesStudent))
              except ValueError:
                print("Enter a number!!!")
        if choice == "3":
            print("--- Student report ---")
            print(student1.showListStudents())
        if choice == "4":
            print(student1.getTheTopStudent())
        if choice == "5":
            print("Exiting program.")
            break

menu()