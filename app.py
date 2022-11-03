

import pymysql
from functions import *
from flask import *
import datetime
from werkzeug.utils import secure_filename
import os
import pymysql.cursors

connection = pymysql.connect(host = 'localhost', user = 'root', password = '', database = '4RLS')

app = Flask(__name__)
app.secret_key = "QWSERRdsr4948948*/*/8776tdhd" # session id will be encrypted using this key
UPLOAD_FOLDER = "static/images"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024 # Only accepting images worth 4mbs
ALLOWED_EXTENSIONS = set(
    [
        'png', 'jpg', 'jpeg', 'webp'
    ]
)

def allowed_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# print(allowed_files(""))

# function checking sessions

def check_user():
    if 'user_id' in session:
        return True
    else:
        return False

def check_role():
    if 'role' in session:
        role = session['role']
        return role
    else:
        session.clear()
        return redirect('/login')

def get_userid():
    if 'user_id' in session:
        user_id = session['user_id']
        return user_id
    else:
        session.clear()
        return redirect('/login')

@app.route('/logout')
def logout():
    # session.pop('user_id', None)
    session.clear()
    return redirect('/login')

@app.route('/login', methods = ['POST', 'GET'])

# def login(email, password):
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        sql = "select * from admin where email = %s"
        cursor = connection.cursor()
        cursor.execute(sql, email)
        if cursor.rowcount == 0:
            # print("Your email does not exist")
            return render_template('login.html', message = 'Your email does not exist')
        else:
            row = cursor.fetchone()
            if row[6] == 'inactive':
                # print("Your account is inactive. Wait for approval")
                return render_template('login.html', message = 'Your account is inactive. Wait for approval')
            elif row[6] == 'active':
                hash_pswd = row[7] # hashed password from database
                status = password_verify(password, hash_pswd) # verifying hashed password is same with database
                if status:
                    # password_verify(password, hash_pswd) == True:
                    phone = row[5] # encrypted data
                    decryptphone = decrypt(phone)
                    print("Phone number:", decryptphone)
                    otp = randomizer()
                    send_sms(decryptphone, "Your OTP is {}, Do not share with anyone".format(otp))
                    time = datetime.datetime.now()
                    sqlotp = "update admin set otp = %s, otptime = %s where email = %s"
                    cursor = connection.cursor()
                    cursor.execute(sqlotp, (password_hash(otp), time, email))
                    connection.commit()
                    cursor.close()

    #                  activating sessions
    #                 session['userid'] = row[0]
                    session['fname'] = row[1]
                    # session['role'] = row[9]
                    session['email'] = row[4]

                    return redirect('/conotp')

    # TODO HTML UI

                else:
                    return render_template('login.html', message = 'Wrong credentials. Try again')
                    # print("Wrong credentials. Try again")

    else:
        return render_template('login.html')

# login("email@gmail.com", "nairobi1234")

@app.route('/conotp', methods = ['POST', 'GET'])
def conotp():
    if 'email' in session:
        if request.method == 'POST':
            email = session['email']
            otp = request.form['otp']
            sql = "select * from admin where email = %s"
            cursor = connection.cursor()
            cursor.execute(sql, email)
            row = cursor.fetchone()
            otp_hash = row[11]
            optime = row[12]

            # converting otptime from str to datetime

            prev_time = datetime.datetime.strptime(optime, '%Y-%m-%d %H:%M:%S.%f')
            # get time now
            time_now = datetime.datetime.now()
            # finding difference
            diff = time_now - prev_time
            if diff.total_seconds() > 30:
                render_template('conotp.html', message = "Your OTP has expired!")
                return render_template('login.html')
            else:
                status = password_verify(otp, otp_hash)
                if status:
                    session['user_id'] = row[0]
                    session['fname'] = row[1]
                    session['role'] = row[9]
                    session['prof_pic'] = row[13]
                    return redirect('/')
                else:
                    return render_template('conotp.html', message = "Wrong OTP")
        return render_template('conotp.html')

    else:
        return redirect('/login')

@app.route('/')
def dashboard():
    sqldrivers = "select * from drivers"
    cursord = connection.cursor()
    cursord.execute(sqldrivers)
    no_of_drivers = cursord.rowcount

    sqldrivers2 = "select * from drivers where status = %s"
    cursord2 = connection.cursor()
    cursord2.execute(sqldrivers2, "Allocated")
    alloc_drivers = cursord2.rowcount

    sqldrivers3 = "select * from drivers where status = %s"
    cursord3 = connection.cursor()
    cursord3.execute(sqldrivers3, "Not allocated")
    not_alloc = cursord3.rowcount

    sqldrivers4 = "select * from vehicle_service where status = %s"
    cursord4 = connection.cursor()
    cursord4.execute(sqldrivers4 ,"Pending")
    pending_services = cursord4.rowcount

    cursord.close()
    cursord2.close()
    cursord3.close()
    cursord4.close()






    if check_user():
        return render_template("dashboard.html", not_alloc = not_alloc, no_of_drivers = no_of_drivers, alloc_drivers = alloc_drivers, pending_services=pending_services)
    else:
        return redirect('/login')

