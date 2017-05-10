from flask import render_template, flash, redirect, request, Response
from flask import Flask, session, url_for, escape, jsonify
from app import app
import json, requests
from . import function

import os
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# app.secret_key = os.urandom(24)

# index view function suppressed for brevity
@app.route('/')
@app.route('/index')
def index():

	if 'email' in session:
		if request.method == 'POST':
			return render_template("search_results.html",
							title='Welcome',
							session=session['email']
							)
		return render_template("search.html",
						title='Welcome',
						session=session['email']
						)

	if request.method == 'POST':
		return render_template("search_results.html",
						title='Welcome',
						session=session['email']
						)

	return render_template("search.html",
                        title='Welcome',
						session=None)


@app.route('/s', methods=['GET', 'POST'])
def results():

		checkin = request.args['checkin']
		checkout = request.args['checkout']

		S = request.args['adults']
		M = request.args['children']
		L = request.args['infants']
		guests = int(S) + int(M) + int(L)
		adults = int(S)
		children = int(M)
		infants = int(L)
		print("number of guests = ", guests)
		print("number of adults = ", adults)
		print("number of children = ", children)
		print("checkin  = ", checkin)
		print("checkout = ", checkout)
		print("=====================================================\n", request.query_string, "=====================================================\n")

		Info = function.Search_bytotal(guests, adults, children, infants, checkin, checkout)
		Info2 = function.Search_bytotal(guests, adults, children, infants, checkin, checkout)

		print("Info: ", Info)
		print("Info: ", Info2)

		if 'email' in session:

			return render_template("search_results.html",
		                        title='results',
								session=session['email'],
		                        info = Info)

		return render_template("search_results.html",
	   						title='results',
							session=None,
	                        info = Info)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if 'email' in session:
		return redirect('/')
	else:
	    error=None
	    if request.method == 'POST':
	        Email= request.form.get("email")
	        PW = request.form.get("password")
	        result1 = function.Check_email(Email)
	        result2 = function.Check_pw(Email, PW)
	        if result1 ==[]:
	            error = 'Invalid username'
	        elif result2 ==[]:
	            error = 'Invalid password'
	        else:
	            session['email'] = Email
	            return redirect('/')

	    return render_template("login.html",
	                        title='Sign In',
	                        error=error)

@app.route('/signup', methods=['POST', 'GET'])
def signup():

	if request.method == 'POST':
		Email= request.form.get("user[email]")
		PW = request.form.get("user[password]")
		result = function.Save_mem(Email, PW)
		if result == 1:
			session['email'] = Email
			return redirect('/')
		else:
			error = 'Email already exists.'
			return render_template("signup.html",
								title='SignUp',
								error=error)
	else:
		return render_template("signup.html",
							title='SignUp',
							error=None)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('email', None)
    return redirect('/')


@app.route('/enrollment_home/address', methods=['GET', 'POST'])
def enrollment_home_address():
	# Check session
    if not 'email' in session:
        return redirect('/')
    User = session['email']
    citycode = function.Check_citycode(User)





    if request.method == 'POST':
        print(request.form)
        state = request.form.get("state")
        city = request.form.get("city")
        street = request.form.get("street")
        apt = request.form.get("apt")
        zipcode = request.form.get("zipcode")
        function.Save_home_address(User, state, city, street, apt, zipcode)
        citycode = zipcode[0:3]
        function.Update_Citycode(User, citycode)
        return redirect('/enrollment_home/room')


    return render_template("address.html",
                        title='progress',
						session='OK',
						city='')


@app.route('/enrollment_home/room', methods=['GET', 'POST'])
def enrollment_home_room():
	# Check session
	if not 'email' in session:
		return redirect('/')


	if request.method == 'POST':
		User = session['email']
		print(request.form)


		house_type = request.form.get("house_type")
		if house_type == '1':
			house_type = 'A'
		elif house_type == '2':
			house_type = 'P'
		room = request.form.get("number_of_room")
		function.Save_home_room(User, house_type, room)
		return redirect('/enrollment_home/car_elevator')

	return render_template("room.html",
                        title='progress',
						session='OK')

@app.route('/enrollment_home/car_elevator', methods=['GET', 'POST'])
def enrollment_home_car_elevator():
	# Check session
	if not 'email' in session:
		return redirect('/')


	if request.method == 'POST':
		User = session['email']
		print(request.form)

		print(User)
		elevator = house_type = request.form.get("elevatorType")
		parking = house_type = request.form.get("parkingType")
		function.Save_home_car_elevator(User, elevator, parking)
		return redirect('/rooms')


	return render_template("car_elevator.html",
                        title='progress',
						session='OK')

@app.route('/enrollment_home/complete', methods=['GET', 'POST'])
def enrollment_home_complete():
	# Check session
	if not 'email' in session:
		return redirect('/')


	if request.method == 'POST':
		print(request.form)
		return redirect('/')

	return render_template("enrollment_home_complete.html",
                        title='progress',
						session='OK')

