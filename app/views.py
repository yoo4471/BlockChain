#-*- coding: utf-8 -*-
from flask import render_template, flash, redirect, request, Response
from flask import Flask, session, url_for, escape
from app import app
import json
from . import function
import os
import time
from werkzeug.contrib.cache import SimpleCache
from datetime import date

cache = SimpleCache()

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# app.secret_key = os.urandom(24)

# index view function suppressed for brevity
PETSITTERS = ''
USER_SEARCH = ''
count = 0
total_charge = 0

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

# none region
@app.route('/s', methods=['GET', 'POST'])
def results_none_region():

	checkin = request.args['checkin']
	checkout = request.args['checkout']

	S = request.args['adults'] #small
	M = request.args['children'] #medium
	L = request.args['infants'] #large
	guests = int(S) + int(M) + int(L)
	adults = int(S)
	children = int(M)
	infants = int(L)
	region = None

	print("region = ", region)
	print("number of small pet = ", guests)
	print("number of medium pet = ", adults)
	print("number of large pet = ", children)
	print("checkin  = ", checkin)
	print("checkout = ", checkout)
	print("====================================================="+request.query_string+"=====================================================")

	Info = function.Search_bytotal(region, guests, adults, children, infants, checkin, checkout)

	# save petsitter
	global PETSITTERS
	PETSITTERS = Info
	# save search
	global USER_SEARCH
	USER_SEARCH = guests, adults, children, infants, checkin, checkout

	pass_search = "all location", checkin, checkout, guests, adults, children, infants

	if Info == 0:
		total = 0
		page = 0
		print("Info : ", Info)
	else :
		total = 0
		for i in Info:
			total = total + 1
		page = total/8 + 1

	if 'email' in session:

		return render_template("search_results.html",
		                        title='results',
								session=session['email'],
		                        info = Info,
								total = total,
								page = page,
								print_search = pass_search)

	return render_template("search_results.html",
	   						title='results',
							session=None,
	                        info = Info,
							total = total,
							page = page,
							print_search = pass_search)

@app.route('/s/', defaults={'region': ''}, methods=['GET', 'POST'])
@app.route('/s/<region>', methods=['GET', 'POST'])
def results(region):

	checkin = request.args['checkin']
	checkout = request.args['checkout']

	S = request.args['adults'] #small
	M = request.args['children'] #medium
	L = request.args['infants'] #large
	guests = int(S) + int(M) + int(L)
	adults = int(S)
	children = int(M)
	infants = int(L)

	print(region)
	print("number of small pet = ", guests)
	print("number of medium pet = ", adults)
	print("number of large pet = ", children)
	print("checkin  = ", checkin)
	print("checkout = ", checkout)
	print("====================================================="+request.query_string+"=====================================================")

	Info = function.Search_bytotal(region, guests, adults, children, infants, checkin, checkout)

	# save petsitter
	global PETSITTERS
	PETSITTERS = Info
	# save search
	global USER_SEARCH
	USER_SEARCH = guests, adults, children, infants, checkin, checkout

	pass_search = region, checkin, checkout, guests, adults, children, infants

	print("===========with region=========")

	if Info == 0:
		total = 0
		page = 0
		print("Info : ", Info)
	else :
		total = 0
		for i in Info:
			total = total + 1
			page = total/8 + 1

	if 'email' in session:

		return render_template("search_results.html",
		                        title='results',
								session=session['email'],
		                        info = Info,
								total = total,
								page = page,
								print_search = pass_search)

	return render_template("search_results.html",
	   						title='results',
							session=None,
	                        info = Info,
							total = total,
							page = page,
							print_search = pass_search)

# def get_petsitter(petsitter_info):
#     rv = cache.get(petsitter_info[0])
#     if rv is None:
#         rv = calculate_value()
#         cache.set(PETSITTERS, rv, timeout=5 * 60)
#     return rv

