import time
import re

# opens file, reads file, then writes file to new .txt file
with open('assets/potential-contacts.txt', 'r') as file_read, open ('new_email.txt', 'w') as file_write:
    for paragraph in file_read:
        email_lst = re.findall('\S+@\S+', paragraph)
        for email in email_lst:
            file_write.write(email + '\n')

with open('new_email.txt','r') as f:                                                                                                                                                                                                                                                 
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
