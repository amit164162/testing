student={}
for x in range(3):
    name=input('enter student name')
    m=[]
for y in range(3):
     marks=(int)(input('enter marks'))
        m=m.append(marks)
        student[name]=m  
for n,m in student.items():
    print('name:',n,end='\t')
    total=sum(m)
    per=total/len(m)
    if per>=60:
        print('division first')
    elif per>=45 and per<60:
        print('division:second')
else:
    print('division:third')                