@app.route('/booking/<int:num>', methods=['GET', 'POST'])
def booking(num):

	global PETSITTERS
	global count
	# print("===============petsitter : " , PETSITTERS[num-1] , "================")
	# print("num-1: ", PETSITTERS[num-1])
	count = num - 1

	if 'email' in session:
		return redirect(url_for('detail',petsitter = num-1))

	return redirect(url_for('detail',petsitter = num-1))

@app.route('/detail/<int:petsitter>', methods=['GET', 'POST'])
def detail(petsitter):

	global PETSITTERS
	global USER_SEARCH
	global total_charge
	# print("petsitter name : " , PETSITTERS[petsitter][0])

	# get petsitter's information
	detail_about_petsitter = function.Read_petsitter(PETSITTERS[petsitter][0])
	print("detail : ", detail_about_petsitter)
	print("petsitter: ", PETSITTERS[petsitter])

	cost_small = detail_about_petsitter[0][2] * USER_SEARCH[1]
	cost_medium = detail_about_petsitter[0][3] * USER_SEARCH[2]
	cost_large = detail_about_petsitter[0][4] * USER_SEARCH[3]
	add_all = cost_small + cost_medium + cost_large

	total = cost_small, cost_medium, cost_large, add_all

	total_charge = add_all

	if 'email' in session:
		return render_template("booking.html",
							title='booking',
							session=session['email'],
							detail_petsitter = detail_about_petsitter,
							results = PETSITTERS[petsitter],
							user = USER_SEARCH,
							total_cost = total
							)

	return render_template("booking.html",
						title='booking',
						session=None,
						detail_petsitter = detail_about_petsitter,
						results = PETSITTERS[petsitter],
						user = USER_SEARCH,
						total_cost = total
						)

@app.route('/payments/', methods=['GET', 'POST'])
def payments():

	global PETSITTERS
	global USER_SEARCH
	global count
	global total_charge

	print("count: ", count)

	if 'email' in session:
		# get petsitter's information
		detail_about_petsitter = function.Read_petsitter(PETSITTERS[count][0])

		checkin = USER_SEARCH[4]
		checkout = USER_SEARCH[5]

		checkin_year = int(checkin[6:10])
		checkin_month = int(checkin[0:2])
		checkin_day =int(checkin[3:5])

		checkout_year = int(checkout[6:10])
		checkout_month = int(checkout[0:2])
		checkout_day =int(checkout[3:5])

		d0 = date(checkin_year, checkin_month, checkin_day)
		d1 = date(checkout_year, checkout_month, checkout_day)
		term = d1 - d0
		# print(term.days)
		temp_charge = total_charge
		total = temp_charge * term.days
		total_charge = total

		return render_template("payments.html",
							title='payments',
							session=session['email'],
							detail_petsitter = detail_about_petsitter,
							results = PETSITTERS[count],
							user = USER_SEARCH,
							charge = temp_charge,
							term = term.days,
							total = total
							)

	else:

		return render_template("signup.html",
							title='SignUp',
							error=None
							)


