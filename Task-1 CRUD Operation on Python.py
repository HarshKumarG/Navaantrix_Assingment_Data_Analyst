#!/usr/bin/env python
# coding: utf-8

# ## 1. CRUD Operations on Mobile Sales Dataset
# 
# #### Perform CRUD operations on a sales dataset stored in a CSV file. You can choose any Python 
# #### library or tool for database operations or perform them directly on the CSV file. Implement 
# #### the following operations:
# 
# #### Create: Insert new records into the dataset.
# 
# #### Read: Retrieve and display specific records from the dataset.
# 
# #### Update: Modify existing records in the dataset.
# 
# #### Delete: Remove specific records from the dataset

# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[2]:


#importing the installed library
import mysql.connector


# In[3]:


#establishing the connection
connection=mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="ababa")


# In[4]:


# to check whether connection is esblished or not
if connection.is_connected:
    print("Connected to database successfully")
else:
    print("Not Connected")


# In[5]:


# Creating a cursor object
cursor=connection.cursor()


# In[6]:


#query to show database 
cursor.execute("show databases")
databases=cursor.fetchall()
for i in databases:
    print(i[0])


# In[7]:


# to use desired database
cursor.execute("use ababa")
print("Successfully selected the databse")


# In[8]:


# show the available tables in databse
cursor.execute("show tables")
tables=cursor.fetchall()
print("Tables available in selected database")
for i in tables:
    print(i[0])


# In[9]:


# show records in Mobiles table
cursor.execute("select * from mobiles limit 5")
r1=cursor.fetchall()
print("records are present in table")
for i in r1:
    print(i)


# #### 1.Create: Insert new records into the dataset.

# In[10]:


# inserting 5 records in mobiles table
query=("insert into mobiles (customer_id,customer_name,city,ship_mode,mode_of_payment,amount,item,quantity) values(%s,%s,%s,%s,%s,%s,%s,%s)")
values=[(501,"Rahul Kashyap","Mumbai","Express Shipping","UPI",49999,"Apple Mobile",2),
(502,"Harsh Gupta","Banglore","Same Day Delivery","Debit Card",5500,"Boat Earphone",3),
(503,"Neha Chauhan","Kolkata","Standard Shipping","Credit Card",84000,"Samsung Phone",2),
(504,"Pankaj Singh","Delhi","Same Day Delivery","Net Banking",40120,"Screen Protector",10),
(505,"Suraj Vishwakarma","Banglore","Standard Shipping","Net Banking",5500,"Phone Case",3)]
cursor.executemany(query,values)
connection.commit()
print("5 records inserted successfully")


# #### 2.Read Operation (Retrieve and display specific records from the dataset)

# In[11]:


# Retrieve 5 recents records inserted Earlier (customer_id 501 to 505)
cursor.execute("select * from mobiles where customer_id between 501 and 505")
rec=cursor.fetchall()
print("5 recents records inserted where customer_id 501 to 505")
for i in rec:
    print(i)


# In[12]:


# Retrieve records where ship_mode is Express Shipping and mode_of_payment is UPI
cursor.execute("select * from mobiles where ship_mode='Express Shipping' and mode_of_payment='UPI'")
sm=cursor.fetchall()
print("Found!,here is the expected output where ship_mode is Express Shipping and mode_of_payment is UPI")
for i in sm:
    print(i)


# In[13]:


# Retrieve the Total amount for each item in descending order
cursor.execute("select Item,round(sum(amount),2) as Total_Amount from mobiles group by item order by Total_Amount desc")
Ta=cursor.fetchall()
print("Here is total amount for each item")
for i in Ta:
    print(i)


# In[14]:


# retrieve the top 3 customers who mades the high sale amount
cursor.execute("select distinct Amount,customer_name from mobiles order by amount desc limit 3")
TC=cursor.fetchall()
print("Top 3 customers are...")
for i in TC:
    print(i)


# #### 3.Update Operation (Modify existing records in the dataset.)

# In[15]:


# Update the city from Delhi to Pune where customer_name is Mason Gibson
cursor.execute("update mobiles set city='Pune' where customer_name='Mason Gibson' ")
connection.commit()
print("Successfully city updated!")


# In[16]:


# Update the customer name as Abhishekh where amount is greater than 50k and ship mode is Standard Shipping
cursor.execute("update mobiles set customer_name='Abhishekh' where amount>50000 and ship_mode='Standard Shipping' ")
connection.commit()
print("Successfully customer name is updated!")


# In[17]:


# Update the customer_id as 1000 where customer name is Mark Bond
cursor.execute("update mobiles set customer_id=1000 where customer_name='Mark Bond' ")
connection.commit()
print("Successfully customer id is updated!")


# #### 4.Delete Operation (Remove specific records from the dataset):

# In[19]:


# delete the records where customer_id is 40
cursor.execute("delete from mobiles where customer_id=40 ")
connection.commit()
print("Deleted record Successfully!")


# In[20]:


# delete the records where customer_id is 80
cursor.execute("delete from mobiles where customer_id=80 ")
connection.commit()
print("Deleted record Successfully!")


# In[ ]:




