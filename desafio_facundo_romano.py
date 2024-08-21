import random

SUBJECTS = ['Algebra', 'Fisica', 'Quimica', 'Programacion']
STUDENTS = ['Santi', 'Mati', 'Facu', 'Agus']

def generate_matrix(subjects, students):
    """
        Generates a matrix of subjects, students, and their grades.

        Args:
            subjects (List[str]): List of subject names.
            students (List[str]): List of student names.

        Returns:
            List[List[Union[str, int]]]: A matrix where each row represents a subject and contains
            student names and grades. Elements can be either strings (student names) or integers (grades).
    """

    matrix = [['Student'] + subjects]

    for student in students:
        scores = []

        for _ in subjects:
            scores.append(random.randint(0, 10))
        

        matrix.append([student] + scores)
    
    return matrix

def getStudentAverage(student):
    gradesAcum = 0

    for studentRow in MATRIX:
        if (studentRow[0] == student):
            totalSubjects = len(studentRow) - 1
            for grade in studentRow:
                if isinstance(grade, int):
                    gradesAcum += grade

    average = gradesAcum/totalSubjects

    return average

def getStudentsAverages():
    averages = []
    for student in STUDENTS:
        averages.append([student, getStudentAverage(student)])

    return averages

def getSubjectAverage(subject_position):
    grades_sum = 0
    students_total = 0

    for student in MATRIX:
        if student[0] == 'Student': continue 

        grades_sum += student[subject_position]
        students_total += 1
    
    return grades_sum/students_total

def getSubjectsAverages():
    averages = []

    for subject in SUBJECTS:
        subject_position = MATRIX[0].index(subject)
        average = getSubjectAverage(subject_position)

        averages.append([MATRIX[0][subject_position], average])

    return averages

MATRIX = generate_matrix(SUBJECTS, STUDENTS)
averages_by_student = getStudentsAverages()
averages_by_subject = getSubjectsAverages()
print(MATRIX)
print(averages_by_student)
print(averages_by_subject)



