#!/usr/bin/env python
# coding: utf-8

# # Assignment 2 Day 3 B7
#  
# Prime numbers between 1 to 200

# In[41]:


#Prime numbers between 1 to 200

print("The prime numbers between 1 to 200 are as follows-")
print(" ")
for i in range(1,201):
    count=0
    for j in range(2,(i//2+1)):
        
        if i%j==0:
            count=count+1
            break

    if (count==0 and i!=1):
        print(i) 


# In[ ]:





# In[ ]:





# In[ ]:




