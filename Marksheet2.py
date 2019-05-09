#!/usr/bin/env python
# coding: utf-8

# In[1]:


sub1=int(input("Enter marks of the \"English\" Subject Number/100: "))
sub2=int(input("Enter marks of the \"Mathematics\" subject Number/100: "))
sub3=int(input("Enter marks of the \"Computer Science\" subject Number/100: "))
sub4=int(input("Enter marks of the \"Physics\" subject Number/100: "))
sub5=int(input("Enter marks of the \"Chemistry\" subject Number/100: "))
subPass = 0
subFail = 0

avg=(sub1+sub2+sub3+sub4+sub4)/5
chkPercentage = sub1+sub2+sub3+sub4+sub4
print("Average of Your Marks is " + str(avg))
percentage = (chkPercentage / 500) * 100
print("Percentage of Your Marks is " + str(percentage) + "%")
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")
if(sub1 < 55):
    print("You are Fail in English Subject")
    subFail = subFail + 1
else:
    subPass = subPass + 1
if(sub2 < 55):
    print("You are Fail in Mathematics Subject")
    subFail = subFail + 1
else:
    subPass = subPass + 1
if(sub3 < 55):
    print("You are Fail in Computer Science Subject")
    subFail = subFail + 1
else:
    subPass = subPass + 1
if(sub4 < 55):
    print("You are Fail in Physics Subject")
    subFail = subFail + 1
else:
    subPass = subPass + 1
if(sub5 < 55):
    print("You are Fail in Chemistry Subject")
    subFail = subFail + 1
else:
    subPass = subPass + 1
print("Total Subjects 5 , Pass " + str(subPass) + " Fail " + str(subFail) )


# In[ ]:




