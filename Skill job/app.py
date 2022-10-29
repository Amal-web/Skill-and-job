from flask import Flask,render_template,redirect,url_for,request
import sqlite3 as sql
import uuid

app=Flask(__name__,static_folder="static")

@app.route("/user/signin",methods=["POST","GET"])
def userlogin():
    if request.method=="GET":
        return render_template("./user/signin.html")

    else:
        email=request.form["email"]
        password=request.form["password"]
        print(email,password)

        with sql.connect("users.db") as con:
            cursor=con.cursor()
            cursor.execute("SELECT email,password FROM users WHERE email=?",(email,))
            user=cursor.fetchone()
            print(user)
            print(user[1])
            
            if user:
                if password==user[1]:
                    return redirect("/user/newsfeed")

                else:
                    return "Password Invalid"

            else:
                return "Invalid Response"



@app.route("/user/signup",methods=["POST","GET"])
def signup():
    if request.method=="GET":
        return render_template("./user/signup.html")

    else:
        name=request.form["name"]
        email=request.form["email"]
        phone=request.form["number"]
        password=request.form["password"]
        re_password=request.form["re-password"]
        key=uuid.uuid1().hex
        print(name,email,phone,password,re_password,key)

        if password==re_password:
            print("password matched")

            with sql.connect("users.db") as con:
            
                cur=con.cursor();
                cur.execute("INSERT INTO users (id,name,email,phone,password) VALUES (?,?,?,?,?)",(key,name,email,phone,password))
                con.commit()

                print("successfully added")
                return redirect("/user/newsfeed")
        else:
            return "Invalid Response"


@app.route("/user/profile")
def userprofile():
    return render_template("./user/profile.html")

@app.route("/user/profile/editprofile",methods=["POST","GET"])
def editprofile():
    if request.method=="GET":
        return render_template("./user/editprofile.html")

    else:
        name=request.form["name"]
        about=request.form["about"]
        email=request.form["email"]
        phone=request.form["phone"]
        designation=request.form["designation"]
        school=request.form["school"]
        skills=request.form["skills"]
        project=request.form["project"]
        description=request.form["description"]

        print(name,about,email,phone,designation,school,skills,project,description)
        
        with sql.connect("users.db") as con:
            cursor=con.cursor()
            cursor.execute("INSERT INTO userdata (name,about,email,phone,designation,school,skills,project,description) VALUES (?,?,?,?,?,?,?,?,?)",
            (name,about,email,phone,designation,school,skills,project,description))
            con.commit()

            print("added success fully")
            return "success"



@app.route("/user/jobs")
def jobs():
    return render_template("./user/jobs.html")


@app.route("/user/newsfeed")
def addproject():
    return render_template("./user/newsfeed.html")

if __name__=='__main__': 
    app.run(port=3000,debug=True)