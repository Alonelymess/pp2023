def input_student():

    #Student info
    n_students = int(input("Input number of students: "))
    list_students = [{'Name': None, 'DoB': None, 'ID': None} for i in range(n_students)] #Save student list
    for i in range(0, n_students):
        print("Student " + str(i+1))
        
        list_students[i]['Name'] = input("Input student name: ")
        list_students[i]['DoB'] = input("Input student DoB: ")
        list_students[i]['ID'] = input("Input student id: ")
        print(list_students[0])
        print("\n")

    return list_students


def input_course():
    list_students = input_student()
    
    #Courses info
    cours_num = int(input("Input number of courses: "))
    list_courses = [{'ID': None, 
                     'Name': None, 
                     'Marks of students': [{'Score': None, 
                                            'Student name': None, 
                                            'Student ID': None}
                                            for i in range(len(list_students))]} 
                                                                                for i in range(cours_num)]
    for i in range(0, cours_num):
        list_courses[i]['ID'] = input("Input course " + str(i+1) + " ID: ")
        list_courses[i]['Name'] = input("Input course " + str(i+1) + "name: ")
        print("Input marks of students: ")
        for j in range(len(list_students)):
            list_courses[i]['Marks of students'][j]['Score'] = input("\t Input score for " + list_students[j]['Name'] 
                                                                     + " " + list_students[j]['ID'] + ": " )
            list_courses[i]['Marks of students'][j]['Student name'] = list_students[j]['Name']
            list_courses[i]['Marks of students'][j]['Student ID'] = list_students[j]['ID']

    return list_courses

def show_courses(list_courses):
    course_ID = input("Enter course ID: ")
    for k in range(len(list_courses)):
        if list_courses[k]['ID'] == course_ID:
            print("\n" + list_courses[k]['Name'] + " " + list_courses[k]['ID'])
            print('Marks of students: ')

            for j in range(len(list_courses[k]['Marks of students'])):
                print('\t' + "Name: " + list_courses[k]['Marks of students'][j]['Student name'])
                print('\t' + "ID: " + list_courses[k]['Marks of students'][j]['Student ID'])
                print('\t' + "Score: " + list_courses[k]['Marks of students'][j]['Score'])
                print('\n')
    

#Init data
while True:
    list_courses = input_course()
    while True:
        show_courses(list_courses)
        if input("Do you want to continue searching? (Y/N): ") == 'N':
            break
    if input("Do you want to redo? (Y/N): ") == 'N':
            break


    


