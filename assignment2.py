
from array import array
import csv
from csv import DictReader
#[Q1.a]
def csv_file():

    #This is for the lists
    with open ('assignment2_file.csv', mode='r')as csvfile:  #mode=r is for reading the file
        csvreader = csv.reader(csvfile)                      #open the csv file into the module 
        list1 = list(csvreader)
        print(list1 , file=open("assignment2_file.txt", "a"))
    


    #This is for the tuple 
    with open ('assignment2_file.csv', mode='r')as csvfile:
        csvreader = csv.reader(csvfile)
        tuple1 = list(map(tuple, csvreader))
        print(tuple1 ,file=open("assignment2_file.txt", "a"))

    #This is for the dictionary 
    with open ('assignment2_file.csv', 'r')as csvfile: 
        csvreader = csv.reader(csvfile)
        dictionary1 = DictReader(csvreader)
        list_of_dict = list(csvreader)
        print(list_of_dict, file=open("assignment2_file.txt", "a"))



        
    #This is for set    
    with open ('assignment2_file.csv', 'r')as csvfile:  
        csvreader = csv.reader(csvfile)
        set1 = list(map(set,csvreader))
        print(set1 , file=open("assignment2_file.txt", "a")) 



#This is for array

    items_1 = []

    with open ('assignment2_file.csv', 'r')as csvfile: 
        csvreader = csv.reader(csvfile)
        array1 = list(csvreader)
        for row in csvreader:
            items_1.append[0]
        print(array1 , file=open("assignment2_file.txt", "a"))
    
#Q1.b
    print(array1,'\n',tuple1,'\n',list1,'\n',set1,'\n',dict1)

    with open('assignment2_file.txt','w') as file1:
        data=str(dict1)+'\n'+str(list1)+'\n'+str(tuple1)+'\n'+str(array1)
        file1.write(data)

    print("\n")

#Q1.c
if 'Fujairah' in list1 and 'brown' in set1 and 'Data Science' in dictionary1:
    print("Yes, Found them!!\n 'Fujairah' in list1,\n 'brown' in set1 and \n 'Data Science' in dict1")
else:
    print("None")

print("\n")




    

def main():
    csv_file()

main()






#Q2
#This is the insertion sort for the array
def insertion_sort(array1):
    for i in range(1 , len(array1)):
        key = array1[i]
        j = i - 1

        while j >= 0 and key < array1[j]:
            array1[j + 1] = array1[j]
        j = j - 1 

        array1[j + 1] = key 
    data = [120,20,100,10,40,30,50,45,70,60]
    insertion_sort(data)
    print("sorted array in ascending order")
    print(data,  file=open("assignment2_file.txt", "a"))
 
    insertion_sort()


#this is the merge sort for the tuple

def merge_sort(tuple1):
    if len(tuple1) <= 1:
        return tuple1
    mid = len(tuple1) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(tuple1[:mid]), merge_sort(tuple1[mid:])

    # Merge each side together
    return merge_sort(left, right, tuple1.copy())
print(merge_sort , file=open("assignment2_file.txt", "a"))

merge_sort()


#This is the Quick sort for the list 
def quick_sort(sequence):
    length = len(sequence)
    if length < 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item >pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

quick_sort(list1)


#This is the quick sort for set1
quick_sort(set1)


ndict1={}
for i in sorted(dict1):
    temp=dict1[i]
    ndict1[i]=temp
dict1=ndict1



#appending

with open('assignment2_file.txt','w') as fileC:
    data= str(array1)+'\n'+str(tuple1)+'\n'+str(list1)+'\n'+str(set1)+'\n'+str(dict1)
    fileC.write(data)


#printing 

con=[]
with open('assignment2_file.txt','r') as file4:
    for line in file4:
        con.append(line.rstrip())
        for x in con:
            print(x)

print("\n")

#Q3

with open('assignment2_file2.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    for x in con:
        temp=[]
        temp.append(x)
        writer.writerow(temp)