@app.route('/addmake', methods = ['POST', 'GET'])
def addmake():
    if check_user() and check_role() == "admin":
        if request.method == 'POST':
            make = request.form['make']
            if not make:
                return jsonify({'error1':'Please enter make'})
            else:
                cursor = connection.cursor()
                sql = "insert into vehicle_make(make_name) values(%s)"
                try:
                    cursor.execute(sql, (make))
                    connection.commit()
                    return jsonify({'success': 'Make added'})
                except:
                    connection.rollback()
                    return jsonify({'error2': 'Error occured, please try again!'})
        else:
            return render_template('admin/addmake.html')

    else:
        return redirect('/login')

@app.route('/addlocation', methods = ['POST', 'GET'])
def addlocation():
    if check_user() and check_role() == "admin":
        if request.method == 'POST':
            make = request.form['make']
            if not make:
                return jsonify({'error1':'Please enter location'})
            else:
                cursor = connection.cursor()
                sql = "insert into locations(loc_name) values(%s)"
                try:
                    cursor.execute(sql, (make))
                    connection.commit()
                    return jsonify({'success': 'Location added'})
                except:
                    connection.rollback()
                    return jsonify({'error2': 'Error occured, please try again!'})
        else:
            return render_template('admin/addlocation.html')

    else:
        return redirect('/login')

@app.route('/addtype', methods = ['POST', 'GET'])
def addtype():
    if check_user() and check_role() == "admin":
        if request.method == 'POST':
            type = request.form['type']
            if not type:
                return jsonify({'error1':'Please enter type'})
            else:
                cursor = connection.cursor()
                sql = "insert into vehicle_type(type_name) values(%s)"
                try:
                    cursor.execute(sql, (type))
                    connection.commit()
                    return jsonify({'success': 'Type added'})
                except:
                    connection.rollback()
                    return jsonify({'error2': 'Error occured, please try again!'})
        else:
            return render_template('admin/addtype.html')

    else:
        return redirect('/login')

@app.route('/adduser', methods = ['POST', 'GET'])
def adduser():
    if check_user() and check_role() == "admin":
        if request.method == 'POST':
            fname = request.form['fname']
            lname = request.form['lname']
            surname = request.form['surname']
            gender = request.form['gender']
            password = randomizer()
            role = request.form['role']
            phone = request.form['phone']
            email = request.form['email']
            regex = "^\+254\d{9}"

            if not fname:
                return jsonify({'errorfname':'Please enter first name'})
            elif not lname:
                return jsonify({'errorlname':'Please enter last name'})
            # elif not surname:
            #     return jsonify({'errorsurname':'Please enter surname'})
            elif not gender:
                return jsonify({'errorgender':'Please enter gender'})
            elif role not in ['admin', 'finance', 'operations', 'guests', 'service']:
                return jsonify({'errorrole':'Invalid role!'})
            elif len(phone) < 13:
                return jsonify({'errorphone':'Please enter valid phone no. i.e +254XXXXXXXXX'})
            elif not emailval(email):
                return jsonify({'erroremail':'Please enter valid email'})

            else:

                sqlcheck = "select * from admin where email = %s"
                cursor = connection.cursor()
                cursor.execute(sqlcheck, (email))
                if cursor.rowcount > 0:
                    return jsonify({'erroremail': 'Email already exists'})
                else:
                    cursor = connection.cursor()
                    sql = "insert into admin(fname, lname, surname, email, phone, password, gender, role) values(%s, %s, %s, %s, %s, %s, %s, %s)"
                    try:
                        cursor.execute(sql, (fname, lname, surname, email, encypt(phone), password_hash(password), gender, role))
                        connection.commit()
                        message = ''' "Hello {}, you are signed in as {}. 
                        Login in using your email. Your password is {}" '''.format(fname, role, password)
                        send_sms(phone, message)
                        return jsonify({'success': 'User added'})
                    except:
                        connection.rollback()
                        return jsonify({'error2': 'Error occured, please try again!'})
        else:
            return render_template('admin/adduser.html')

    else:
        return redirect('/login')

@app.route('/addmodel', methods = ['POST', 'GET'])
def addmodel():
    if check_user() and check_role() == "admin":
        if request.method == 'POST':
            model = request.form['model']
            make_id = request.form['make_id']
            if not model or not make_id:
                return jsonify({'error1':'Empty fields'})
            else:
                cursor = connection.cursor()
                sql = "insert into vehicle_model(make_id, model_name) values(%s, %s)"
                try:
                    cursor.execute(sql, (make_id, model))
                    connection.commit()
                    return jsonify({'success': 'Model added'})
                except:
                    connection.rollback()
                    return jsonify({'error2': 'Error occured, please try again!'})
        else:
            # GETTING MAKES FROM DB
            makes = getmakes()
            return render_template('admin/addmodel.html', makes = makes)

    else:
        return redirect('/login')

