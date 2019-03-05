#!/home/shah/yes/bin/python

print("Content-Type: text/HTML")
print()

print("<h1>This is our coding page\n\n</h1><br><br>")
print("<h2>This page will be maintained by <mark>Shahrukh Afzal</mark></h2>")


print("<br><br>")
import pandas as pd
import cgi

form = cgi.FieldStorage()
url = form.getvalue("url")
data = pd.read_html(url)




def personal_data(arg):
    course = arg[2][2][2]
    name = arg[2][2][4]
    roll_no = arg[2][2][3]
    branch = arg[2][5][2]
    college = arg[2][2][1]
    gender = arg[2][5][5]
    return roll_no, name, branch, gender, course, college


def sem_data(arg):
    a = []
    for i in range(8, len(arg), 7):
        a.append(arg[i])

    for j in range(11, len(arg), 7):
        a.append(arg[j])
    return a




def final_sem(raw_sem):
    z=[]
    sem1 = 0
    sem2 = 0
    sem3 = 0
    sem4 = 0
    sem5 = 0
    sem6 = 0
    sem7 = 0
    sem8 = 0
    for j in range(0, len(raw_sem)-1):
        if ((raw_sem[j][0][7][3]) == '1'):
            sem1 = (raw_sem[j])
        elif ((raw_sem[j][0][7][3]) == '2'):
            sem2 = (raw_sem[j])
        elif ((raw_sem[j][0][7][3]) == '3'):
            sem3 = (raw_sem[j])
        elif ((raw_sem[j][0][7][3]) == '4'):
            sem4 = (raw_sem[j])
        elif ((raw_sem[j][0][7][3]) == '5'):
            sem5 = (raw_sem[j])
        elif ((raw_sem[j][0][7][3]) == '6'):
            sem6 = (raw_sem[j])
        elif ((raw_sem[j][0][7][3]) == '7'):
            sem7 = (raw_sem[j])
        elif ((raw_sem[j][0][7][3]) == '8'):
            sem8 = (raw_sem[j])
    #return sem1, sem2, sem3, sem4, sem5, sem6, sem7, sem8
    z.append(sem1)
    z.append(sem2)
    z.append(sem3)
    z.append(sem4)
    z.append(sem5)
    z.append(sem6)
    z.append(sem7)
    z.append(sem8)
    return z

#print("Wait!!! Data is being loaded\n\n")
def na_fill(args):
    for each in args:
        each.fillna(value=0, inplace=True)
    return args


def header(arg):
    i=[]
    for each in arg:
        try:
            each.columns = each.iloc[0]
            each=each[1:]
            i.append(each)
        except:
            pass
    return i  

#print("Wait!!! Data is also being loaded\n\n")
roll_no, name, branch, gender, course, college = personal_data(data)

#sem1, sem2, sem3, sem4, sem5, sem6, sem7, sem8 = final_sem(na_fill(sem_data(data)))
'''
all_sem_list=[]
all_sem_list.append(sem1)
all_sem_list.append(sem2)
all_sem_list.append(sem3)
all_sem_list.append(sem4)
all_sem_list.append(sem5)
all_sem_list.append(sem6)
all_sem_list.append(sem7)
all_sem_list.append(sem8)
'''
#print("Wait!!! Data is being loaded\n\n")
print("<br><br>")
print("<br><br>")
print("<br><br>")
print("<br><br>")
print("<mark>", name, "</mark>", " whose roll_no is ", "<mark>", roll_no, "</mark>", " is studying ", course, " ", "<mark>", branch, "</mark>", " in ",  college, " college<br><br> ")


#def view_back(final)

view_back = lambda sem:sem[sem['Grade' or 'Credit']=='F'] #((sem[sem['Credit']=='F']) or (sem[sem['Grade']=='F']) or (sem[sem['Credit']=='0']))


p = final_sem(na_fill(sem_data(data)))
q = header(p)
print(view_back(q[2]))
print(q[0])
print("<br><br>")
print("<br><br>")
try:
    print("Back in semester  <b>1</b>  : \n\n")
    print(view_back(q[0])['Name'])
except:
    pass   

print("<br><br>")
try:
    print("Back in semester  <b>2</b>  : \n\n")
    print(view_back(q[1])['Name'])
except:
    pass  
print("<br><br>")
try:
    print("Back in semester  <b>3</b>  : \n\n")
    print(view_back(q[2])['Name'])
except:
    pass  
print("<br><br>")
try:
    print("Back in semester  <b>4</b>  : \n\n")
    print(view_back(q[3])['Name'])
except:
    pass  
print("<br><br>")
try:
    print("Back in semester  <b>5</b>  : \n\n")
    print(view_back(q[4])['Name'])
except:
    pass  
print("<br><br>")
try:
    print("Back in semester  <b>6</b>  : \n\n")
    print(view_back(q[5])['Name'])
except:
    pass  

print("<br><br>")
try:
    print("Back in semester  <b>7</b>  : \n\n")
    print(view_back(q[6])['Name'])
except:
    pass  
print("<br><br>")
try:
    print("Back in semester  <b>8</b>  : \n\n")
    print(view_back(q[7])['Name'])
except:
    pass  
print("<br><br>")
print("<br><br>")


'''
sem1_back=view_back(sem1)
sem2_back=view_back(sem2)
sem3_back=view_back(sem3)
sem4_back=view_back(sem4)
sem5_back=view_back(sem5)
sem6_back=view_back(sem6)
sem7_back=view_back(sem7)
sem8_back=view_back(sem8)
'''

print("""
<table cellspacing="0" rules="all" border="1" id="ctl04_ctl00_ctl00_grdViewSubjectMarksheet" style="border-collapse:collapse;width: 100%; font-family: Verdana; font-size: 8pt;">
<tbody>
                        <tr>
							<th scope="col">Code</th><th scope="col">Name</th><th scope="col">Type</th><th scope="col">Internal</th><th scope="col">External</th><th scope="col">Back Paper</th><th scope="col">Credit</th>
						</tr>
                        <tr>
                        </tr>



"""
)

#print(view_back(q[1]).columns)

print("""

<tr>
<td>NOE-1</td>
<td>Maths-2</td>
<td>Theory</td>
<td>30</td>
<td>12</td>
<td>--</td>
<td>0</td>

</tr>
<tr>
<td>
</td>

</table>
""")


print("<br><br>")

#print("{} got back in{}".format(name,sem1_back))

print("<br><br><a href='home.html'>Home</a><br><br>")

print("<br><br><a href='enter_url.html'>Another Result</a>")
