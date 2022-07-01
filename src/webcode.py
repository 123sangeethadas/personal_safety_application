from flask import *
from src.dbconnection import *
app=Flask(__name__)
app.secret_key="qwerty"
@app.route('/')
def main():
    # return render_template('index1.html')
    return render_template('Login.html')

@app.route('/about')
def about():
    # return render_template('index1.html')
    return render_template('indexabout.html')


@app.route('/contact')
def contact():
    # return render_template('index1.html')
    return render_template('indexcon.html')


@app.route('/login',methods=['post'])
def login():
    uname=request.form['textfield']
    passwd=request.form['textfield2']
    qry="select * from login where username=%s and password=%s"
    val=(uname,passwd)
    res=select1(qry,val)
    if res is None:
        return'''<script>alert("invalid");window.location="/"</script>'''
    elif res[3]=="admin":
        return '''<script>alert("success");window.location="/admin"</script>'''
    elif res[3] == "police":
        session['lid']=str(res[0])
        return '''<script>alert("success");window.location="/policestation"</script>'''

    else:
        return'''<script>alert("invalid");window.location="/"</script>'''








@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/viewregistereduser')
def viewregistereduser():
    qry="SELECT * FROM `user_details`"
    res=select(qry)
    return render_template('view registereduser.html',val=res)

@app.route('/viewfeedbackandrating')
def viewfeedback():

        q="SELECT `police_station_details`.pmail,`feedback`.* FROM `police_station_details` JOIN `feedback` WHERE `police_station_details`.lid=`feedback`.loginid union SELECT `user_details`.`mailid`,`feedback`.* FROM `user_details` JOIN `feedback` WHERE `user_details`.loginid=feedback.loginid";
        r=select(q);
        return render_template('view feedback and rating.html', val=r)
    # else:
    #     q="SELECT `user_details`.`mailid`,`feedback`.* FROM `user_details` JOIN `feedback` WHERE `user_details`.loginid=feedback.loginid";
    #     r=select(q);
    #     return render_template('view feedback and rating.html', val=r)




@app.route('/addormodify')
def addormodify():
    qry="SELECT * FROM `police_station_details`"
    res=select(qry)

    return render_template('add or modify police station.html',val=res)

@app.route('/addpolicestation',methods=['get','post'])
def addpolicestation():
    return render_template('add police station.html')
@app.route('/deletepolicestation',methods=['get','post'])
def deletepolicestation():
    lid=request.args.get('id')
    qry="DELETE FROM `login` WHERE `loginid`=%s"
    val=(lid,)
    iud(qry,val)
    qry="DELETE FROM `police_station_details` WHERE `lid`=%s"
    iud(qry, val)
    return redirect('/addormodify')



@app.route('/insertpolicestation',methods=['get','post'])
def insertpolicestation():
    pname=request.form['textfield']
    phoneno=request.form['textfield2']
    email=request.form['textfield3']
    place=request.form['textfield4']
    post=request.form['textfield5']
    pincode=request.form['textfield6']
    username=request.form['textfield7']
    password=request.form['textfield8']
    longitude=request.form['textfield9']
    latitude=request.form['textfield10']
    qry="INSERT INTO `login` VALUES(NULL,%s,%s,'police')"
    val=(username,password)
    id=iud(qry,val)
    qry="INSERT INTO `police_station_details` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(id),pname,phoneno,email,place,post,pincode,latitude,longitude)
    iud(qry,val)
    return redirect('/addormodify')


@app.route('/policestation')
def policestation():
    return render_template('police station.html')

@app.route('/viewemrgency')
def viewemergency():
    qry="SELECT `emergency`.*,`user_details`.`firstname`,`lastname` FROM `user_details` JOIN `emergency` ON `emergency`.`uid`=`user_details`.`loginid` WHERE `emergency`.`pid`=%s"
    val=(session['lid'],)
    res=selectall(qry,val)
    return render_template('view emergency message.html',val=res)

@app.route('/viewcomplaints')
def viewcomplaints():
    qry="SELECT `complaint`.*,`user_details`.`firstname`,`lastname` FROM `user_details` JOIN `complaint` ON `complaint`.`uid`=`user_details`.`loginid` WHERE `complaint`.`replay`='pending' AND `complaint`.`pid`=%s"
    val=(session['lid'])
    res = selectall(qry, val)
    return render_template('view complaints and send replay.html',val=res)

@app.route('/sendreplay')
def sendreplay():
    cid=request.args.get('cid')
    session['cid']=str(cid)
    return render_template('send replay.html')

@app.route('/sendreplay1',methods=['post'])
def sendreplay1():
    reply=request.form['textarea']
    qry="UPDATE `complaint` SET `replay`=%s WHERE `pcid`=%s"
    val=(reply,session['cid'])
    iud(qry,val)
    return redirect('/viewcomplaints')


@app.route('/sendfeedback')
def sendfeedback():
    return render_template('send feedback.html')


@app.route('/insertfeedback',methods=['post'])
def insertfeedback():
    feedback=request.form['textarea']
    rating=request.form['r']

    qry="INSERT INTO `feedback` VALUES(NULL,%s,'police',%s,%s,CURDATE(),'pending')"
    val=(session['lid'],feedback,rating)
    iud(qry,val)
    return '''<script>alert("success");window.location="/policestation"</script>'''


@app.route('/sendnotification')
def sendnotification():
    qry="SELECT * FROM `notification` WHERE `pid`=%s"
    val=(session['lid'])
    res=selectall(qry,val)
    return render_template('send notification.html',val=res)



@app.route('/addnotification',methods=['get','post'])
def addnotification():
    return render_template("add notification.html")


@app.route('/deletenoti',methods=['get','post'])
def deletenoti():
    id=request.args.get('id')
    qry="DELETE FROM `notification` WHERE `nid`=%s"
    val=(id)
    iud(qry,val)
    return redirect('/sendnotification')


@app.route('/insertnotification',methods=['get','post'])
def insertnotification():
    notification=request.form['textarea']
    qry="INSERT INTO `notification` VALUES(NULL,%s,%s,CURDATE())"
    val=(session['lid'],notification)
    iud(qry,val)
    return redirect('/sendnotification')

@app.route('/editpolice')
def editpolice():
    id=request.args.get('id')
    qry="SELECT * FROM `police_station_details` WHERE `lid`=%s"
    val=(id,)
    res=selectone(qry,val)
    return render_template('edit police station.html',i=res)



@app.route('/updatep',methods=['post'])
def updatep():
    id=request.form['lid']
    pname=request.form['textfield']
    phone=request.form['textfield2']
    email=request.form['textfield3']
    place=request.form['textfield4']
    post=request.form['textfield5']
    pin=request.form['textfield6']
    latti=request.form['textfield9']
    longi=request.form['textfield10']
    qry="UPDATE `police_station_details` SET `pname`=%s,`pphone`=%s,`pmail`=%s,`place`=%s,`post`=%s,`pin`=%s,`latitude`=%s,`longitude`=%s WHERE `lid`=%s"
    val=(pname,phone,email,place,post,pin,latti,longi,id)
    iud(qry,val)
    return '''<script>alert("success");window.location="/addormodify"</script>'''



app.run(debug=True)