@app.route('/addowner', methods = ['POST', 'GET'])
def addowner():
    if check_user() and check_role() == "admin":
        if request.method == 'POST':
            fname = request.form['fname']
            surname = request.form['surname']
            lname = request.form['lname']
            phone = request.form['phone']
            email = request.form['email']
            address = request.form['address']
            loc_id = request.form['loc_id']
            # passport_pic = request.form['passport_pic']
            id_no = request.form['id_no']
            dob = request.form['dob']
            user_id = get_userid()
            password = randomizer()
            files = request.files.getlist("files[]")
            for file in files:
                if file and allowed_files(file.filename):
                    filename = secure_filename(file.filename)
                    #adding random strings to filename
                    uniquefilename = "{}{}".format(randomizer(), filename)
                    try:
                        #upload file using that name
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], uniquefilename))
                        session['uniquefilename'] = uniquefilename
                    except Exception as error:
                        session['uniquefilename'] = ""
                        print("Upload error", error)
                else:
                    return jsonify({"error":"Invalid file, upload only png, jpeg, jpg."})

            if not fname:
                return jsonify({'error':'Please enter first name'})
            elif not lname:
                return jsonify({'error':'Please enter last name'})
            elif not emailval(email):
                return jsonify({'error':'Please enter valid email'})
            elif not id_no:
                return jsonify({'error':'Please enter ID number'})
            elif not phonevalid(phone):
                return jsonify({'error':'Invalid phone number. +254XXXXXXXX'})
            elif not dob:
                return jsonify({'error':'Please enter your date of birth'})
            else:
                cursor = connection.cursor()
                sql = "insert into owners(fname, surname, lname, phone, email,address, loc_id, passport_pic, id_no, dob, user_id, password) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                try:
                    cursor.execute(sql, (fname, surname, lname, encypt(phone), email,address, loc_id, session['uniquefilename'], id_no, dob, user_id, password_hash(password)))
                    connection.commit()
                    message = "Thankyou for joining UE4. Download the application from the link provided and login with your email and password: {} to get started".format(password)
                    send_sms(phone, message)
                    return jsonify({'success': 'Owner added'})
                except:
                    connection.rollback()
                    return jsonify({'error2': 'Error occured, please try again!'})
        else:
            # GETTING MAKES FROM DB
            locations = getloc()
            print("works")
            return render_template('admin/addowner.html', locations = locations)


    else:
        return redirect('/login')
    
@app.route('/adddriver', methods = ['POST', 'GET'])
def adddriver():
    if check_user() and check_role() == "admin":
        print("works")
        if request.method == 'POST':
            fname = request.form['fname']
            print("works2")
            surname = request.form['surname']
            lname = request.form['lname']
            phone = request.form['phone']
            email = request.form['email']
            dl_no = request.form['dl_no']
            dl_no_expiry = request.form['dl_no_expiry']
            # passport_pic = request.form['passport_pic']
            loc_id = request.form['loc_id']
            dob = request.form['dob']
            con_id = request.form['con_id']
            password = randomizer()
            user_id = get_userid()
            files = request.files.getlist("files[]")
            print("works2")
            for file in files:
                if file and allowed_files(file.filename):
                    filename = secure_filename(file.filename)
                    #adding random strings to filename
                    uniquefilename = "{}{}".format(randomizer(), filename)
                    try:
                        #upload file using that name
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], uniquefilename))
                        session['uniquefilename'] = uniquefilename
                    except Exception as error:
                        session['uniquefilename'] = ""
                        print("Upload error", error)
                else:
                    return jsonify({"error":"Invalid file, upload only png, jpeg, jpg."})

            print("working")
            if not fname:
                return jsonify({'error':'Please enter first name'})
            elif not lname:
                return jsonify({'error':'Please enter last name'})
            elif not emailval(email):
                return jsonify({'error':'Please enter valid email'})
            elif not dl_no:
                return jsonify({'error':'Please enter driver license number'})
            elif not phonevalid(phone):
                return jsonify({'error':'Invalid phone number. +254XXXXXXXX'})
            elif not dob:
                return jsonify({'error':'Please enter your date of birth'})
            elif not con_id:
                return jsonify({'error':'Please enter your contract ID'})
            else:
                cursor = connection.cursor()
                print("works")
                sql = "insert into drivers(fname, surname, lname, phone, email, dl_no, dl_no_expiry, passport_pic, loc_id, dob, con_id, password, user_id) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                try:
                    cursor.execute(sql, (fname, surname, lname, encypt(phone), email, dl_no, dl_no_expiry, session['uniquefilename'], loc_id, dob, con_id, password_hash(password), user_id))
                    connection.commit()
                    message = "Thankyou for joining UE4. Download the application from the link provided and login with your email and password: {} to get started".format(password)
                    send_sms(phone, message)
                    return jsonify({'success': 'Driver added'})
                except:
                    connection.rollback()
                    return jsonify({'error2': 'Error occured, please try again!'})
        else:
            # GETTING MAKES FROM DB
            locations = getloc()
            return render_template('admin/adddriver.html', locations = locations)


    else:
        return redirect('/login')

