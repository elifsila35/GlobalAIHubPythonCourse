#!/usr/bin/env python
# coding: utf-8

# In[ ]:


first_dictionary = { "kullanici_adi" : "hi", "parola" : "hello"}


#print(first_dict)


kullanici_adi1 =input("Lütfen kullanıcı adınızı giriniz: ")
parola1= input("Lütfen Parolanızı giriniz: ")

for kullanici_adi in [first_dictionary]:
    if (kullanici_adi == kullanici_adi1 and parola != parola1):
        print("Parolanız hatalı")
    elif (kullanici_adi != kullanici_adi1 and parola == parola1):
        print("Kullanıcı adınız hatalı")
    elif (kullanici_adi != kullanici_adi1 and parola!= parola1):
        print("Kullanıcı adınız ve parolanız hatalıdır.")
    
    else:
        print("Tebrikler, Başarıyla giriş yaptınız")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




