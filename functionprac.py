def student(captain,*other_student):
    print('Captain: ',captain)
    for student in other_student:
        print("Other student {parm}".format(parm=student))
student('Protick','Tanvir','Rabby')