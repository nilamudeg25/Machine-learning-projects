import pymysql

def connect():
    global con,cursor
    con=pymysql.connect(host="localhost",user="root",password="admin",database="reservation")
    cursor=con.cursor()

def closedb():
    con.close()
    cursor.close()
  
class Rail:
    def __init__(self,name,number,source,destination,departure,arrival,runson):
        self.__name=name
        self.__number=number
        self.__source=source
        self.__destination=destination
        self.__departure=departure
        self.__arrival=arrival
        self.__runson=runson
       
      
    def getName(self):
        return self.__name
    def getNumber(self):
        return self.__number
    def getSource(self):
        return self.__source
    def getDestination(self):
        return self.__destination
    def getDeparture(self):
        return self.__departure
    def getArrival(self):
        return self.__arrival
    def getRunson(self):
        return self.__runson
    
    def setname(self,newname):
        self.__name=newname
    def setnumber(self,newnumber):
        self.__number=newnumber
    def setsource(self,newsource):
        self.__source=newsource
    def setdestination(self,newdestination):
        self.__destination=newdestination    
    def setdeparture(self,newdeparture):
        self.__departure=newdeparture
    def setarrival(self,newarrival):
        self.__arrival=newarrival
    def setrunson(self,newrunson):
        self.__runson=newrunson



