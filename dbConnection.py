try: 
    import mysql.connector
    import random
except  Exception as ex:
    error0 = str(ex)
    print("ImP:   "+error0)    

class dbConnect():
        def __init__(self):
            self.my_db = mysql.connector.connect(host='localhost', 
                                    user='root', 
                                    passwd='Pinzer123#@!',
                                    database='db_typing')
            self.mycursor = self.my_db.cursor() 
            self.myUname = self.myName = self.myLname = self.myPass = ''     
        
        # Function to register User
        def InsertInfo (self,name,last,user,passw,email):
            try:
                InsertQuery = 'INSERT INTO `db_typing`.`tbl_userinfo` (`usrName`, `usrLname`, `usrUname`, `usrPass`, `usrEmail`) VALUES (%s, %s, %s, %s, %s);'
                val = (name,last,user,passw,email)
                self.mycursor.execute(InsertQuery,val)
                z = self.getData(user,passw)
                self.my_db.commit()  
                return z
            except Exception as ex:
                print(ex)
                return -100



        # Function to register User
        def guestInfo (self):
            print("Guest Clicked")
            try:
            # Take the Guest name From external txt file for DB registeration.
                file = 'num1.txt'
                num = open(file).read()
                sp = num.split('\n')
                s = random.choice(sp)
                r = random.choice(sp)
                InsertQuery = 'INSERT INTO `db_typing`.`tbl_userinfo` (`usrName`, `usrUname`) VALUES (%s, %s);'
                re = (s,r)
                self.mycursor.execute(InsertQuery,re)
                self.my_db.commit()  
                return r
            except Exception as ex:
                print(ex)
                return "Nabod"
     
        
        
        # Function to check login Status
        def checkLogin (self,Uname, Pass):
            try:
                
                checkQuery = 'SELECT * FROM tbl_userinfo WHERE usrUname = %s and usrPass = %s;'
                checkCond = (Uname, Pass)
                self.mycursor.execute(checkQuery, checkCond)            
                myresult = self.mycursor.fetchall()
            
                for x in (myresult):
                    pass
            
                if (Uname == x[3] and Pass == x[4]):
                    uLoginName = str(x[1])  
                    uLoginLname = str(x[2])
                    uLoginUname = str(x[3])
                    uLoginID = str(x[0])

                    self.myUname = uLoginUname
                    self.myName = uLoginLname
                    self.myLname = uLoginLname
                    self.myPass = str(x[4])
                    # self.userINFO(Uname,Pass)
                    fulName = uLoginName+"  "+uLoginLname
                   
                    # Writing the ID of person who logs in.
                    IDFile = open('temID.txt','w')
                    IDFile.write(uLoginID)
                    IDFile.close()
                    
                    print("Login Succeeded")
                    return (fulName)
                else: 
                    print("Fail to Login")
                    return ("N/A USER")            
            
            except Exception as ex:
                    error = str(ex)
                    print("Check:  :   "+error)
                    return ("N/A USER")

            self.my_db.commit()    
                



        # Function to get data =
        def getData (self,Uname, Pass):
            try:
                checkQuery = 'SELECT * FROM tbl_userinfo WHERE usrUname = %s and usrPass = %s;'
                checkCond = (Uname, Pass)
                self.mycursor.execute(checkQuery, checkCond)            
                myresult = self.mycursor.fetchall()
            
                for x in (myresult):
                    pass
            
                if (Uname == x[3] and Pass == x[4]):
                    selectID = str(x[0])  
                    return (selectID)
                else: 
                    print("Fail to Login")
                    return ("N/A USER")            
            
            except Exception as ex:
                    error = str(ex)
                    print("Check:  :   "+error)
                    return ("N/A USER")

            self.my_db.commit()      


        def userINFO (self,UrsID):
            try:
                checkQuery = 'SELECT * FROM tbl_userinfo WHERE usrID = '+UrsID+' ;'
                # checkCond = (UrsID)
                self.mycursor.execute(checkQuery)            
                myresult = self.mycursor.fetchall()
                
                return myresult
            
            except Exception as ex:
                    error = str(ex)
                    print("Check userINFO:   "+error)
                    return ("N/A USER")

            self.my_db.commit()        
    
        # def userInfo(self):
        #     x = self.userINFO(self.myUname,self.myPass)
        #     # print("RE: ",x)
        #     return x
        
       
        def insertFeedback(self, usrID, usrEmail, usrmsg):
            try:
                intQuery = "INSERT INTO `db_typing`.`tbl_feedback` (`usrID`, `usrEmail`, `fdbText`) VALUES ('"+usrID+"', '"+usrEmail+"', '"+usrmsg+"');"          
                self.mycursor.execute(intQuery)
                self.my_db.commit()  
                return True
            except Exception as ex:
                print(ex)
                return False            
        
   

        # to display records
        def recordINFO (self,UrsID):
            try:
                checkQuery ='SELECT tbl_record.rID,concat(tbl_userinfo.usrName," ",tbl_userinfo.usrLname) as fullName ,tbl_userinfo.usrName, tbl_record.rLevel, tbl_record.rTime, tbl_record.rWord_PM,tbl_record.rAccuracy from tbl_userinfo inner join tbl_record on tbl_record.userID = tbl_userinfo.usrID where tbl_userinfo.usrID = '+UrsID+';'               
                # checkCond = (UrsID)
                self.mycursor.execute(checkQuery)            
                myresult = self.mycursor.fetchall()
                return myresult
            
            except Exception as ex:
                    error = str(ex)
                    print("Check userINFO:   "+error)
                    return ("N/A USER")

            self.my_db.commit() 



        # to display feedbacks
        def feedInfo (self,UrsID):
            try:
                checkQuery ='SELECT tbl_userinfo.usrid, tbl_userinfo.usrUname, tbl_feedback.usrEmail, tbl_feedback.fdbText from tbl_feedback inner join tbl_userinfo on tbl_feedback.usrID = tbl_userinfo.usrID where tbl_userinfo.usrID = '+UrsID+';'               
                # checkCond = (UrsID)
                self.mycursor.execute(checkQuery)            
                myresult = self.mycursor.fetchall()
                return myresult
            
            except Exception as ex:
                    error = str(ex)
                    print("Check userINFO:   "+error)
                    return ("N/A USER")

            self.my_db.commit()      
    
    

        def instRecord(self, usrID, uLevel, uTime, uWpm, uAcc):
            try:
                intQuery = "INSERT INTO `db_typing`.`tbl_record` (`userID`, `rLevel`, `rTime`, `rWord_PM`, `rAccuracy`) VALUES ('"+usrID+"', '"+uLevel+"', '"+uTime+"', '"+uWpm+"', '"+uAcc+"');"        
                self.mycursor.execute(intQuery)
                self.my_db.commit()  
                return True
            except Exception as ex:
                print(ex)
                return False  

    
# s = dbConnect()
# d = s.checkLogin('123','123')     
# print(d)     
# i = open('temID.txt').read()
# print(i)
# x = s.userINFO(i)
# print(x)
# s.insertFeedback("321",'pero','HI')
# z = s.recordINFO('20')
# for x in z:
    # print(x[0])
# y = s.feedInfo('20')
# for x in y:
#     print(x[0])
# t = s.instRecord('321','Begginer','16','50','90')