#
# @app.route('/guest/<guest>')
# def hello_guest(guest):
#    return 'Hello %s as Guest' % guest
#
# @app.route('/user/<name>')
# def hello_user(name):
#    if name =='admin':
#       return redirect(url_for('hello_admin'))
#    else:
#       return redirect(url_for('hello_guest',guest = name))

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
	# ImmutableMultiDict([('user[last_name]', 'yoo'),
	# 					('user[password]', '1q2w3e4r'),
	# 					('user[birthday_month]', '1'),
	# 					('user[birthday_day]', '4'),
	# 					('user[birthday_year]', '2011'),
	# 					('utf8', '✓'),
	# 					('from', 'email_signup'),
	# 					('user[first_name]', 'dongwon'),
	# 					('user[email]', 'asldkfj@nave.rcom'),
	# 					('user_profile_info[receive_promotional_email]', '0'),
	# 					('user_profile_info[receive_promotional_email]', '1'),
	# 					('authenticity_token', '#j')])

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
		# ImmutableMultiDict([('country_code', 'US'),
		# 					('city', '1'),
		# 					('street', '1'),
		# 					('zipcode', '1'),
		# 					('apt', '1'),
		# 					('state', '1')])
        state = request.form.get("state")
        city = request.form.get("city")
        street = request.form.get("street")
        apt = request.form.get("apt")
        zipcode = request.form.get("zipcode")
        function.Save_home_address(User, state, city, street, apt, zipcode)
        citycode = zipcode[0:3]
        function.Update_Citycode(User, citycode)
        return redirect('/enrollment_home/room')

	# if citycode[0][0] != '0':
        # city =
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
		# ImmutableMultiDict([('house_type', '2'),
		# 					('number_of_room', '1')])

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
		# ImmutableMultiDict([('elevatorType', 'yes'),
		# 					('parkingType', 'no')])
		print(User)
		elevator = house_type = request.form.get("elevatorType")
		parking = house_type = request.form.get("parkingType")
		function.Save_home_car_elevator(User, elevator, parking)
		return redirect('/rooms')


	return render_template("car_elevator.html",
                        title='progress',
						session='OK')

@app.route('/start/', methods=['GET', 'POST'])
def start_petsitter():

	if not 'email' in session:
		return redirect('/')

	if request.method == 'POST':

		print("start_petsitter : " , request.form)
		Nickname = request.form.get("Nickname")
		Count_Total = request.form.get("Count_Total")
		Count_Large = request.form.get("Count_Large")
		Count_Medium = request.form.get("Count_Medium")
		Count_Small = request.form.get("Count_Small")
		Cost_Large = request.form.get("Cost_Large")
		Cost_Medium = request.form.get("Cost_Medium")
		Cost_Small = request.form.get("Cost_Small")
		Start_Date = request.form.get("Start_Date")
		End_Date = request.form.get("End_Date")
		Except_Date = request.form.get("Except_Date")
		Home_Name = request.form.get("Home_Name")
		Home_Intro = request.form.get("Home_Intro")

		User = session['email']

		function.Save_petsitter1(User, Nickname, Cost_Large, Cost_Medium, Cost_Small, Start_Date , End_Date , Except_Date)
		function.Save_petsitter2(User, Count_Total , Count_Large , Count_Medium , Count_Small, Home_Name ,Home_Intro)

		return redirect('/petsitter')


	return render_template("start_petsitter.html",
                        title='Search',
						session='OK')

@app.route('/enrollment_pet/pet', methods=['GET', 'POST'])
def enrollment_pet_pet():
    # Check session
	if not 'email' in session:
		return redirect('/')

	# User = session['email']
    # citycode = function.Check_citycode(User)
	# if citycode[0][0] != '0':
    #     return "already enroll home!"


	if request.method == 'POST':
		print(request.form)

		# ImmutableMultiDict([('petName', 'mong'),
		# 					('petGender', 'male'),
		# 					('pet[birthday_month]', '1'),
		# 					('pet[birthday_day]', '10'),
		# 					('pet[birthday_year]', '2016')])

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

		# ImmutableMultiDict([('pet-breed', '1'),
		# 					('pet-size', '3')])

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

		# ImmutableMultiDict([('ns', '1'),
		# 					('vac', '2')])
		User = session['email']
		ns = request.form.get("ns")
		vac = request.form.get("vac")
		function.Save_pet_vac(User, ns, vac)
		function.Increase_npet(User)

		return redirect('/pets')

	return render_template("pet_vac.html",
                        title='pet',
						session='OK')


@app.route('/modify_pet/pet', methods=['GET', 'POST'])
def modify_pet_pet():
    # Check session
   if not 'email' in session:
      return redirect('/')

   if request.method == 'POST':
      print(request.form)

      # ImmutableMultiDict([('petName', 'mong'),
      #                ('petGender', 'male'),
      #                ('pet[birthday_month]', '1'),
      #                ('pet[birthday_day]', '10'),
      #                ('pet[birthday_year]', '2016')])

      User = session['email']

      petname = request.form.get("petName")
      petgender = request.form.get("petGender")
      month = request.form.get("pet[birthday_month]")
      day = request.form.get("pet[birthday_day]")
      year = request.form.get("pet[birthday_year]")

      petbirth = year+"-"+month+"-"+day
      function.Modify_pet_pet(User, petname, petgender,petbirth)

      return redirect('/modify_pet/size')

   return render_template("modify_pet.html",
                        title='pet',
                  		session='OK')

@app.route('/modify_pet/size', methods=['GET', 'POST'])
def modify_pet_size():

   if not 'email' in session:
      return redirect('/')

   if request.method == 'POST':
      print(request.form)

      # ImmutableMultiDict([('pet-breed', '1'),
      #                ('pet-size', '3')])

      User = session['email']

      breed = request.form.get("breed")
      size = request.form.get("size")
      function.Modify_pet_size(User, breed, size)

      return redirect('/modify_pet/vac')

   return render_template("modify_pet_size.html",
                        title='pet',
                  		session='OK')

@app.route('/modify_pet/vac', methods=['GET', 'POST'])
def modify_pet_vac():

   if not 'email' in session:
      return redirect('/')

   if request.method == 'POST':
      print(request.form)

      # ImmutableMultiDict([('ns', '1'),
      #                ('vac', '2')])
      User = session['email']
      ns = request.form.get("ns")
      vac = request.form.get("vac")
      function.Modify_pet_vac(User, ns, vac)

      return redirect('/pets')

   return render_template("modify_pet_vac.html",
                        title='pet',
                  		session='OK')

@app.route('/modify_home/address', methods=['GET', 'POST'])
def modify_home_address():
   # Check session
    if not 'email' in session:
        return redirect('/')
    User = session['email']
    citycode = function.Check_citycode(User)

    # if citycode[0][0] != '0':
        # return "already enroll home!"

    if request.method == 'POST':
        print(request.form)
      # ImmutableMultiDict([('country_code', 'US'),
      #                ('city', '1'),
      #                ('street', '1'),
      #                ('zipcode', '1'),
      #                ('apt', '1'),
      #                ('state', '1')])
        state = request.form.get("state")
        city = request.form.get("city")
        street = request.form.get("street")
        apt = request.form.get("apt")
        zipcode = request.form.get("zipcode")
        function.Modify_home_address(User, state, city, street, apt, zipcode)
        citycode = zipcode[0:3]
        function.Update_Citycode(User, citycode)
        return redirect('/modify_home/room')

   # if citycode[0][0] != '0':
        # city =
    return render_template("modify_address.html",
                        title='progress',
                  session='OK',
                  city='')


@app.route('/modify_home/room', methods=['GET', 'POST'])
def modify_home_room():
   # Check session
   if not 'email' in session:
      return redirect('/')


   if request.method == 'POST':
      User = session['email']
      print(request.form)
      # ImmutableMultiDict([('house_type', '2'),
      #                ('number_of_room', '1')])

      house_type = request.form.get("house_type")
      if house_type == '1':
         house_type = 'A'
      elif house_type == '2':
         house_type = 'P'
      room = request.form.get("number_of_room")
      function.Modify_home_room(User, house_type, room)
      return redirect('/modify_home/car_elevator')

   return render_template("modify_room.html",
                        title='progress',
                  		session='OK')

@app.route('/modify_home/car_elevator', methods=['GET', 'POST'])
def modify_home_car_elevator():
   # Check session
   if not 'email' in session:
      return redirect('/')


   if request.method == 'POST':
      User = session['email']
      print(request.form)
      # ImmutableMultiDict([('elevatorType', 'yes'),
      #                ('parkingType', 'no')])
      print(User)
      elevator = house_type = request.form.get("elevatorType")
      parking = house_type = request.form.get("parkingType")
      function.Modify_home_car_elevator(User, elevator, parking)
      return redirect('/rooms')


   return render_template("modify_car_elevator.html",
                        title='progress',
                  		session='OK')


