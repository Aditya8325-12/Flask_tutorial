from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home_get():
    return render_template('home.html',message='user not login ')

@app.route("/",methods=['POST'])
def home():
    login_username=request.form['username']
    login_password=request.form['password']
    file=open("register.txt",'r')
    msg=False
    for line in file:
        user_list=line.split(",")
        if login_username==user_list[0] and login_password==user_list[1]:
            msg=True
    if msg==True:
        return render_template("home.html",username=login_username,password=login_password)
    else:
        return redirect(url_for('login_get'))

@app.route("/regi")
def reg():
    return render_template("register.html")

@app.route("/login")
def login_get():
    return render_template("login.html",message='plese enter the username  and password')


@app.route('/login',methods=['POST'])
def login():
        name=request.form['name']
        username=request.form['username']
        password=request.form['password']
        try:
            file=open("register.txt",'a')
            file.write(username+","+password+","+name+"\n")
            file.close()
            return render_template('login.html')
        except:
            return redirect(url_for('home'))
    
if __name__=='__main__':
    app.run(debug=True)
    