@app.route('/addvehicle', methods = ['POST', 'GET'])
def addvehicle():
    if check_user() and check_role() == "admin":
        if request.method == 'POST':
            reg_no = request.form['reg_no']
            type_id = request.form['type_id']
            make_id = request.form['make_id']
            model_id = request.form['model_id']
            capacity_id = request.form['capacity_id']
            color = request.form['color']
            weight = request.form['weight']
            no_of_pass = request.form['no_of_pass']
            # vehicle_pic = request.form['vehicle_pic']
            yom = request.form['yom']
            owner_id = request.form['owner_id']
            chassis_no = request.form['chassis_no']
            # password = randomizer()
            # user_id = get_userid()
            files = request.files.getlist("files[]")
            for file in files:
                if file and allowed_files(file.filename):
                    filename = secure_filename(file.filename)
                    #adding random strings to filename
                    uniquefilename = "{}{}".format(randomizer(), filename)
                    try:
                        #upload file using that name
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], uniquefilename))
                        session['uniquefilename'] = uniquefilename
                    except Exception as error:
                        session['uniquefilename'] = ""
                        print("Upload error", error)
                else:
                    return jsonify({"error":"Invalid file, upload only png, jpeg, jpg."})

            if not reg_no:
                return jsonify({'error':'Please enter registration number'})
            elif not type_id:
                return jsonify({'error':'Please enter the type'})
            elif not make_id:
                return jsonify({'error':'Please enter make'})
            elif not capacity_id:
                return jsonify({'error':'Please enter vehicle capacity'})
            elif not color:
                return jsonify({'error':'Please enter color'})
            elif not weight:
                return jsonify({'error':'Please enter weight of vehicle'})
            elif not no_of_pass:
                return jsonify({'error':'Please enter the max number of passengers'})
            elif not owner_id:
                return jsonify({'error':'Please enter owner ID'})
            elif not chassis_no:
                return jsonify({'error':'Please enter the chassis number'})
            else:
                cursor = connection.cursor()
                print("works")
                # ADD MODEL ERROR SERVER NOT UNDERSTAND
                sql = "insert into vehicles(reg_no, type_id, make_id, model_id, capacity_id, color, weight, no_of_pass, vehicle_pic, yom, owner_id, chassis_no) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                # try:
                # ADD MODEL ERROR SERVER NOT UNDERSTAND
                # ADD MODEL ERROR SERVER NOT UNDERSTAND
                cursor.execute(sql, (reg_no, type_id, make_id, model_id, capacity_id, color, weight, no_of_pass, session['uniquefilename'], yom, owner_id, chassis_no))
                connection.commit()
                # message = "Thankyou for joining UE4. Download the application from the link provided and login with your email and password: {} to get started".format(password)
                # send_sms(phone, message)
                return jsonify({'success': 'Vehicle added'})
                # except:
                #     connection.rollback()
                #     return jsonify({'error2': 'Error occured, please try again!'})
        else:
            # GETTING MAKES FROM DB
            types = gettypes()
            makes = getmakes()
            models = getmodels()
            capacitys = getcapacity()
            owners = getowner()
            # ADD MODEL ERROR SERVER NOT UNDERSTAND
            return render_template('admin/addvehicle.html', types = types, makes = makes, models = models, capacitys = capacitys, owners = owners)

            # locations = getloc()
            # return render_template('admin/addvehicle.html', locations = locations)


    else:
        return redirect('/login')

@app.route('/profile')
def profile():
    if check_user():
        user_id = get_userid() # get current userid to get details
        sql = 'select * from admin where user_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (user_id))
        row = cursor.fetchone()
        return render_template("profile.html", row = row)
    else:
        return redirect('/login')

@app.template_filter() # function called in template
def data_decrypt(encryptdata):
    decrypted = decrypt(encryptdata)
    return decrypted

@app.route('/changepassword', methods = ['POST', 'GET'])
def changepassword():
    if check_user():
        if request.method == 'POST':
            user_id = get_userid()
            current_pswd = request.form['current_pswd']
            new_pswd = request.form['new_pswd']
            con_pswd = request.form['con_pswd']

            sql = 'select * from admin where user_id = %s'
            cursor = connection.cursor()
            cursor.execute(sql, (user_id))
            row = cursor.fetchone()
            hashed_pswd = row[7]
            status = password_verify(current_pswd, hashed_pswd)
            if status:
                print("Current okay")
                response = password_check(new_pswd)
                if response == True:
                    print("New okay")
                    if new_pswd != con_pswd:
                        return jsonify({'conwrong': 'Passwords do not match!'})
                    else:
                        print("Confirm okay")
                        sql = 'update admin set password = %s where user_id = %s'
                        cursor = connection.cursor()
                        try:
                            cursor.execute(sql, (password_hash(new_pswd), user_id))
                            connection.commit()
                            return jsonify({'consuccess': 'Password changed'})
                        except:
                            connection.rollback()
                            return jsonify({'errorpswd': 'An error occurred, please try again'})
                else:
                    return jsonify({'newwrong': response})
            else:
                return jsonify({'currentwrong':'Wrong password'})


        else:
            return render_template('changepassword.html')
    else:
        return redirect('/login')

@app.route('/ownerlivesearch', methods = ['POST', 'GET'])
def ownerlivesearch():
    if check_user() and check_role() == "admin":
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        if request.method == 'POST':
            search_word = request.form['search_word']
            if search_word == '':
                sql = "select * from owners order by owner_id desc"
                cursor.execute(sql)
                owners = cursor.fetchall()
                count = cursor.rowcount
                print(owners)
                return jsonify(
                    {
                        'htmlresponse': render_template(
                            'views/ownerresponse.html', owners = owners, count = count, locations = getloc()
                        )
                    }
                )
            else:
                sql = "select * from owners Where phone LIKE '%{}%' or email LIKE '%{}%' or surname LIKE '%{}%' order by owner_id desc".format(
                    search_word, search_word, search_word
                )
                cursor.execute(sql)
                owners = cursor.fetchall()
                count = cursor.rowcount
                print(owners)
                return jsonify(
                    {
                        'htmlresponse': render_template(
                            'views/ownerresponse.html', owners=owners, count=count, locations = getloc()
                        )
                    }
                )
        else:
            return render_template('views/ownerui.html')

    else:
        return redirect('/login')

