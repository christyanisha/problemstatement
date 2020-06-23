import mysql.connector
def getdb():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database='internship')
def additem():
    try:
        global var
        mydb = getdb()
        mycursor = mydb.cursor()
        #print(entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get())
        print("TELEVISION")
        N = int(input("enter 'N'value:"))
        if N != 0:
            
            for i in range(0,N):
                sql = "INSERT INTO product (brand , cat,amt) VALUES (%s, %s,%s)"
                entry1=input("brand:")
                entry2=input("catogary:")
                entry3=input("amt:") 
                val = [entry1,entry2,entry3]
                mycursor.execute(sql,val)
                mydb.commit()
                print("success")
                #messagebox.showinfo("inserted","successfully inserted into db")
            
        else:
            print()
    except mysql.connector.Error as e:
        print(e)

additem()
def custom():
    mydb = getdb()
    mycursor = mydb.cursor()
    a=int(input("enter amount:"))
    #b=int(input("enter end amount:"))
    mycursor.execute("select * from product  WHERE amt <='%s'"%a)
    
    myresult = mycursor.fetchall()
    #myresult.execute("select * from product  order by amt")
    
    for count in range (0,len(myresult)):
        print(myresult[count])
custom()    
    
