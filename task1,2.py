'''
#spreadsheet
from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://wwww.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('python-upworkcombination.json', scope)
client = gspread.authorize(creds)

python_upworKcombination = client.open("Python upworKcombination").worksheet("sheet-0")
python_upworKcombination.update_acell(1,1, "hello")
'''

###task1
print('Task 1 : Start')
import itertools
import random

randomlist = []
for i in range(0,10):
    n = random.randint(1,10)
    randomlist.append(n)
print('initial list of numbers :', randomlist)
print('--------------------------------------------------------------------------------------------------------------')

#Create combinations of 5
com = list(itertools.combinations(randomlist, 5))
unq = set(com)
final_list=[]
#order
for single_list in unq:
    single_list = list(single_list)
    single_list.sort()
    final_list.append(single_list)

print('All Possible Combinations of 5 numbers, in ascending order without repetition are :')
for single_list in final_list:
    print(single_list)

print('Task 1 : end')
print('--------------------------------------------------------------------------------------------------------------')


###task2
print('Task 2 : Start')
print('initial list of numbers :', randomlist)
print('--------------------------------------------------------------------------------------------------------------')
#Create combinations of 6
com = list(itertools.combinations(randomlist, 6))
unq = set(com)
final_list=[]
#order
for single_list in unq:
    single_list = list(single_list)
    single_list.sort()
    final_list.append(single_list)

print('All Possible Combinations of 6 numbers, in ascending order without repetition are :')
for single_list in final_list:
    print(single_list)

print('Task 2 : end')
print('--------------------------------------------------------------------------------------------------------------')
