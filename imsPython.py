import random
from js import document, Element
from pyodide import create_proxy

passwords = ['winter1', 'fall1', 'summer1', 'spring1', 'temp1','winter','fall123','summer','spring','temp123','learn123']
selected_password = random.choice(passwords)

a = """Good afternoon,
Good morning,
 
To support you with your log-in challenge, please open the following link in Google Chrome for a successful log in: http://bit.ly/lms-mmc
Log in with the same Montefiore username and password that you use to login to your Outlook email and computer. 

Our system is case sensitive, so please be mindful of this when typing in the information. Please let us know if you are still unable to log in after trying this suggestion.

"""

apologies = []

c = """Hello\n  
Please open the following link in Google Chrome for a successful log in:
Your username (case sensitive) is:
Please let us know if you are still unable to log in after trying this suggestion.\n\nThank you.
"""
c2 = """Hello,\n
We are happy to assist you in logging in. 
Please open the following link in Google Chrome for a successful log in: {}
Your username (case sensitive) is: 
Your temporary password (case sensitive) is: {}

You can reset your password upon successful log-in to your account. 
Please do not hesitate to reach out if you are still experiencing issues.
\nThank you."""
    #-------List for storing all links ------------
testlist=[
"http://bit.ly/lms-mmc",
"http://bit.ly/lms-bahn",
"http://bit.ly/lms-student",
"http://bit.ly/lms-contractors",  
"http://bit.ly/lms-einstein",
"https://montefiore.plateau.com/learning/user/portal.do?siteID=EPIC&landingPage=login",
"http://bit.ly/lms-house", 
"https://montefiore.plateau.com/learning/user/portal.do?siteID=MEDTEST&landingPage=login",
"http://bit.ly/lms-mnr",
"http://bit.ly/lms-mvh",
"https://bit.ly/nyack-lms",
"http://bit.ly/lms-nurses",
"http://bit.ly/lms-osha",
"https://montefiore.plateau.com/learning/user/portal.do?siteID=SLC&landingPage=login",
"http://bit.ly/lms-voluntary",
"http://bit.ly/lms-volunteer1",
"http://bit.ly/lms-volunteer2",
"http://bit.ly/lms-whp",
"http://bit.ly/admin-pwd",
"http://bit.ly/lms-Burke ",
"http://bit.ly/lms_meac",
"http://bit.ly/admin-pwd",
"http://bit.ly/lms-nao",
"https://montefiore.plateau.com/learning/user/portal.do?siteID=Nursing%20Exams&landingPage=login"
]

def clr(event):
    prepbox = document.getElementById("prepbox")
    prepbox.value = ""
Clear = document.getElementById("Clear")
Clear.addEventListener("click",create_proxy(clr))

def p(event):
    selected_password = random.choice(passwords)
    prepbox = document.getElementById("prepbox")
    prepbox.value = selected_password
Psw = document.getElementById("Psw")
Psw.addEventListener("click",create_proxy(p))

def for_Corp(event):
    prepbox = document.getElementById("prepbox")
    prepbox.value = a
Corp = document.getElementById("Corp")
Corp.addEventListener("click",create_proxy(for_Corp))

def on_click(event):
    prepbox = document.getElementById("prepbox")
    prepbox.value = c
BAHN = document.getElementById("BAHN")
BAHN.addEventListener("click",create_proxy(on_click))

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[1],selected_password)
BAHN = document.getElementById("BAHN")
BAHN.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[2],selected_password)
ClinStudent = document.getElementById("ClinStudent")
ClinStudent.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[3],selected_password)
Contractors = document.getElementById("Contractors")
Contractors.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[4],selected_password)
Einstein = document.getElementById("Einstein")
Einstein.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event): 
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[5],selected_password)
Epic = document.getElementById("Epic")
Epic.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[6],selected_password)
HouseStaff = document.getElementById("HouseStaff")
HouseStaff.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[7],selected_password)
MedTest = document.getElementById("HouseStaff")
MedTest.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[8],selected_password)
MNR = document.getElementById("MNR")
MNR.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[9],selected_password)
MVH = document.getElementById("MVH")
MVH.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[10],selected_password)
NYACK = document.getElementById("NYACK")
NYACK.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    selected_password = random.choice(passwords) 
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[11],selected_password)
Nursing = document.getElementById("Nursing")
Nursing.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[13],selected_password)
SLC= document.getElementById("SLC")
SLC.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[17],selected_password)
WHP= document.getElementById("WHP")
WHP.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[16],selected_password)
Volunteer2= document.getElementById("Volunteer2")
Volunteer2.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[12],selected_password)
Osha= document.getElementById("Osha")
Osha.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[14],selected_password)
Voluntary= document.getElementById("Voluntary")
Voluntary.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[20],selected_password)
MEAC = document.getElementById("MEAC")
MEAC.addEventListener("dblclick",create_proxy(on_click2))

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[21],selected_password)
ADMIN = document.getElementById("ADMIN")
ADMIN.addEventListener("dblclick",create_proxy(on_click2))  

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[22],selected_password)
NAO = document.getElementById("NAO")
NAO.addEventListener("dblclick",create_proxy(on_click2)) 

def on_click2(event):
    selected_password = random.choice(passwords)
    p(event)
    prepbox = document.getElementById("prepbox")
    prepbox.value = c2.format(testlist[23],selected_password)
NursingExams = document.getElementById("NursingExams")
NursingExams.addEventListener("dblclick",create_proxy(on_click2)) 


