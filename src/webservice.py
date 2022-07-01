from flask import*

from src.dbconnection import *

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

app=Flask(__name__)


@app.route('/login',methods=['post'])
def login():
    print(request.form)
    username=request.form['username']
    password=request.form['password']
    qry="select * from `login` where username=%s and `password`=%s and type='user'"
    val=(username,password)
    s=select1(qry,val)
    if s is None:
        return jsonify({'task':'invalid'})
    else:
        id=s[0]
        return jsonify({'task':'valid',"id" : id })


@app.route('/register', methods=['post'])
def reg():
     print(request.form)
     try:

            firstname = request.form['Fname']
            lastname = request.form['Lname']
            phoneno= request.form ['phn']
            mailid=request.form['Email']
            age=request.form['Age']
            gender=request.form['gender']
            place=request.form['Place']
            Post=request.form['Post']
            pin=request.form['Pin']
            username=request.form['uname']
            password=request.form['pwrd']
            repassword=request.form['rpwrd']
            qry = "INSERT INTO `login` VALUES(NULL,%s,%s,'user')"
            val = (username,password)
            s = iud(qry, val)
            if password==repassword:
                qry1="insert into `user_details` values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val1=(str(s),firstname,lastname,phoneno,mailid,age,gender,place,Post,pin)
                iud(qry1,val1)
                return jsonify({'task':'success'})
            else:
                return jsonify({'task': 'failed'})


     except Exception as e:
            print(e)
            return jsonify({'task': 'error'})




@app.route('/emergency',methods=['post'])
def emergency():

    try:
        uid=request.form['uid']
        message=request.form['message']
        latitude=request.form['latitude']
        longitude=request.form['longitude']
        q="SELECT `police_station_details`.*, (3959 * ACOS ( COS ( RADIANS('"+latitude+"') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('"+longitude+"') ) + SIN ( RADIANS('"+latitude+"') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM `police_station_details` order by user_distance"
        s=select(q)
        for i in s:
            print("hiiiiiiiiiiiiiii=========================")
            pid=str(i[1])
            qry="INSERT INTO `emergency` VALUES(NULL,%s,%s,%s,%s,%s,now())"
            val=(uid,pid,message,latitude,longitude)
            iud(qry,val)
            return jsonify({'task': 'success'})
    except Exception as e:
            print(e)
            return jsonify({'task': 'error'})



@app.route('/sendfeedback',methods=['post'])
def feedback():
    print(request.form)
    try:
        loginid=request.form['lid']

        fback_cmnd=request.form['feedback']
        rating=request.form['rating']

        qry = "INSERT INTO `feedback` VALUES(NULL,%s,'user',%s,%s,curdate(),'pending')"
        val = (loginid,fback_cmnd,rating)
        iud(qry, val)

        return jsonify({'task': 'success'})
    except Exception as e:
        print(e)
        return jsonify({'task': 'error'})

@app.route('/sendcomplaint',methods=['post'])
def sendcomplaint():
    print(request.form)
    try:
        pid=request.form['pid']
        compt=request.form['content']

        uid=request.form['lid']
        qry="INSERT INTO `complaint`VALUES(null,%s,%s,%s,curdate(),'pending')"
        val=(uid,pid,compt)
        iud(qry,val)
        return jsonify({'task': 'Success'})
    except Exception as e:
        print(e)
        return jsonify ({'task': 'error'})



@app.route('/viewcomplaint',methods=['post'])
def viewcomplaint():
    print(request.form)
    try:

        uid=request.form['lid']
        qry="SELECT complaint.*,`police_station_details`.`pname` FROM `complaint` JOIN `police_station_details` ON `police_station_details`.`lid`=`complaint`.`pid` WHERE `complaint`.`uid`=%s"
        val=(uid)
        res=androidselectall(qry,val)
        print(res)
        return jsonify(res)
    except Exception as e:
        print(e)
        return jsonify ({'task': 'error'})


@app.route('/viewpoliceinformation',methods=['post'])
def viewpoliceinformation():
    qry="SELECT * FROM police_station_details"
    res=androidselectallnew(qry)
    return jsonify(res)

@app.route('/viewpname_id',methods=['post'])
def viewpname_id():
    qry="SELECT `police_station_details`.lid as pid,pname FROM `police_station_details`;"
    res=androidselectallnew(qry)
    print(res)
    return jsonify(res)

@app.route('/viewnotification',methods=['post'])
def viewnotification():
    qry="SELECT `notification`.*,`police_station_details`.`pname` FROM `notification` JOIN `police_station_details` ON `notification`.`pid`=`police_station_details`.`lid`"
    res=androidselectallnew(qry)
    return jsonify(res)

@app.route('/viewfeedbackandcmnd',methods=['post'])
def viewfeedbackandcmnd():
    id=request.form['lid']
    qry="SELECT * FROM `feedback` WHERE `loginid`=%s"
    val=(id,)
    res=androidselectall(qry,val)
    return jsonify(res)

@app.route('/forgotpwd',methods=['get','post'])
def forgotpwd():
    email=request.form['email']
    username=request.form['uname']
    q="SELECT `password` FROM `login` WHERE username=%s"
    v=username
    s1 = selectone(q,v)
    print(s1)
    pwd = s1[0]
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('personalsafetyapp123@gmail.com', 'personalsafety')
    except Exception as e:
        print("Couldn't setup email!!" + str(e))
    msg = MIMEText("Your password is : " +pwd )
    print(msg)
    msg['Subject'] = 'Personal safety App'
    msg['To'] = email
    msg['From'] = 'personalsafetyapp123@gmail.com'
    try:
        gmail.send_message(msg)
    except Exception as e:
        print("COULDN'T SEND EMAIL", str(e))
    # con.commit()
    return jsonify({'task':'valid'})



#
# @app.route('/viewlocationservice',methods=['post'])
# def viewlocationservice():
#     try:
#     locid = request.form['locid']
#     lati = request.form['latitude']
#     longi = request.form['longitude']
#     qry = "INSERT INTO `location` VALUES(NULL,%s,%s)"
#     val =
#     iud(qry, val)
#     return jsonify({'task': 'success'})
#     except Exception as e:\
#         print(e)
#     return jsonify({'task': 'error'})

if __name__ =="__main__":
    app.run(host="0.0.0.0",port=5000)