@app.route('/driverlivesearch', methods = ['POST', 'GET'])
def driverlivesearch():
    if check_user() and check_role() == "admin":
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        if request.method == 'POST':
            search_word = request.form['search_word']
            if search_word == '':
                sql = "select * from drivers order by driver_id desc"
                cursor.execute(sql)
                drivers = cursor.fetchall()
                count = cursor.rowcount
                print(drivers)
                return jsonify(
                    {
                        'htmlresponse': render_template(
                            'views/driverresponse.html', drivers = drivers, count = count, locations = getloc()
                        )
                    }
                )
            else:
                sql = "select * from drivers Where phone LIKE '%{}%' or email LIKE '%{}%' or surname LIKE '%{}%' order by driver_id desc".format(
                    search_word, search_word, search_word
                )
                cursor.execute(sql)
                drivers = cursor.fetchall()
                count = cursor.rowcount
                print(drivers)
                return jsonify(
                    {
                        'htmlresponse': render_template(
                            'views/driverresponse.html', drivers=drivers, count=count, locations = getloc()
                        )
                    }
                )
        else:
            return render_template('views/driverui.html')

    else:
        return redirect('/login')

@app.route('/vehiclelivesearch/<driver_id>', methods = ['POST', 'GET'])
def vehiclelivesearch(driver_id):
    if check_user() and check_role() == "admin":

        # put this driver_id in session
        sqlD = 'select * from drivers where driver_id = %s'
        cursor = connection.cursor()
        cursor.execute(sqlD, (driver_id))

        if cursor.rowcount == 0:
            return redirect("/driverlivesearch")
        else:
            row = cursor.fetchone()
            phone = decrypt(row[4])
            session['driver_id'] = driver_id
            session['driver_name'] = row[1] +" " + row[3]
            session['driver_phone'] = phone

        cursor = connection.cursor(pymysql.cursors.DictCursor)
        if request.method == 'POST':
            search_word = request.form['search_word']
            if search_word == '':
                sql = "select * from vehicles order by reg_no desc"
                cursor.execute(sql)
                vehicles = cursor.fetchall()
                count = cursor.rowcount
                print(vehicles)
                return jsonify(
                    {
                        'htmlresponse': render_template(
                            'views/vehicleresponse.html', vehicles=vehicles, capacitys=getcapacity(), makes = getmakes(), types = gettypes(), models = modellist(), count = count
                        )
                    }
                )
            else:
                sql = "select * from vehicles Where reg_no LIKE '%{}%' order by reg_no desc".format(
                    search_word, search_word, search_word
                )
                cursor.execute(sql)
                vehicles = cursor.fetchall()
                count = cursor.rowcount
                print(vehicles)
                return jsonify(
                    {
                        'htmlresponse': render_template(
                            'views/vehicleresponse.html', vehicles=vehicles, capacitys=getcapacity(), makes = getmakes(), types = gettypes(), models = modellist(), count = count
                        )
                    }
                )
        else:
            return render_template('views/vehicleui.html')

    else:
        return redirect('/login')

@app.route('/addvehicle/<owner_id>', methods = ['POST', 'GET'])
def addVehicle(owner_id):
    # encrypting owner_id as exposed to url
    if check_user() and check_role() == "admin":
        if request.method == 'POST':
            reg_no = request.form['reg_no']
            type_id = request.form['type_id']
            make_id = request.form['make_id']
            model_id = request.form['model_id']
            capacity_id = request.form['capacity_id']
            color = request.form['color']
            weight = request.form['weight']
            no_of_pass = request.form['no_of_pass']
            # vehicle_pic = request.form['vehicle_pic']
            yom = request.form['yom']
            owner_id = request.form['owner_id']
            chassis_no = request.form['chassis_no']
            user_id = get_userid()
            files = request.files.getlist("files[]")
            for file in files:
                if file and allowed_files(file.filename):
                    filename = secure_filename(file.filename)
                    #adding random strings to filename
                    uniquefilename = "{}{}".format(randomizer(), filename)
                    try:
                        #upload file using that name
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], uniquefilename))
                        session['uniquefilename'] = uniquefilename
                    except Exception as error:
                        session['uniquefilename'] = ""
                        print("Upload error", error)
                else:
                    return jsonify({"error":"Invalid file, upload only png, jpeg, jpg."})

            if not reg_no:
                return jsonify({'error':'Please enter registration number'})
            elif not yom or len(yom) != 4:
                return jsonify({'error':'Year invalid'})
            elif not capacity_id:
                return jsonify({'error':'Please enter vehicle capacity'})
            elif not color:
                return jsonify({'error':'Please enter color'})
            elif not no_of_pass:
                return jsonify({'error':'Please enter the max number of passengers'})
            elif not weight:
                return jsonify({'error':'Please enter weight of vehicle'})
            elif not chassis_no:
                return jsonify({'error':'Please enter the chassis number'})
            else:
                cursor = connection.cursor()
                # ADD MODEL ERROR SERVER NOT UNDERSTAND
                sql = "insert into vehicles(reg_no, type_id, make_id, model_id, capacity_id, color, weight, no_of_pass, vehicle_pic, yom, owner_id, chassis_no, user_id) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                try:
                    # ADD MODEL ERROR SERVER NOT UNDERSTAND
                    # ADD MODEL ERROR SERVER NOT UNDERSTAND
                    cursor.execute(sql, (
                    reg_no, type_id, make_id, model_id, capacity_id, color, weight, no_of_pass, session['uniquefilename'],
                    yom, owner_id, chassis_no, user_id))
                    connection.commit()
                    sql = "select * from owners where owner_id = %s"
                    cursor = connection.cursor()
                    cursor.execute(sql, (owner_id))
                    row = cursor.fetchone()
                    phone = decrypt(row[4])
                    message = "Dear {}, your vehicle {} has been added to our fleets. Download our app with the link below to track it".format(row[1], reg_no)
                    send_sms(phone, message)
                    return jsonify({'success': 'Vehicle added'})
                except:
                    connection.rollback()
                    return jsonify({'error2':'Vehicle not added'})
        else:
            # GETTING MAKES FROM DB
            types = gettypes()
            makes = getmakes()
            # models = getmodels()
            capacitys = getcapacity()
            owners = getowner()
            print("works")
            return render_template('admin/addvehicle.html', types = types, makes = makes, capacitys = capacitys, owner_id = owner_id)


    else:
        return redirect('/login')

