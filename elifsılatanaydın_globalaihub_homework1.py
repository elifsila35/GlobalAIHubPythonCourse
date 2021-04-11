#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Bir liste oluşturun ve listenin ikinci yarısını listenin ilk yarısı ile değiştirin ve ekranda bu listeyi yazdırın.

def swap(mylist):
    
    mylist=[[1,2],[3,4]]
    mylist1=mylist[0]
    mylist2=mylist[1]
    
    #print("mylist1", mylist1)
    #print("mylist2", mylist2)
    
    mylist1, mylist2 = mylist2, mylist1
    
    print("mylist1", mylist1)
    print("mylist2", mylist2)
    mylist= [mylist1]+[mylist2]
    
    print("new mylist",mylist)
    return
swap(mylist)


# In[ ]:


#Kullanıcıdan 'n' değişkenine tek basamaklı bir tamsayı girmesini isteyin.
#Ardından, n 0'dan n'ye (n dahil) tüm çift sayıları yazdırın.

x = input("Lütfen Tek Basamaklı Bir Sayı Girin ")
print("Girilen sayı: {}".format(x))
if int(x)<=10 and int(x) != 10:
    for i in range(int(x)):
        if i % 2 == 0:
            print(i)
           
else:
    print("Uyarı! Lütfen Tek Basamaklı Bir Sayı Girin")


# In[ ]:




    


# In[ ]:





# In[ ]:





# In[ ]:



            
        


# In[ ]:





# In[ ]:





# In[ ]:




