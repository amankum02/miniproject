#create dictionary of 5 employee
emp={
    101:{'Name':'Aman', 'Age':23, 'Department':'Developer'},
    102:{'Name':'Pawan', 'Age':24, 'Department':'Developer'},
    103:{'Name':'Abhishek', 'Age':21, 'Department':'Design'},
    104:{'Name':'Akash', 'Age':23, 'Department':'Testing'},
    105:{'Name':'Amar', 'Age':25, 'Department':'Testing'}
}
avg=0
#print all the employee
for i,j in emp.items():
    print(f"{i}: {j}",end='\n')
    avg+=emp[i]['Age']
#print the average of age
print(f"Average Of ages:  {avg/len(emp):.2f}")
print('-----------------------------------------------------')


#add a new employee in dictionary
emp[106]={'Name':'Amar Deep', 'Age':22, 'Department':'Developer'}
for i,j in emp.items():
    print(f"{i}: {j}",end='\n')
    avg+=emp[i]['Age']
#print the average of age
print(f"Average Of ages:  {avg/len(emp):.2f}")
print('-----------------------------------------------------')

#rremove one element from dictionary
emp.pop(103)

for i,j in emp.items():
    print(f"{i}: {j}",end='\n')
    avg+=emp[i]['Age']
#print the average of age
print(f"Average Of ages:  {avg/len(emp):.2f}")