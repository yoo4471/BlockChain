#user email largecost mediumcost smallcost homename region housetype room totalpet
def Make_db_petsitter_info():
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS petsitter_info(user text, email text, largecost text, mediumcost text, smallcost text, homename text, region text, housetype text, room text, totalpet text)")
    con.close()

def Save_petsitter_info(user, email, largecost, mediumcost, smallcost, homename, region, housetype, room, totalpet):
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO petsitter_info(user, email, largecost, mediumcost, smallcost, homename, region, housetype, room, totalpet) VALUES (?,?,?,?,?,?,?,?,?,?)", (user, email, largecost, mediumcost, smallcost, homename, region, housetype, room, totalpet))
    con.commit()
    con.close()

def Read_petsitter_info(E):
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM petsitter_info WHERE user=?", (E, ))
    data = cursor.fetchall()
    con.commit()
    con.close()
    return data

def delete_petsitter_info(E):
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM petsitter_info  WHERE user=?", (E, ))
    con.commit()
    con.close()

#email , guests , adults , children , infants, checkin, checkout
def Make_db_user_search():
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user_search(email text, guests int, adults int, children int, infants int, checkin text, checkout text)")
    con.close()

def Save_user_search(email , guests , adults , children , infants, checkin, checkout):
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO user_search(email , guests , adults , children , infants, checkin, checkout) VALUES (?,?,?,?,?,?,?)", (email , guests , adults , children , infants, checkin, checkout))
    con.commit()
    con.close()

def Read_user_search(E):
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM user_search  WHERE email=? ", (E, ))
    data = cursor.fetchall()
    con.commit()
    con.close()
    return data

def delete_user_search(E):
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM user_search WHERE email = ?", (E, ))
    con.commit()
    con.close()

#count
def Make_db_petsitter_num():
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS petsitter_num(count int, email text)")
    con.close()

def Save_petsitter_num(count, E):
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO petsitter_num(count, email) VALUES (?, ?)", (count,E))
    con.commit()
    con.close()

def Read_petsitter_num(E):
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM petsitter_num  WHERE email=?", (E, ))
    data = cursor.fetchall()
    con.commit()
    con.close()
    return data

def delete_petsitter_num(E):
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM petsitter_num  WHERE email=? ", (E, ))
    con.commit()
    con.close()

#total_charge
def Make_db_charge():
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS charge(total_charge int, email text)")
    con.close()
def Save_charge(total_charge, E):
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO charge(total_charge, email ) VALUES (?, ?)", (total_charge ,E))
    con.commit()
    con.close()
def Read_charge(E):
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM charge WHERE email=?", (E, ))
    data = cursor.fetchall()
    con.commit()
    con.close()
    return data
def delete_charge(E):
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM charge WHERE email=?", (E, ))
    con.commit()
    con.close()

def modify_charge(total_charge, E):
    con = sqlite3.connect("global.db")
    cursor = con.cursor()
    cursor.execute("UPDATE  charge SET total_charge=? WHERE email=?", (total_charge ,E))
    con.commit()
    con.close()
