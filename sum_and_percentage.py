#Python Assignment2

# WAP to create a DS of students (define DS as per the protocols) and print the sum of scores in five subjects and gets the each student percentage.

students = [
            {"RollNo":1, "Name":"Anil", "Sub1":50,"Sub2":50,"Sub3":50,"Sub4":50,"Sub5":50},
            {"RollNo":2, "Name":"Balwant", "Sub1":50,"Sub2":40,"Sub3":48,"Sub4":77,"Sub5":89},
            {"RollNo":3, "Name":"Chandrashekhar", "Sub1":52,"Sub2":64,"Sub3":66,"Sub4":78,"Sub5":42}
            ]
print students

for student in students:
    
    
    total= sum([student['Sub1'],student['Sub2'],student['Sub3'],student['Sub4'],student['Sub5']])
    percentage= total/5

    print "**"*50
    print student

    print " {} got total score  {} and his percentage is {}".format(student["Name"],total, percentage)
                                                                   
raw_input()
