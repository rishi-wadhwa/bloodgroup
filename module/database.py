'''
Created on Jan 10, 2017

@author: hanif
'''

import pymysql

class Database:
    def connect(self):
        return pymysql.connect("localhost","root","","crud_flask" )
    
    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if id == None:
                cursor.execute("SELECT * FROM register order by bgroup asc")
            else: 
                cursor.execute("SELECT * FROM REGISTER where id = %s order by bgroup asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
    def read34(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if id == None:
                cursor.execute("SELECT * FROM contact ")
            else: 
                cursor.execute("SELECT * FROM contact ")

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
    def read22(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if id == None:
                cursor.execute("SELECT * FROM register ")
            else: 
                cursor.execute("SELECT * FROM register where id = %s order by fname asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
    def read3(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if id == None:
                cursor.execute("SELECT * FROM register order by bgroup asc")
            else: 
                cursor.execute("SELECT * FROM REGISTER where id = %s order by bgroup asc", (bgroup,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
            
    def insert(self,data):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("INSERT INTO register(fname,lname,email,contact,username,password,address,bgroup,problem) VALUES(%s, %s, %s,%s,%s,%s,%s,%s,%s)", (data['name'],data['phone'],data['address'],data['contact'],data['username'],data['password'],data['address1'],data['bgp'],data['problem']))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
    def insert1(self,data):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("INSERT INTO register(fname,lname,email,contact,username,password,address,bgroup,problem) VALUES(%s, %s, %s,%s,%s,%s,%s,%s,%s)", (data['name'],data['phone'],data['address'],data['contact'],data['username'],data['password'],data['address1'],data['bgp'],data['problem']))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
    def insert11(self,data):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("INSERT INTO menu(foodname,ftype,fprice) VALUES(%s, %s,%s)", (data['foodName'],data['foodType'],data['priceFull']))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
    def insertc(self,data):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("INSERT INTO contact(name,email,messages) VALUES(%s, %s,%s)", (data['name'],data['email'],data['message']))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
    def insertp(self,data):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("INSERT INTO patient(patient_name,email_id,contact_no,address,dob,required,units_required,hospital_name,purpose,blood_group) VALUES(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)", (data['name'],data['email'],data['phn'],data['Address'],data['DOB'],data['when_reqd'],data['units'],data['h_name'],data['purpose'],data['BG']))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
    
    def updateadmin(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("UPDATE register set fname=%s,lname = %s, email = %s,contact=%s where id = %s", (data['name'],data['lname'],data['email'],data['contact'],id))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
        
    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("DELETE FROM register where id = %s", (id,))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
