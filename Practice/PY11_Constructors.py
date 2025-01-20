# class Studants():
#     name = "mihir"
#     def __init__(self, name , marks, rollno):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks


# s1 = Studants("uday", 98, 11)   
# print(s1.name, s1.rollno, s1.marks)


# class Studant():

#     def __init__(self , name, m1,m2,m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def AVG(self):
#         avg = (self.m1+self.m2+self.m3)/3
#         print("hii", self.name ,"your Average Score is :", avg)
#         # return (self.m1+self.m2+self.m3)/3
    

# s1 = Studant("mihir", 10,20,40)
# print(s1.name, s1.m1, s1.m2, s1.m3)

# s1.AVG()



class Bank_Account():
    def __init__(self, bal, Acc_no):
        self.bal = bal
        self.Acc_no = Acc_no

    def debit(self , Amount):
        self.bal -= Amount
        print("RS", Amount, "was debited",self.bal)

    def credit(self , Amount):
        self.bal += Amount
        print("RS", Amount, "was credited", self.bal)
    
    def Get_balnces(self):
        return self.bal
    

acc1 = Bank_Account(50000, 12442312)
acc1.debit(10000)
acc1.credit(1000)

print(acc1.Get_balnces())