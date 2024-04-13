# write your code here

import pandas as pd
import re

table_history = pd.read_csv("table-history.csv")
status_changes = pd.read_csv("status-changes.csv")

"""Clean the data"""

table_history["Clean_String"] = table_history["changes"].str.replace("-^!^!^-",",").str.replace("@#@#@#",",").str.replace("-^!^!^--^!^!^-",",")

table_history["Customer_Type"] = table_history["Clean_String"].str.replace(",,",",").str.split(",").str[1]

df = pd.merge(left=table_history,right=status_changes,on="customer_id")

clean = df[["customer_id","start_date","postdate_y","status"]]

#creating a new variable called customer_start with the columns customer_id,start_date, and status
#find the min value of the start date with a status of OK for each customer_id
 
#Create a new variable called customer_end with the columns customers_id, post_date, and status
#find the max value of the start date with a status of termination for each of the customer_id

#Merge the new 2 tables together. Keep the Customer_end status with the columns [Customer_id, Start_date, End_Date, Status]



if __name__ == "__main__":
    print("hello world")
