import csv
class Physician: #This is physician class
    __slots__ = ['__id', '__name', '__specialty'] # the underscore is to make it pvt
    def __init__(self , id , name , specialty):
        self.__id = id
        self.__name = name
        self.__specialty = specialty

    def get_id(self):           #These are the accessors and mutators for the class physician
           return self.__id

    def get_name(self):
           return self.__name

    def get_specialty(self):
           return self.__specialty

    def set_specialty(self, specialty):
            self.__specialty

    def set_id(self , id):
            self.__id

    def set_name(self , name):
            self.__name

    def __str__(self): #this is the special method str
            return f" The physician's name is {self.__name} and his id number is {self.__id}. He specializes in {self.__specialty}"

    def __repr__(self): #this is the special method repr
            return repr(self.__name , self.__name , self.__specialty) 



class Patient: #this is the patient class
    __slots__ = ['__emr_id' , '__name', '__gender' , '__phone_number']
    def __init__(self , emr_id , name , gender , phone_number):
        self.__emr_id = emr_id 
        self.__name = name 
        self.__gender = gender 
        self.__phone_number = phone_number

    def get_emr_id(self):
        return self.__emr_id    #These are the accessors and mutators for the class patient

    def get_name(self):
        return self.__name      #get is the accessor and set is the mutator

    def get_gender(self):
        return self.__gender

    def get_phone_number(self):
        return self.__phone_number

    def set_emr_id(self, emr_id):
        self.__emr_id

    def set_name(self , name):
        self.__name

    def set_gender(self, gender):
        self.__gender

    def __repr__(self):         #this is the special method repr
        return f'Patient(id={self.__emr_id},name={self.__name},gender={self.__gender},phone_number={self.__phone_number}'

        



class Encounter: #This is the encounter class 
    def __init__(self , physician , patient , date , disease , medication ):
        self.physician = physician
        self.patient = patient 
        self.date = date 
        self.disease = disease 
        self.medication = medication
        
    def __repr__(self):         #this is the special method repr
        return f'Encounter(Patient={self.patient},Physician={self.physician},Date={self.date},Disease={self.disease},Medication={self.medication}'

obj_a=[] #This is a list to store the objects of class physicians
with open('physicians.csv' ,'r') as q:
    for row in q:
        strp = row.strip().split(",")
obj_a.append(Physician(strp[0],strp[1],strp[2])) #for all row in physicians.csv will create an object for Physician and append it to obj_a list
        

obj_b=[] #This is a list to store the objects of class patients
with open('patients.csv','r') as z:
    for row in z:
        strp = row.strip().split(",")
obj_b.append(Patient(strp[0],strp[1],strp[2],strp[3])) #for all row in patients.csv will create an object for patients and append it to obj_b list

obj_c=[] ##This is a list to store the objects of class Encounter
obj_c.append(Encounter(3,4,'21-5-2021','dis1','med1')) 
obj_c.append(Encounter(5,9,'16-6-2021','dis2','med2'))
obj_c.append(Encounter(1,3,'14-9-2021','dis3','med3'))
obj_c.append(Encounter(4,6,'9-2-2021','dis4' ,'med4'))
obj_c.append(Encounter(2,8,'29-8-2021','dis5','med5'))



for l in obj_a: #Now we need to print everything
    print(str(l))
for l in obj_b:
    print(repr(l))
for l in obj_c:
    print(repr(l))
with open('encounter.csv', 'w') as f: #This will write it into a new csv file called encounter
    writer = csv.writer(f)

    for item in obj_c:
        writer.writerow([item.patient,item.physician,item.date,item.disease,item.medication])
