#!/usr/bin/env python
# coding: utf-8

# In[ ]:


question1=str(input("Bu nedir?"))
ans1="elma"
ans1_=ans1.lower()
if question1==ans1_:
    y1="okey"
    print("okey, you win 10 points")
else:
    print("wrong")
question2=str(input("Bu renk hangi renktir? "))
ans2="kırmızı"
ans2_=ans2.lower()
if question2==ans2_:
    y2="okey"
    print("okey")
else:
    print("wrong")
question3=str(input("Okulda okuyan insana ne denir? "))
ans3="öğrenci"
ans3_=ans3.lower()
if question3==ans3_:
    y3="okey"
    print("okey")
else:
    print("wrong")
question4=str(input("Yazı yazmak için kullanılan aletin adı nedir? "))
ans4="kalem"
ans4_=ans4.lower()
if question4==ans4_:
    y4="okey"
    print("okey")
else:
    print("wrong")
question5=str(input("Okulda bir şey öğreten insan? "))
ans5="öğretmen"
ans5_=ans5.lower()
if question5==ans5_:
    y5="okey"
    print("okey")
else:
    print("wrong")
question6=str(input("İlk eğitimi nerede alırız? "))
ans6="İlkokul"
ans6_=ans6.lower()
if question6==ans6_:
    y6 ="okey"
    print("okey")
else:
    print("wrong")
question7=str(input("Filmleri nerede izleriz? "))
ans7="sinema"
ans7_=ans7.lower()
if question7==ans7_:
    y7="okey"
    print("okey")
else:
    print("wrong")
question8=str(input("Nerede yaşarız? "))
ans8="ev"
ans8_=ans8.lower()
if question8==ans8_:
    y8="okey"
    print("okey")
else:
    print("wrong")
question9=str(input("Üşümemek için ne giyeriz? "))
ans9="ceket"
ans9_=ans9.lower()
if question9==ans9_:
    y9="okey"
    print("okey")
else:
    print("wrong")
question10=str(input("Mezun olmak için ne gerekir? "))
ans10="diploma"
ans10_=ans10.lower()
if question10==ans10_:
    y10="okey"
    print("okey")
else:
    print("wrong")

dic=[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]
a=dic.count("okey")
x=a*10
if x>=50:
    print("You win!! You are successful")
else:
    print("You lose!! You are unsuccessful")


# In[ ]:





# In[ ]:





# In[ ]:




