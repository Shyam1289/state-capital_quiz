#program to play an indian state 
#and it's capital quiz
from time import sleep as s
print('Wanna check your state-capital quotient?')
s(1)
print("Here,I have a quiz of Indian state and it's capital for you.")
s(2)
print('But before we start, I think you should be well aware of the rules and regulations that govern the quiz.')
s(3)
print('So,here are the rules\n(1).The quiz comprises of 5 sets and each set has further 5 questions.')
s(3)
print('(2). For every correct answer you will be awarded 2 marks.  whereas for every incorrect answer 1 mark will be deducted.')
s(4)
print('(3).In case,if you feel that any question has wrong answer  then  you may cross check it from the given website:-\nhttps://en.m.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India')
s(4)
stlist=['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujrat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
caplist=['Port Blair','Visakhapatnam','Itanagar','Dispur','Patna','Chandigarh','Raipur','Daman','New Delhi','Panaji','Gandhinagar','Chandigarh','Shimla','Srinagar','Ranchi','Bengaluru','Thiruvananthapuram','Leh','Kavaratti','Bhopal','Mumbai','Imphal','Shillong','Aizawl','Kohima','Bhubaneswar','Pondicherry','Chandigarh','Jaipur','Gangtok','Chennai','Hyderabad','Agartala','Lucknow','Dehradun','Kolkata']
from random import *
n=len(stlist)
i,j=1,1
marks=0
while i<=5:
   print('SET-',i)
   r=random()
   j=1
   if r<0.5:
      qlist=stlist
      alist=caplist
      while j<=5:
         q=int((n)*random())
         print('Question(',j,')')
         print('What is the capital of ', qlist[q],'?:')
         ans=input()
         if ans.title()==alist[q]:
            marks+=2
            print('CORRECT')
            alist.remove(alist[q])
            qlist.remove(qlist[q])
            n=len(alist)
         else:
            marks=marks-1
            print('INCORRECT')
            print('Correct Answer is ',alist[q])
            alist.remove(alist[q])
            qlist.remove(qlist[q])
            n=len(alist)
         j=j+1
   else:
      qlist=caplist
      alist=stlist
      while j<=5:
         q=int((n)*random())
         print('Question(',j,')')
         print("Which state has it's capital as", qlist[q],'?:')
         ans=input()
         if ans.title()==alist[q]:
            marks+=2
            print('CORRECT')
            alist.remove(alist[q])
            qlist.remove(qlist[q])
            n=len(alist)
         else:
            marks=marks-1
            print('INCORRECT')
            print('Correct answer is ',alist[q])
            alist.remove(alist[q])
            qlist.remove(qlist[q])
            n=len(alist)
         j=j+1
   i=i+1

print('You scored ',marks,' out of 50.')
print('Special thanks to WIKIPEDIA')
print('Created by Shyam Sunder.')