@app.route('/viewvehicles/<owner_id>')
def viewvehicles(owner_id):
    if check_user() and check_role() == "admin":
        sql = "select * from vehicles where owner_id =%s"
        cursor = connection.cursor()
        cursor.execute(sql, (owner_id))
        if cursor.rowcount == 0:
            return render_template('views/viewvehicles.html', message = "No vehicles")
        else:
            vehicles = cursor.fetchall()
            return render_template('views/viewvehicles.html', vehicles = vehicles, makes = getmakes(), types = gettypes(), models = modellist(), owner_id = owner_id)

    else:
        return redirect('/login')

@app.route('/allocatedriver/<reg_no>')
def allocatedriver(reg_no):
    if check_user() and check_role() == "admin":
        driver_id = session['driver_id']
        phone = session['driver_phone']
        driver_name = session['driver_name']


        # fixing double entries
        sql = "select * from driver_allocations where driver_id = %s and alloc_status = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (driver_id, "active"))

        sql2 = "select * from driver_allocations where reg_no = %s and alloc_status = %s"
        cursor2 = connection.cursor()
        cursor2.execute(sql2, (reg_no, "active"))

        if cursor.rowcount > 0:
            row = cursor.fetchone()
            flash("Driver {} already allocated to vehicle {}".format(driver_name, row[2]), 'alert bg-warning')
            return redirect('/driverlivesearch')
        elif cursor2.rowcount > 0:
            row = cursor2.fetchone()
            flash("Vehicle {} already allocated to diver {}".format(reg_no, row[1]), 'alert bg-warning')
            return redirect('/driverlivesearch')
        else:
            sql = "insert into driver_allocations(driver_id, reg_no) values(%s, %s)"
            cursor = connection.cursor()
            try:
                cursor.execute(sql, (driver_id, reg_no))
                connection.commit()

                # updating
                sqlD = "update drivers set status = %s where driver_id = %s"
                cursorD = connection.cursor()
                cursorD.execute(sqlD, ("Allocated", driver_id))
                connection.commit()

                sqlV = "update vehicles set status = %s where reg_no = %s"
                cursorV = connection.cursor()
                cursorV.execute(sqlV, ("Allocated", reg_no))
                connection.commit()

                message = "Dear {}, you have been allocated to vehicle Reg {}. Please wait for more directions".format(driver_name, reg_no)
                # send_sms(phone, message)
                # clearing driver sessions
                session.pop("driver_id", None)
                session.pop("driver_name", None)
                session.pop("driver_phone", None)
                flash("Driver allocated", 'alert bg-success')
                return redirect('/driverlivesearch')
            except:
                session.pop("driver_id", None)
                session.pop("driver_name", None)
                session.pop("driver_phone", None)
                connection.rollback()
                flash("Driver not allocated", 'alert bg-danger')
                return redirect('/driverlivesearch')

    else:
        return redirect('/login')

@app.route('/allocatedvehicle/<driver_id>')
def allocatedvehicle(driver_id):
    if check_user() and check_role() == "admin":
        sql = "select * from driver_allocations where driver_id = %s and alloc_status = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (driver_id, "active"))
        row = cursor.fetchone()

        # pulling vehicle reg

        reg_no = row[2]

    #     more queries, finding car details

        sql3 = "select * from vehicles where reg_no = %s"
        cursor3 = connection.cursor()
        cursor3.execute(sql3, (reg_no))
        vehicles = cursor3.fetchall()
        return render_template("views/viewvehicles.html",  vehicles = vehicles, makes = getmakes(), types = gettypes(), models = modellist())

    else:
        return redirect('/login')

