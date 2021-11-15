
from array import array
import csv
from csv import DictReader

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
    


def main():
    csv_file()
    

main()


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
    print(data, , file=open("assignment2_file.txt", "a"))
 
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
print(merge_sort , , file=open("assignment2_file.txt", "a"))

merge_sort()


#This is the Quick sort for the list 
def quicksort(list1, start=0, end=None):
