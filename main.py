from flask import Flask, render_template, request, redirect, session
import sqlite3
from flask_session import Session
# from datetime import datetime
import datetime


con = sqlite3.connect("crimemanagement.db", check_same_thread= False)
cursor = con.cursor()
listOfTables = con.execute("SELECT name from sqlite_master WHERE type='table' AND name='CRIMES' ").fetchall()
listOfTables1 = con.execute("SELECT name from sqlite_master WHERE type='table' AND name='USERS' ").fetchall()
if listOfTables!=[]:
    print("Crimes table Already Exists ! ")
else:
    con.execute(''' CREATE TABLE CRIMES(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            NAME TEXT,
                            DESCRIPTION TEXT,
                            REMARKS TEXT,
                            DATE TEXT); ''')

print("crimes table has created")
if listOfTables1!=[]:
    print("Users table Already Exists ! ")
else:
    con.execute(''' CREATE TABLE USERS(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            address TEXT,
                            email TEXT,
                            phone TEXT,
                            password TEXT); ''')

print("User table has created")

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

from datetime import date

today = date.today()
print("Today's date:", today)
print(str(today))

@app.route("/")
def main():
    return render_template("maindash.html")

@app.route("/adminlogin", methods=["GET","POST"])
def welcome():
    try:
        if request.method == "POST":
            getUsername = request.form["uname"]
            getPassword = request.form["upass"]
            print(getUsername)
            print(getPassword)
            if getUsername == "admin" and getPassword == "12345":
                return redirect("/viewallcrime")
        return render_template("adminlogin.html")
    except Exception as e:
        print(e)

@app.route("/userlogin", methods=["GET","POST"])
def userwelcome():
    if request.method == "POST":
        getEmail = request.form["email"]
        getPass = request.form["pass"]
        print(getEmail)
        print(getPass)
        cursor.execute("SELECT * FROM USERS WHERE email = '"+getEmail+"' AND password = '"+getPass+"'")
        r = cursor.fetchall()
        if len(r) > 0:
            for i in r:
                getName = i[1]
                getId = i[0]

            session["name"] = getName
            session["id"] = getId
            return redirect("/crimereport")
    return render_template("userlogin.html")

@app.route("/userreg", methods=["GET","POST"])
def userreg():
    if request.method == "POST":
        getName = request.form["name"]
        getAddress = request.form["address"]
        getEmail = request.form["email"]
        getPhone = request.form["mobile"]
        getPass = request.form["pwd"]
        getCfnpass = request.form["cfnpwd"]
        print(getName)
        print(getAddress)
        print(getEmail)
        print(getPhone)
        print(getPass)
        print(getCfnpass)
        try:
            if getPass == getCfnpass :
                cursor.execute("INSERT INTO USERS(name, address, email, phone, password) VALUES('"+getName+"','"+getAddress+"','"+getEmail+"','"+getPhone+"','"+getPass+"')")
                print("Successfully created.")
                con.commit()
            else:
                print("Password mismatch")
        except Exception as e:
            print(e)

    return render_template("userreg.html")


@app.route("/crimereport", methods=["GET","POST"])
def register():
    if not session.get("name"):
        return redirect("/userlogin")
    else:
        if request.method == "POST":
            getDescription = request.form["description"]
            getRemarks = request.form["remark"]
            getDate = str(today)
            print(getDescription)

            print(getRemarks)
            print(getDate)
        try:
            con.execute("INSERT INTO CRIMES(DESCRIPTION, REMARKS, DATE) VALUES('"+getDescription+"','"+getRemarks+"','"+getDate+"')")
            print("Successfully inserted.")
            con.commit()
        except Exception as e:
            print(e)

    return render_template("crimereport.html")

@app.route("/guestreport", methods=["GET","POST"])
def guestregister():
    if request.method == "POST":
        getDescription = request.form["description"]
        getRemarks = request.form["remark"]
        getDate = str(today)
        print(getDescription)
        print(getRemarks)
        print(getDate)
        try:
            con.execute("INSERT INTO CRIMES(DESCRIPTION, REMARKS) VALUES('"+getDescription+"','"+getRemarks+"','"+getDate+"')")
            print("Successfully inserted.")
            con.commit()
        except Exception as e:
            print(e)

    return render_template("guestreport.html")


@app.route("/crimesearch", methods=["GET","POST"])
def search():
    if request.method == "POST":
        getDate = request.form["date"]
        print(getDate)
        try:
            cursor.execute("SELECT * FROM CRIMES WHERE DATE='"+getDate+"'")
            q = cursor.fetchall()
            if len(q) == 0:
                print("Invalid date")
            else:
                print("Search successful")
                print(len(q))
                return render_template("crimesearch.html", crime=q, status=True)
        except Exception as e:
            print(e)

    return render_template("crimesearch.html", crime=[], status=False)


@app.route("/useredit",methods=["GET","POST"])
def update():
    if not session.get("name"):
        return redirect("/userlogin")
    else:
        if request.method == "POST":
            getName = request.form["name"]
            print(getName)
        try:
            cursor.execute("SELECT * FROM USERS WHERE NAME='"+getName+"'")
            print("Selected a user")
            r = cursor.fetchall()
            if len(r)==0:
                print("Invalid name")
            else:
                print(len(r))
                return render_template("viewupdate.html", crime=r)

        except Exception as e:
            print(e)
    return render_template("useredit.html")

@app.route("/viewupdate", methods = ['GET','POST'])
def viewupdate():
    if request.method == "POST":
        getName = request.form["name"]
        getAddress = request.form["address"]
        getEmail = request.form["email"]
        getPhone = request.form["mobile"]
        getPass = request.form["pwd"]
        getCfnpass = request.form["cfnpwd"]
        print(getName)
        print(getAddress)
        print(getEmail)
        print(getPhone)
        print(getPass)
        print(getCfnpass)
        try:
            if getPass == getCfnpass:
                cursor.execute("INSERT INTO USERS(name, address, email, phone, password) VALUES('" + getName + "','" + getAddress + "','" + getEmail + "','" + getPhone + "','" + getPass + "')")
                print("Successfully created.")
                con.commit()
            else:
                print("Password mismatch")
        except Exception as e:
            print(e)

    return render_template("viewupdate.html")

@app.route("/viewallcrime")
def viewall():
    cursor.execute("SELECT * FROM CRIMES")
    r = cursor.fetchall()
    return render_template("viewallcrime.html", patients=r)

@app.route("/userlogout", methods=["GET","POST"])
def usrlogout():
    if not session.get("name"):
        return redirect("/userlogin")
    else:
        session["name"] = None
        return redirect("/")


if __name__=="__main__":
    app.run(debug=True)