import mysql.connector 
import time
from datetime import date



global conn,cursor
conn = mysql.connector.connect(host='localhost',database='crime_management',user='root',password='1234')
cursor = conn.cursor()




def introduction():
    msg = '''
         C R I M E   R E C O R D    I N F O R M A T I O N    S Y S T E M

         
          
          Welcome to Crime protech.
          
          
          Crime record are the most important part of any modern society for better controlling crime. Crime database database help us to recognise the
          type of crime right now happending in the system and how to overcome that.

          

          The systemt is divided into four major parts ie addition of data, modification, searching and 
          reporting. All these part are further divided into menus for easy navigation.
          
          

          NOTE: The input system is case-SENSITIVE so type exact Column Name wherever required.
        

          If you have any query or suggestions please contact the support team - crimebranchtechnicalsupport.gmail.com \n\n\n\n'''

    


    for x in msg:
        print(x, end='')
        time.sleep(0.002)
        


    wait = input('Press any key to continue.....')






def made_by():
    msg = ''' 
            Crime Record information system made by     : Cecily Ambooken, Serah Kurian, Devika Madhusoodanan
            School Name                                 : Gems Our Own Indian School, Dubai
            session                                     : 2021-2022
            
            
            \n\n\n
        '''

    for x in msg:
        print(x, end='')
        


    wait = input('Press any key to continue.....')




def display_records():
    cursor.execute('select * from crime_record;')
    records = cursor.fetchall()
    for row in records:
        print(row)







def login():
    
    while True:
        

        uname = input('Enter your name :')
        upass = input('Enter your Password :')
        cursor.execute('select * from login where name="{}" and pwd ="{}"'.format(uname,upass))
        cursor.fetchall()
        rows = cursor.rowcount
        
        if rows!=1:
            print('Invalid Login details..... Try again')
            
        else:
            print('You are eligible for operating this system............')
            print('\n\n\n')
            
            #print('Press any key to continue...............')
            break







def add_crime_type():
    
    offence_name = input('Enter offence Name : ')
    ipc_section =  input('Enter IPC section applied for this offence : ')
     
    sql = 'insert into crime_type(offence_name,ipc_section) values("{}","{}");'.format(offence_name,ipc_section)

    cursor.execute(sql)
    print('\n\n New Offence Type added....')


    wait= input('\n\n\nPress any key to continue............')







def add_record():

    crime_date = input('Enter Crime Date (yyyy/mm/dd) : ')
    offence_type = input('Enter Offence_id : ')
    complaint_by = input('Enter Name of complainee : ')
    address  = input('Enter Complainee Address :')
    phone  = input('Enter Complainee Phone No :')
    status  = input('Enter current status :')
    
    update_date = date.today()
    
    sql = 'insert into crime_record(c_date,offence_type,complaint_by,address,phone_no,status,update_date) values \
            ("{}",{},"{}","{}","{}","{}","{}");'.format(crime_date, offence_id,complaint_by,address,phone,status,update_date) 
    cursor.execute(sql)
    print('\n\n New Crime Record added....')

    cursor.execute('select max(id) from crime_record;')
    no = cursor.fetchone()
    print(' Your complaint  No is : {} \n\n\n'.format(no[0]))
    wait = input('\n\n\nPress any key to continue............')




def modify_crime_type_record():
    
    print(' M O D I F Y    C R I M E  T Y P E  S C R E E N ')
    print('1.  Offence Name \n')
    print('2.  IPC Section \n')

    
    choice = int(input('Enter your choice :'))
    field=''
    if choice==1:
        field='offence_name'
    if choice==2:
        field='ipc_section'
    

    crime_id = input('Enter Crime Type ID :') # id of the record in which we want to change offence name and ipc section
    value = input('Enter new values :')
    sql = 'update crime_type set '+ field +' = "' + value +'" where id ='+ crime_id +';'
    cursor.execute(sql)
    
    print('Record updated successfully................')
    
    wait = input('\n\n\nPress any key to continue............')





def modify_record():

    
    print(' M O D I F Y    C R I M E  R E C O R D  S C R E E N ')
    print('1.  Crime date \n')
    print('2.  Offence Type  \n')
    print('3.  Complaint By  \n')
    print('4.  Address  \n')
    print('5.  Phone No  \n')
    print('6.  Status  \n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'c_date'
    if choice ==2:
        field = 'offence_type'
    if choice == 3:
        field = 'complaint_by'
    if choice == 4:
        field = 'address'
    if choice == 5:
        field = 'phone_no'
    if choice == 6:
        field = 'status'
    
    print('\n\n\n')
    
    crime_id = input('Enter Crime Record ID  :')
    value = input('Enter new values :')
    sql = 'update crime_record set ' + field + \
        ' = "' + value + '" where id =' + crime_id + ';'
    
    cursor.execute(sql)
    
    print('Record updated successfully................')
    wait = input('\n\n\nPress any key to continue............')




def search_menu():

    
    print(' S E A R C H    C R I M E  R E C O R D  S C R E E N ')
    print('1.  Crime date \n')
    print('2.  Offence Type  \n')
    print('3.  Complaint By  \n')
    print('4.  Address  \n')
    print('5.  Phone No  \n')
    print('6.  Status  \n')
    choice = int(input('Enter your choice :'))
    field = ''
    
    if choice == 1:
        field = 'c_date'
        
    if choice == 2:
        field = 'offence_type'
        
    if choice == 3:
        field = 'complaint_by'
        
    if choice == 4:
        field = 'address'
        
    if choice == 5:
        field = 'phone_no'
        
    if choice == 6:
        field = 'status'
        
    value = input('Enter value to search :')
    

    sql = 'select cr.id,c_date,offence_name,complaint_by,address,phone_no,status,update_date \
          from crime_record cr, crime_type ct where cr.offence_type = ct.id \
          AND ' + field + '= ' + value + ';'
   


    cursor.execute(sql)
    results = cursor.fetchall()
    records = cursor.rowcount
    
    for row in results:
        print(row)
        
    if records < 1:
        print('Record not found \n\n\n ')

        
    wait = input('\n\n\nPress any key to continue......')






def main_menu():
    
    login()
    
    introduction()
    
    while True:
        
      
      print(' C R I M E   R E C O R D    I N F O R M A T I O N   S Y S T E M')
      
      print('*'*100)
      
      print("\n1.  Add New Record")
      print("\n2.  Add New Crime Type")
      print('\n3.  Modify Crime Type Record')
      print('\n4.  Modify Crime Record')
      print('\n5.  Search Crime Database')
      print('\n6.  Report menu')
      print('\n7.  Close application')
      print('\n\n')
      
      choice = int(input('Enter your choice ...: '))
    

      if choice == 1:
        add_record()
        

      if choice == 2:
        add_crime_type()
        

      if choice == 3:
        modify_crime_type_record()
        
      
      if choice == 4:
        modify_record()
        

      if choice == 5:
        search_menu()
        

      if choice == 7:
        break
    
    made_by()





if __name__ == "__main__":
    main_menu()