@app.route('/modify_start', methods=['GET', 'POST'])
def modify_start_petsitter():

   if not 'email' in session:
      return redirect('/')

   if request.method == 'POST':

      print("start_petsitter : " , request.form)
      Nickname = request.form.get("Nickname")
      Count_Total = request.form.get("Count_Total")
      Count_Large = request.form.get("Count_Large")
      Count_Medium = request.form.get("Count_Medium")
      Count_Small = request.form.get("Count_Small")
      Cost_Large = request.form.get("Cost_Large")
      Cost_Medium = request.form.get("Cost_Medium")
      Cost_Small = request.form.get("Cost_Small")
      Start_Date = request.form.get("Start_Date")
      End_Date = request.form.get("End_Date")
      Except_Date = request.form.get("Except_Date")
      Home_Name = request.form.get("Home_Name")
      Home_Intro = request.form.get("Home_Intro")

      User = session['email']

      function.Modify_petsitter1(User, Nickname, Cost_Large, Cost_Medium, Cost_Small, Start_Date , End_Date , Except_Date)
      function.Modify_petsitter2(User, Count_Total , Count_Large , Count_Medium , Count_Small, Home_Name ,Home_Intro)

      return redirect('/petsitter')


   return render_template("modify_start_petsitter.html",
                        title='Search',
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
		# if pet[0][6] == '1':
		# 	pet[0][6] == "Small"
		# elif pet[0][6] == '2':
		# 	pet[0][6] == "Medium"
		# else:
		# 	pet[0][6] == "Large"
	else:
		pet = ''

	return render_template("user_pets.html",
                        title='MyProfile/pets',
						session='OK', pets=pet)

@app.route('/petsitter', methods=['GET', 'POST'])
def pesitter():

	if not 'email' in session:
		return redirect('/')

	User = session['email']
	petsitter = function.Read_petsitter(User)

	return render_template("user_petsitter.html",
                        title='MyProfile/petsitter',
						session='OK',
						petsitter = petsitter)

@app.route('/user/payments/ing', methods=['GET','POST'])
def payments_list():
	if not 'email' in session:
		return redirect('/')

	if request.method == 'POST':
		# save payments result

		global PETSITTERS
		global USER_SEARCH
		global count
		global total_charge

		# print("petsitter: ", PETSITTERS[count])
		print("user: ", )

		User = session['email']

		# petsitter/ user/ checkin/ checkout/ tran_complete / charge / etc

		a = time.localtime()
		date = str(a.tm_year) +"_" +str(a.tm_mon)+ "_" +str(a.tm_mday) + " "+str(a.tm_hour)+":"+str(a.tm_min)+":"+str(a.tm_sec)

		petsitter_nickname = function.Read_petsitter(PETSITTERS[count][0])
		print("petsitter_nickname :",petsitter_nickname[0][1])

		function.Save_tran(PETSITTERS[count][0], petsitter_nickname[0][1], User, USER_SEARCH[4], USER_SEARCH[5], date, str(total_charge), '\0')

		# petsitter/ checkin/ checkout / charge
		result = function.Search_tran(User)
		# print("result: ", result)

		return render_template("user_payments_list.html",
	                        title='MyPayments/list',
							session='OK',
							result_list = result)

	User = session['email']
	get = function.Search_tran(User)

	tm = time.localtime()
	mon = format(tm.tm_mon,'02')
	day = format(tm.tm_mday, '02')
	today =  str(mon)+ "/" +str(tm.tm_mday) +"/" +str(tm.tm_year)

	temp = []
	check = 0
	print("get: ", get)
	for i in get:
		# print("i:" ,i)
		checkin = i[4]
		checkout = i[5]
		if today<=checkout:
			temp.append(i)
			check += 1
			if check == 3:
				break

	# {{result_list[0][4]}} ~ {{result_list[0][5]}}

	return render_template("user_payments_list.html",
                        title='MyPayments/list',
						session='OK',
						result_list = temp)

@app.route('/user/payments/complete', methods=['GET','POST'])
def complete_list():
	if not 'email' in session:
		return redirect('/')

	User = session['email']
	get = function.Search_tran(User)

	tm = time.localtime()
	mon = format(tm.tm_mon,'02')
	day = format(tm.tm_mday, '02')
	today =  str(mon)+ "/" +str(tm.tm_mday) +"/" +str(tm.tm_year)

	temp = []
	check = 0
	for i in get:
		checkin = i[4]
		checkout = i[5]
		if today>=checkout:
			temp.append(i)
			check += 1
			if check == 3:
				break

	return render_template("user_payments_complete.html",
                        title='MyPayments/list',
						session='OK',
						result_list = temp)

@app.route('/remove_petsitter', methods=['GET', 'POST'])
def remove_petsitter():

   if not 'email' in session:
      return redirect('/')

   User = session['email']
   function.Delete_petsitter(User)

   return render_template("remove_petsitter.html",
                        title='Search',
                  		session='OK')

@app.route('/remove_house', methods=['GET', 'POST'])
def remove_house():

   if not 'email' in session:
      return redirect('/')

   User = session['email']
   function.Delete_house(User)

   return render_template("remove_house.html",
                        title='Search',
                  		session='OK')

@app.route('/remove_pet', methods=['GET', 'POST'])
def remove_pet():

   if not 'email' in session:
      return redirect('/')

   User = session['email']
   function.Delete_pet(User)

   return render_template("remove_pet.html",
                        title='Search',
                  		session='OK')


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

		return render_template("test_petsitter.html",
                        title='Welcome',
						session=session['email']
						)

	if request.method == 'POST':
		print(request.form)

	# User = session['email']
	# info = function.Read_member(User)


	return render_template("test_petsitter.html",
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

	# User = session['email']
	# info = function.Read_member(User)
	# http://snacky.tistory.com/6

	return render_template("test_search2.html",
                        title='Search',
						session='OK')

	# if not 'email' in session:
	# 	return redirect('/')
	#
	# # if request.method == 'GET':
	# 	# print(request.form)
	# data = function.Read_member()
	# print(data)

	# return render_template("test_get_rooms.html",
    #                     title='progress',
	# 					session='OK',
	# 					rooms = data)

@app.route('/test_booking', methods=['GET', 'POST'])
def test_booking():
	if 'email' in session:
		return render_template("test_booking.html",
                        title='Welcome',
						session=session['email']
						)

	return render_template("test_booking.html",
                        title='Search',
						session='OK')


def remove_DBfiles():
    filenames = ['petsitting.db']

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

        function.Save_home_address(user, str(i+1), 'city', 'street', 'apt', 'zipcode' )
        function.Update_Citycode(user, 'citycode')
        function.Save_home_room(user, 'house_type', 'room')
        function.Save_home_car_elevator(user, 'elevator', 'parking')


        function.Save_pet_pet(user, str(i+1), 'petgender', 'petbirth')
        function.Save_pet_size(user, 'bread', 'size')
        function.Save_pet_vac(user, 'ns', 'vac')
        function.Increase_npet(user)

        function.Save_petsitter1(user, 'lovePet',i+1000, i+2000, i+3000, '04/22/2017' , '05/13/2017' , '05/14/2017')
        function.Save_petsitter2(user, 10 , 6 , 6 , 6, "dongakgo + food + toy" ,"intro")

# @app.route('/s/<name>/booking', methods=[GET,POST])
# def booking(petsitter):
# 	return render_template("test_search2.html",
#                         title='Search',
# 						session='OK')