@app.route('/reallocate/<driver_id>')
def reallocate(driver_id):
    if check_user() and check_role() == 'admin':
        sql = "select * from driver_allocations where driver_id = %s and alloc_status = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (driver_id, 'active'))
        if cursor.rowcount == 0:
            flash("Failed! Driver not allocated", "alert bg-danger")
            return redirect('/driverlivesearch')
        else:
            row = cursor.fetchone()
            reg_no = row[2]
            sqlupdate1 = "update driver_allocations set alloc_status = %s where driver_id = %s"
            cursorupdate1 = connection.cursor()
            cursorupdate1.execute(sqlupdate1, ('inactive', driver_id))
            connection.commit()
            sqlupdate2 = "update drivers set status = %s where driver_id = %s"
            cursorupdate2 = connection.cursor()
            cursorupdate2.execute(sqlupdate2, ('Not allocated', driver_id))
            connection.commit()
            sqlupdate3 = "update vehicles set status = %s where reg_no = %s"
            cursorupdate3 = connection.cursor()
            cursorupdate3.execute(sqlupdate3, ('Not allocated', reg_no))
            connection.commit()
            flash("Success! Driver Deallocated", "alert bg-success")
            return redirect('/driverlivesearch')

    else:
        return redirect('/login')

@app.route('/assign/<driver_id>', methods = ['POST', 'GET'])
def assign(driver_id):
    if check_user() and check_role() == 'admin':
        if request.method == 'POST':
            reg_no = request.form['reg_no']
            from1 = request.form['from']
            to = request.form['to']
            scheduled_date = request.form['scheduled_date']
            scheduled_time = request.form['scheduled_time']
            sql = "insert into vehicle_task_allocation(`reg_no`, `driver_id`, `from`, `to`, `scheduled_date`, `scheduled_time`)values(%s, %s, %s, %s, %s, %s)"
            cursor = connection.cursor()
            try:
                cursor.execute(sql, (reg_no, driver_id, from1, to, scheduled_date, scheduled_time))
                connection.commit()
                #use driver id to get phone number and send sms notifying him
                sql = "select * from drivers where driver_id = %s"
                cursor = connection.cursor()
                cursor.execute(sql, (driver_id))
                row = cursor.fetchone()
                fname = row[1]
                phone = decrypt(row[4])
                message = "Dear {}, you've been assigned a trip from {} to {} on {} at {}.".format(fname, from1, to, scheduled_date, scheduled_time)
                send_sms(phone, message)
                return jsonify({'success':'Assignment added'})
            except:
                return jsonify({'error': 'Assignment failed'})
        else:
            sql = "select * from driver_allocations where driver_id = %s and alloc_status = %s"
            cursor = connection.cursor()
            cursor.execute(sql, (driver_id, 'active'))
            if cursor.rowcount == 0:
                flash("Failed! Driver not allocated", "alert bg-danger")
                return redirect('/driverlivesearch')
            else:
                row = cursor.fetchone()
                reg_no = row[2]
                session['driver_id'] = driver_id
                session['reg_no'] = reg_no
                return render_template('admin/assign.html')
    else:
        return redirect('/login')

@app.route('/assignlivesearch', methods = ['POST', 'GET'])
def assignlivesearch():
    if check_user() and check_role() == "admin" or "operations":
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        if request.method == 'POST':
            search_word = request.form['search_word']
            if search_word == '':
                sql = "select * from vehicle_task_allocation order by task_id desc"
                cursor.execute(sql)
                task = cursor.fetchall()
                count = cursor.rowcount
                print(task)
                return jsonify(
                    {
                        'htmlresponse': render_template(
                            'views/assignresponse.html', task = task, count = count
                        )
                    }
                )
            else:
                sql = "select * from vehicle_task_allocation Where task_id LIKE '%{}%' or scheduled_date LIKE '%{}%' or trip_completion_status LIKE '%{}%' order by driver_id desc".format(
                    search_word, search_word, search_word
                )
                cursor.execute(sql)
                task = cursor.fetchall()
                count = cursor.rowcount
                print(task)
                return jsonify(
                    {
                        'htmlresponse': render_template(
                            'views/assignresponse.html', task=task, count=count
                        )
                    }
                )
        else:
            return render_template('views/assignui.html')

    else:
        return redirect('/login')


@app.route('/send_service/<reg_no>', methods = ['POST', 'GET'])
def send_service(reg_no):
    if check_user() and check_role() == "admin" or check_role() == "operations":
        if request.method == 'POST':
            scheduled_date = request.form['scheduled_date']
            scheduled_time = request.form['scheduled_time']
            services = str(request.form.getlist('services[]'))

            sql = "insert into vehicle_service(reg_no, scheduled_date, scheduled_time, services) values (%s, %s, %s, %s)"
            cursor = connection.cursor()
            # try:
            cursor.execute(sql, (reg_no, scheduled_date, scheduled_time, services))
            connection.commit()
            return jsonify({'success': 'Service scheduled'})
            # except:
            #     connection.rollback()
            #     return jsonify({'error2':'Not added'})

        else:
            session['reg_no'] = reg_no
            return render_template('admin/send_service.html')
    else:
        return redirect('/login')

# @app.route('/allvehicles')
# def allvehicles():
#     if check_user() and check_role() == "admin":
#         sql = "select * from vehicles order by reg_no asc"
#         cursor = connection.cursor()
#         cursor.execute(sql)
#         if cursor.rowcount == 0:
#             return render_template('views/allvehicles.html', message = "No vehicles")
#         else:
#             vehicles = cursor.fetchall()
#             return render_template('views/allvehicles.html', vehicles = vehicles, makes = getmakes(), types = gettypes(), models = modellist())
#
#     else:
#         return redirect('/login')