class Railsmenu:
    def execute(self,choice):
        if choice==1:
            print('insert new train details')
            q='select * from train;'
            connect()
            cursor.execute(q)
            data=cursor.fetchall()
            print(data)

            print('1>update train details \n 2>insert new train details \n 3>delete train details \n 4>exit \n')
            x=int(input('select choice:'))
            if x==2:
           
                name=input('enter train name:')
                number=int(input('enter train_no:'))
                source=input('enter runs from source:')
                destination=input('enter runs to destination:')
                departure=input('enter departure time:')
                arrival=input('enter arrival time:')
                runson=input('enter runs on: ')
        
                try: 
                    data=[name,number,source,destination,departure,arrival,runson]
                    q="insert into train values(%s,%s,%s,%s,%s,%s,%s);"
                    cursor.execute(q,data)
                    con.commit()
                    print('details has been inserted...')
                except pymysql.DatabaseError as e:
                    con.rollback()
                    print(e)
                
                finally:
                    closedb()
            
    
        elif choice ==2:
            print('show train details')
            try:
                connect()
                q="select * from train;"
                cursor.execute(q)
                data=cursor.fetchall()
                for train in data:
                    print("name:{} number:{} source:{} destination:{} departure:{} arrival:{} runson:{}".format(train[0],train[1],train[2],train[3],train[4],train[5],train[6]))
                print('train details has been added')
            except pymysql.DatabaseError as e:
                con.rollback()
                print(e)
                
            finally:
                closedb()


        elif choice==3:
            print("update runson with number")
            number=int(input("enter number of train which you want to update:"))
            q='select * from train ;'
            connect()
            cursor.execute(q)
            data=cursor.fetchall()
            print(data)

            print('1> update train details \n2> insert new train details \n3> delete train details \n4> exit \n')
            x=int(input('select choice:'))
            if x==1:
                ruson=input('enter runson:')
                try:
                    data=[ruson,number]
                    q="update train set ruson=%s where number=%s;"
                    cursor.execute(q,data)
                    con.commit()
                    print('train details has been updated successfully...')
                    
                except pymysql.DatabaseError as e:
                    con.rollback()
                    print(e)
                    
                finally:
                    closedb()



        elif choice ==4:
            print("delete train details")
            q='select * from train;'
            connect()
            cursor.execute(q)
            data=cursor.fetchall()
            print(data)

            print('1>update train details \n2> insert new train details \n3> delete train details \n4> exit \n')
            x=int(input('select choice:'))
            if x==3:
                number=int(input("enter number:"))
                try:
                    q="delete from train where number={}".format(number)
                    cursor.execute(q)
                    
                    print(data)
                    con.commit()
                    print('successfully deleted train details')
                    
                except pymysql.DatabaseError as e:
                    con.rollback()
                    print(e)
                    
                finally:
                    closedb()    

         
    
        elif choice ==5:
            print('Reservation of Ticket')
            q="select * from ticket;"
            connect()
            cursor.execute(q)
            data=cursor.fetchall()
            print(data)

            print('1> insert new passanger details \n2> cancel ticket \n3> exit \n')
            x=int(input('select choice:'))
            if x==1:
                l=[]
                pname=input("enter passanger name:")
                l.append(pname)
                age_of_pa=int(input("enter the age of passanger:"))
                l.append(age_of_pa)
                no_of_pa=int(input("enter no of passanger:"))
                l.append(no_of_pa)
                train_no=int(input("enter train no:"))
                l.append(train_no)
                quota=input('enter the quota:')
                l.append(quota)
            
                print('1> AC1=1950 PP \n2> AC2=1150 PP \n3> AC3=815 PP \n4> Sleeper=315 PP \n5> Second seating=180 PP \n6> First class=950 PP \n7> AC chair car=665 PP \n ')
                pa_cls=int(input("select choice: "))
            
                if pa_cls==1:
                    amt=no_of_pa*1950
                    cls='AC1'
                elif pa_cls==2:
                    amt=no_of_pa*1150
                    cls='AC2'
                elif pa_cls==3:
                    amt=no_of_pa*815
                    cls='AC3'
                elif pa_cls==4:
                    amt=no_of_pa*315
                    cls='sleeper'
                elif pa_cls==5:
                    amt=no_of_pa*180
                    cls='Second seating'
                elif pa_cls==6:
                    amt=no_of_pa*950
                    cls='First class'
                else :
                    amt=no_of_pa*665
                    cls='AC chair car'
                l.append(pa_cls)
                print("Total amount to be paid:",amt)
                l.append(amt)
                pnr=int(input('enter pnr no:'))
                l.append(pnr)
                status=input('enter status:')
                l.append(status)
                train1=l

                try:
                
                    data=[pname,age_of_pa,no_of_pa,train_no,quota,pa_cls,amt,pnr,status]
                    q="insert into ticket values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                    cursor.execute(q,data)
                    con.commit()
                    print('passanger details has been inserted...')
                except pymysql.DatabaseError as e:
                    con.rollback()
                    print(e)
                
                finally:
                    closedb()
            
            

   
        elif choice ==6:
            print('Show details of passanger')
            try:
                connect()
                q="select * from ticket;"
                cursor.execute(q)
                data=cursor.fetchall()
                for ticket in data:
                    print("pname:{} age_of_pa:{} no_of_pa:{} train_no:{} quota:{} pa_cls:{} amt:{} pnr:{} status:{}".format(ticket[0],ticket[1],ticket[2],ticket[3],ticket[4],ticket[5],ticket[6],ticket[7],ticket[8]))
                print('passanger details has been added successfully...')
            except pymysql.DatabaseError as e:
                con.rollback()
                print(e)
                
            finally:
                closedb()


      
        elif choice ==7:
            print('Display PNR status')
            
            pnr=int(input("enter pnr no: "))
            pn=(pnr,)
            q="select * from ticket where pnr=%s;"
            connect()
            cursor.execute(q,pn)
            data=cursor.fetchall()
            print('pnr status are as follows: ')
            for ticket in data:
                 print(ticket)

            

        elif choice ==8:
            print('Cancellation of Ticket')
            q="select * from ticket;"
            connect()
            cursor.execute(q)
            data=cursor.fetchall()
            print(data)

            pnr=int(input('enter pnr: '))
            print('1> insert new passanger details \n2> cancel ticket \n3> exit \n')
            x=int(input("select choice:"))
            if x==2:
                status=input("enter status: ")
                try:
                    data=[status,pnr]
                    q="update ticket set status=%s where pnr=%s ;"
                    cursor.execute(q,data)
                    con.commit()
                    print('successfully cancelled ticket')
                    
                except pymysql.DatabaseError as e:
                    con.rollback()
                    print(e)
                    
                finally:
                    closedb() 


            
        elif choice ==9:
            print('Exit')
 
        else:
            print("wrong choice")





menu=Railsmenu()

print('*******welcome TO Indian Railway Passanger*******')

while True:
    print('1> insert new train details \n2> show train details \n3> update train details \n4> delete train details \n5> Reservation of Ticket \n6> show details of passanger \n7> Display PNR status  \n8> Cancellation of Ticket \n9> exit \n')
    ch=int(input('enter your choice:'))
    menu.execute(ch)

