import time
import re

# Reading Opened File
with open("assets/potential-contacts.txt", "r") as file:
  contact_data = file.read()

with open('assets/potential-contacts.txt', 'r') as fr, open ('new_email.txt', 'w') as fw:
    for paragraph in fr:
        email_lst = re.findall('\S+@\S+', paragraph)
        for email in email_lst:
            fw.write(email + '\n')

with open('raw/new_email.txt','r') as f:                                                                                                                                                                                                                                                 
    distinct_content=set(f.readlines())                                                                                                                                                                                                                                                   

to_file=""                                                                                                                                                                                                                                                                       
for element in distinct_content:                                                                                                                                                                                                                                                               
    to_file += element                                                                                                                                                                                                                                                           
with open('email.txt','w') as w:                                                                                                                                                                                                                                                  
    w.write(to_file) 

with open('assets/potential-contacts.txt', 'r') as fr, open ('raw_phone_numbers.txt', 'w') as fw:
    for paragraph in fr:
        phone_lst = re.findall('[0-9-+x.()]{7,}', paragraph)
        for phone in phone_lst:
            numbers = phone.replace(".", "").replace("-","").replace("(","").replace(")","")
            if len(numbers) == 10:
                format_num = numbers[:3] + '-' + numbers[3:6] + '-' + numbers[6:]
                fw.write(format_num + '\n')

with open('raw_phone_numbers.txt','r') as f:                                                                                                                                                                                                                                                 
    distinct_content=set(f.readlines())                                                                                                                                                                                                                                                   

to_file=""                                                                                                                                                                                                                                                                       
for element in distinct_content:                                                                                                                                                                                                                                                               
    to_file=to_file+element                                                                                                                                                                                                                                                           
with open('phone_numbers.txt','w') as w:                                                                                                                                                                                                                                                  
    w.write(to_file) 