@app.route('/serviceslivesearch', methods = ['POST', 'GET'])
def serviceslivesearch():
    if check_user() and check_role() == "admin" or "operations" or "operations":
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        if request.method == 'POST':
            search_word = request.form['search_word']
            if search_word == '':
                sql = "select * from vehicle_service order by service_id desc"
                cursor.execute(sql)
                services = cursor.fetchall()
                count = cursor.rowcount
                print(services)
                return jsonify(
                    {
                        'htmlresponse': render_template(
                            'views/servicesresponse.html', services = services, count = count
                        )
                    }
                )
            else:
                sql = "select * from vehicle_service Where service_id LIKE '%{}%' or status LIKE '%{}%' or services LIKE '%{}%' order by service_id desc".format(
                    search_word, search_word, search_word
                )
                cursor.execute(sql)
                services = cursor.fetchall()
                count = cursor.rowcount
                print(services)
                return jsonify(
                    {
                        'htmlresponse': render_template(
                            'views/servicesresponse.html', services=services, count=count
                        )
                    }
                )
        else:
            return render_template('views/servicesui.html')

    else:
        return redirect('/login')

@app.route('/servicescomplete/<service_id>', methods = ['POST', 'GET'])
def servicescomplete(service_id):
    if check_user() and check_role() == "mechanics":
        if request.method == 'POST':
            reg_no = request.form['reg_no']
            services = str(request.form.getlist('name[]'))
            sql = "insert into processed(service_id, reg_no, services)values(%s, %s, %s)"
            cursor = connection.cursor()
            # try:
            cursor.execute(sql, (service_id, reg_no, services))
            connection.commit()
            sqlupdate = "update vehicle_service set status = %s where service_id = %s"
            cursor = connection.cursor()
            cursor.execute(sqlupdate, ("Completed", service_id))
            connection.commit()
            return jsonify({'success':'Process complete!'})
            # except:
            #     return jsonify({'error':'Process not complete!'})
        else:
            sql = "select * from vehicle_service where service_id = %s"
            cursor = connection.cursor()
            cursor.execute(sql, service_id)
            row = cursor.fetchone()
            return render_template('admin/servicescomplete.html', row = row)

    else:
        redirect('/login')

@app.route('/processed_services', methods = ['POST', 'GET'])
def processed_services():
    if check_user() and check_role() == "admin" or "operations":
        if request.method == 'POST':
            reg_no = request.form['reg_no']
            sql = "select * from processed where reg_no = %s"
            cursor = connection.cursor()
            cursor.execute(sql, reg_no)
            if cursor.rowcount == 0:
                return render_template('views/process.html', message = 'Not found')
            else:
                rows = cursor.fetchall()
                return render_template('views/process.html', rows = rows)
        else:
            sql = "select * from processed order by reg_date desc"
            cursor = connection.cursor()
            cursor.execute(sql)
            if cursor.rowcount == 0:
                return render_template('views/process.html', message='Not found')
            else:
                rows = cursor.fetchall()
                return render_template('views/process.html', rows=rows)
    else:
        redirect('/login')


def getloc():
    sql = 'select * from locations order by loc_name asc'
    cursor = connection.cursor()
    cursor.execute(sql)
    locations = cursor.fetchall()
    return locations

def getcapacity():
    sql = 'select * from capacity order by capacity_code asc'
    cursor = connection.cursor()
    cursor.execute(sql)
    capacitys = cursor.fetchall()
    print(capacitys)
    return capacitys

def getmakes():
    sql = "select * from vehicle_make order by make_name asc"
    cursor = connection.cursor()
    cursor.execute(sql)
    makes = cursor.fetchall()
    return makes

def gettypes():
    sql = "select * from vehicle_type order by type_name asc"
    cursor = connection.cursor()
    cursor.execute(sql)
    types = cursor.fetchall()
    return types

def modellist():
    sql = "select * from vehicle_model order by model_name asc"
    cursor = connection.cursor()
    cursor.execute(sql)
    models = cursor.fetchall()
    return models

@app.route('/getmodels', methods = ['POST', 'GET'])
def getmodels():
    make_id = request.form['make_id']
    sql = "select * from vehicle_model where make_id =%s order by model_name asc"
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql, (make_id))
    models = cursor.fetchall()
    if cursor.rowcount == 0:
        return jsonify({"error":"No models"})
    else:
        return jsonify(models)

def getcapacity():
    sql = "select * from capacity order by capacity_code asc"
    cursor = connection.cursor()
    cursor.execute(sql)
    capacity = cursor.fetchall()
    return capacity

def getowner():
    sql = "select * from owners order by surname desc"
    cursor = connection.cursor()
    cursor.execute(sql)
    owner = cursor.fetchall()
    return owner

@app.template_filter()
def stringtolist(string):
    import ast
    print(type(string))
    y = ast.literal_eval(string)
    print(y)
    return y

# def getowner_id():
#     sql = "select * from owners order by owner_id desc"
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     owner_id = cursor.fetchone()
#     return owner_id

@app.route('/areagen')
def areagen():
    sql = "select * from vehicles"
    cursor = connection.cursor()
    cursor.execute(sql)
    yom = []
    status = []
    rows = cursor.fetchall()
    for row in rows:
        yom.append(row[9])
        status.append(row[14])

    return jsonify({'yom': yom, 'status': status})

app.run(debug = True)
