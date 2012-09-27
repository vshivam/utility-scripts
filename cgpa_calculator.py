def grade(grd):
    if(grd == "a" or grd =="A"):
        return 10
    if(grd == "a-" or grd =="A-"):
        return 9
    if(grd == "b" or grd =="B"):
        return 8
    if(grd == "b-" or grd =="B-"):
        return 7
    if(grd == "c" or grd =="C"):
        return 6
    if(grd == "c-" or grd =="C-"):
        return 5
    if(grd == "d" or grd =="D"):
        return 4
    if(grd == "e" or grd =="E"):
        return 2

units_completed = int(raw_input("Units Completed ?"))
print units_completed
current_cgpa = float(raw_input("Current Cgpa ?"))
print current_cgpa
num_courses = int(raw_input("Enter Number of courses to Add"))
print ("units_completed*current_cgpa = "+ str(units_completed*current_cgpa))
total_units = 0
total_credits = 0
for i in range(0,num_courses):
    unit = int(raw_input("Number of Units"))
    print unit
    grade_1 = (grade(raw_input("Enter Grade  A or A- or B or B- or C or C- or D or E")))
    print grade_1
    total_units = (total_units) + (unit*grade_1)
    total_credits = total_credits + unit

print total_units
print total_credits
print ("Completed Units = %s") %  (total_credits + units_completed)
print ("Credits Accumulated = %s") % ( units_completed*current_cgpa+total_units)
print (" CGPA = %s") % ((units_completed*current_cgpa+total_units)/(total_credits + units_completed))