@app.route('/enrollment_pet/pet', methods=['GET', 'POST'])
def enrollment_pet_pet():
    # Check session
	if not 'email' in session:
		return redirect('/')



	if request.method == 'POST':
		print(request.form)



		User = session['email']

		petname = request.form.get("petName")
		petgender = request.form.get("petGender")
		month = request.form.get("pet[birthday_month]")
		day = request.form.get("pet[birthday_day]")
		year = request.form.get("pet[birthday_year]")

		petbirth = year+"-"+month+"-"+day
		function.Save_pet_pet(User, petname, petgender,petbirth)

		return redirect('/enrollment_pet/size')

	return render_template("pet.html",
                        title='pet',
						session='OK')

@app.route('/enrollment_pet/size', methods=['GET', 'POST'])
def enrollment_pet_size():

	if not 'email' in session:
		return redirect('/')



	if request.method == 'POST':
		print(request.form)


		User = session['email']

		breed = request.form.get("breed")
		size = request.form.get("size")
		function.Save_pet_size(User, breed, size)

		return redirect('/enrollment_pet/vac')

	return render_template("pet_size.html",
                        title='pet',
						session='OK')

@app.route('/enrollment_pet/vac', methods=['GET', 'POST'])
def enrollment_pet_vac():

	if not 'email' in session:
		return redirect('/')

	if request.method == 'POST':
		print(request.form)

		User = session['email']
		ns = request.form.get("ns")
		vac = request.form.get("vac")
		function.Save_pet_vac(User, ns, vac)
		function.Increase_npet(User)

		return redirect('/pets')

	return render_template("pet_vac.html",
                        title='pet',
						session='OK')

@app.route('/enrollment_pet/complete', methods=['GET', 'POST'])
def enrollment_pet_complete():
	# Check session
	if not 'email' in session:
		return redirect('/')


	if request.method == 'POST':
		print(request.form)
		return redirect('/')

	return render_template("enrollment_pet_complete.html",
                        title='progress',
						session='OK')

@app.route('/rooms', methods=['GET', 'POST'])
def rooms():

	if not 'email' in session:
		return redirect('/')

	if request.method == 'POST':
		print(request.form)

	User = session['email']
	check_room = function.Check_citycode(User)
	if(check_room):
		room = function.Read_house(User)
	else:
		room = ''

	return render_template("user_rooms.html",
                        title='MyProfile/rooms',
						session='OK', rooms = room)

@app.route('/pets', methods=['GET', 'POST'])
def pets():

	if not 'email' in session:
		return redirect('/')

	if request.method == 'POST':
		print(request.form)

	User = session['email']
	check_pet = function.Check_npet(User)
	if check_pet[0][0]=='1':
		pet = function.Read_pet(User)
	else:
		pet = ''

	return render_template("user_pets.html",
                        title='MyProfile/pets',
						session='OK', pets=pet)

@app.route('/users/edit', methods=['GET', 'POST'])
def users_edit():

	if not 'email' in session:
		return redirect('/')

	if request.method == 'POST':
		print(request.form)


	return render_template("user_edit.html",
                        title='MyProfile/edit',
						session='OK')


@app.route('/test', methods=['GET', 'POST'])
def test():


	if 'email' in session:

		return render_template("test_search.html",
                        title='Welcome',
						session=session['email']
						)

	if request.method == 'POST':
		print(request.form)


	return render_template("test_search.html",
                        title='Search',
						session='OK',
						info = info)
@app.route('/test2', methods=['GET', 'POST'])
def test2():


	if 'email' in session:

		return render_template("test_search2.html",
                        title='Welcome',
						session=session['email']
						)

	if request.method == 'POST':
		print(request.form)

	return render_template("test_search2.html",
                        title='Search',
						session='OK')

def remove_DBfiles():
    filenames = ['house.db', 'member.db', 'pet.db', 'petsitting.db']

    #print(Path().parent)

    for filename in filenames:
        try:

            path = os.getcwd() + "/" + filename
            print(path)
            os.remove(path)
        except OSError:
            pass

def loop_insert():
    for i in range(1, 101):
        user = str(i) + "@gmail.com"
        passwd = '1234'
        function.Save_mem(user, passwd)

        function.Save_home_address(user, str(i), 'city', 'street', 'apt', 'zipcode' )
        function.Update_Citycode(user, 'citycode')
        function.Save_home_room(user, 'house_type', 'room')
        function.Save_home_car_elevator(user, 'elevator', 'parking')


        function.Save_pet_pet(user, str(i), 'petgender', 'petbirth')
        function.Save_pet_size(user, 'bread', 'size')
        function.Save_pet_vac(user, 'ns', 'vac')
        function.Increase_npet(user)

        function.Save_petsitter1(user, i, '04/22/2017' , '05/13/2017' , '05/14/2017')
        function.Save_petsitter2(user, 10 , 6 , 6 , 6)
