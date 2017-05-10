#-*- coding: utf-8 -*-
import sqlite3

#petsitting.db 만드는 함수
#Email, PW, PN, CC, AP
# PN: 펫 수 (1, 0) , 0으로 초기화
# CC: 집등록할경우 해당 집의 city code, 0으로 초기화
# AP: 펫시팅 가능 여부 (1, 0) , 0으로 초기화

def Make_db_member():
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS member(Email text NOT NULL UNIQUE, PW text NOT NULL,PN text DEFAULT 0, CC text DEFAULT 0, AP text DEFAULT 0, Time DATE DEFAULT (datetime('now','localtime')))")
    con.commit()
    con.close()

#pet.db 만드는 함수
#Host, P_key, Name, Birth, Gender, Kind, Size,  NS, Vac
#HosT: member table 의 Email
#P_key: 이메일#Pet
def Make_db_pet():
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS pet(Host text NOT NULL,P_key text, Name text, Birth text, Gender text, Kind text, Size text, NS text, Vac text,  Time DATE DEFAULT (datetime('now','localtime')), PRIMARY KEY(Host), CONSTRAINT fk_Pet FOREIGN KEY (Host) REFERENCES member(Email))")
    con.commit()
    con.close()

#house.db 만드는 함수
#Host, H_key, State, City, Street, Apt, Address,citycode, Type, Room, Area, Elevator, Parking
#Host, H_key, Address, Type, Room, Area, Elevator, Parking
#Type :  집타입 아파트 : A, 빌라 : V, 개인주택 : P, 다세대 주택 : M
#Host -> member table 의 Email
def Make_db_house():
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS house(Host text NOT NULL, H_key text NOT NULL, State text NOT NULL, City text NOT NULL, Street text NOT NULL, Apt text NOT NULL, Address text NOT NULL, Citycode text DEFAULT 0 ,Type text DEFAULT 0, Room text DEFAULT 0, Elevator text, Parking text,  Time DATE DEFAULT (datetime('now','localtime')), PRIMARY KEY(Host), CONSTRAINT fk_house FOREIGN KEY (Host) REFERENCES member(Email))")
    con.commit()
    con.close()

 #petsitter.db 만드는 함수
 #Host , Cost , Start_Date , End_Date , Except_Date , Total , Large , Midium , Small
def Make_db_petsitter():
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS petsitter(Host text NOT NULL, Cost int, Start_Date text, End_Date text, Except_Date text, Total int, Large int, Midium int, Small int, Time DATE DEFAULT (datetime('now','localtime')), PRIMARY KEY(Host), CONSTRAINT fk_petsitter FOREIGN KEY (Host) REFERENCES member(Email))")
    con.commit()
    con.close()

# image table 생성
# Host, Asset, Path
#Path는 이미지의 절대경로이다.
def Make_db_image():
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS image(Host text NOT NULL,Asset text, Path text, Time DATE DEFAULT (datetime('now','localtime')), CONSTRAINT fk_house FOREIGN KEY (Host) REFERENCES member(Email))")
    con.commit()
    con.close()

# C_key, PSID, CSID, TS, TE, TC, TA, TH
#거래키, 판매자아이디, 소비자아이디, 거래시작시간, 거래 종료시간, 결제완료시간, 결제 금액, 기타사항
def Make_db_tran():
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tran(C_key text NOT NULL, PSID text NOT NULL, CSID text NOT NULL, TS text NOT NULL, TE text NOT NULL, TC DATE DEFAULT (datetime('now','localtime')), TA text NOT NULL, TH text NOT NULL)")
    con.commit()
    con.close()

def Search_tran(E):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM tran WHERE PSID =? OR CSID =? ", (E,E ))
    data = cursor.fetchall()
    con.commit()
    con.close()
    return data

def Save_tran(C_key, PSID, CSID, TS, TE, TA, TH):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO tran(C_key, PSID, CSID, TS, TE, TA, TH) VALUES (?,?,?,?,?,?,?)", (C_key, PSID, CSID, TS, TE, TA, TH))
    con.commit()
    con.close()


def Check_email(E):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("SELECT Email FROM member WHERE Email=? ",(E, ))
    data = cursor.fetchall()
    con.commit()
    con.close()
    return data

def Check_pw(E, P):
    con = sqlite3.connect("pesitting.db")
    cursor = con.cursor()
    cursor.execute("SELECT Email FROM member WHERE Email=? AND PW = ?",(E, P))
    data = cursor.fetchall()
    con.commit()
    con.close()
    return data

def Check_citycode(E):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("SELECT CC FROM member WHERE Email=?",(E, ))
    data = cursor.fetchall()
    con.commit()
    con.close()
    return data

def Check_npet(E):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("SELECT PN FROM member WHERE Email=?",(E, ))
    data = cursor.fetchall()
    con.commit()
    con.close()
    return data

#petsitter.db에 펫시터 정보 삽입하는 함수
def Save_petsitter1(Host, Cost, Start_Date , End_Date , Except_Date):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    try:
         cursor.execute("INSERT INTO petsitter (Host, Cost, Start_Date , End_Date , Except_Date ) VALUES (?, ?, ?, ?, ?)", (Host, Cost, Start_Date , End_Date , Except_Date))
    except:
        return 0
    con.commit()
    con.close()
    return 1
# cursor.execute("UPDATE house set Type = ?, Room = ? WHERE Host = ?", (H_Type, H_Room, E))
#petsitter.db에 펫시터 정보 삽입하는 함수
def Save_petsitter2(Host,Total , Large , Midium , Small):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE petsitter set Total =?, Large = ?, Midium =?, Small=? WHERE Host =?", (Total , Large , Midium , Small, Host))
    con.commit()
    con.close()

# cursor.execute("UPDATE house SET State = ? WHERE Host = ? AND State <> ? ", (H_State,E, H_State))
def Modify_petsitter1(Host, Cost, Start_Date , End_Date , Except_Date):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE petsitter  SET Cost =? WHERE Host =? AND Cost <> ?", (Cost, Host, Cost))
    cursor.execute("UPDATE petsitter  SET Start_Date =? WHERE Host =? AND Start_Date <> ?", (Start_Date, Host, Start_Date))
    cursor.execute("UPDATE petsitter  SET  End_Date =? WHERE Host =? AND  End_Date <> ?", (End_Date, Host,  End_Date))
    cursor.execute("UPDATE petsitter  SET  Except_Date =? WHERE Host =? AND  Except_Date <> ?", ( Except_Date, Host,  Except_Date))
    con.commit()
    con.close()

def Modify_petsitter2(Host,Total , Large , Midium , Small):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE petsitter  SET Total =? WHERE Host =? AND Total <> ?", (Total, Host, Total))
    cursor.execute("UPDATE petsitter  SET Large =? WHERE Host =? AND Large <> ?", (Large, Host, Large))
    cursor.execute("UPDATE petsitter  SET Midium =? WHERE Host =? AND Midium <> ?", (Midium, Host, Midium))
    cursor.execute("UPDATE petsitter  SET Small =? WHERE Host =? AND Small <> ?", (Small, Host, Small))
    con.commit()
    con.close()

#Email : E, Password: P로 회원가입 할 경우 디비에 이를 저장
def Save_mem(E, P):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    try:
        cursor.execute("INSERT INTO member (Email, PW) VALUES (?,?)", (E,P))
    except:
        return 0 # 이미 있는 이메일인 경우 -중복가입 방지
    con.commit()
    con.close()
    return 1

#db에서 Citycode 수정하는 함수
def Update_Citycode(E, city):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE member SET CC = ? WHERE Email = ? ", (city,E))
    con.commit()
    con.close()

#pet 등록할 경우 db에서 해당 고객 N_pet 증가시켜주는 함수
def Increase_npet(E):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE  member SET PN = 1 WHERE Email = ? ", (E,))
    con.commit()
    con.close()

#house 등록할 경우 db에 집 정보 저장하는 함수
#Host, H_key, State, City, Street, Apt, Address, Zipcode
def Save_home_address(E, H_State, H_City, H_Street, H_Apt,H_Zipcode):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    key = E + "#Home"
    H_Address = H_State + " "+ H_City + " " + H_Street + " " + H_Apt
    cursor.execute("INSERT INTO house(Host, H_key, State, City, Street, Apt, Address,  Citycode) VALUES (?, ?, ?, ?, ?,?,?,?)", (E,key, H_State, H_City, H_Street, H_Apt, H_Address, H_Zipcode))
    con.commit()
    con.close()

#house 등록할 경우 db에 집 정보 저장하는 함수
#Type, Room
def Save_home_room(E, H_Type, H_Room):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE house set Type = ?, Room = ? WHERE Host = ?", (H_Type, H_Room, E))
    con.commit()
    con.close()
#house 등록할 경우 db에 집 정보 저장하는 함수
#Elevator, Parking
def Save_home_car_elevator(E, H_Elevator, H_Parking):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE house set Elevator = ?, Parking= ? WHERE Host = ?", (H_Elevator, H_Parking, E))
    con.commit()
    con.close()

def Modify_home_address(E, H_State, H_City, H_Street, H_Apt,H_Zipcode):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    H_Address = H_State + " "+ H_City + " " + H_Street + " " + H_Apt
    cursor.execute("UPDATE house SET State = ? WHERE Host = ? AND State <> ? ", (H_State,E, H_State))
    cursor.execute("UPDATE house SET City = ? WHERE Host = ? AND City <> ? ", (H_City,E, H_City))
    cursor.execute("UPDATE house SET Street = ? WHERE Host = ? AND Street <> ? ", (H_Street,E,H_Street))
    cursor.execute("UPDATE house SET Apt = ? WHERE Host = ? AND Apt <> ? ", (H_Apt,E, H_Apt))
    cursor.execute("UPDATE house SET Address = ? WHERE Host = ? AND Address <> ? ", (H_Address,E, H_Address))
    cursor.execute("UPDATE house SET Citycode = ? WHERE Host = ? AND Citycode <> ? ", (H_Zipcode,E, H_Zipcode))
    con.commit()
    con.close()

def Modify_home_room(E, H_Type, H_Room):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE house SET Type = ? WHERE Host = ? AND Type <> ? ", (H_Type,E, H_Type))
    cursor.execute("UPDATE house SET Room = ? WHERE Host = ? AND Room <> ? ", (H_Room,E, H_Room))
    con.commit()
    con.close()

def Modify_home_car_elevator(E, H_Elevator, H_Parking):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE house SET Elevator = ? WHERE Host = ? AND Elevator <> ? ", (H_Elevator,E, H_Elevator))
    cursor.execute("UPDATE house SET Parking = ? WHERE Host = ? AND Parking <> ? ", (H_Parking,E, H_Parking))
    con.commit()
    con.close()
#pet 등록할 경우 db에 펫 정보 저장하는 함수
#Host, P_key, Name, Birth, Gender, Kind, size, NS, Vac
#P_size : S= 소형견, M= 중형견, L=대형경
#NS, Vac : Y, N
def Save_pet_pet(E, P_Name, P_Gender, P_Birth):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    key = E + "#Pet"
    cursor.execute("INSERT INTO pet (Host, P_key, Name, Birth, Gender) VALUES (?,?,?,?,?)", (E, key, P_Name, P_Birth, P_Gender))
    con.commit()
    con.close()

def Save_pet_size(E, P_Kind,P_size):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE pet set Kind = ?, Size= ? WHERE Host = ?", (P_Kind,P_size, E))
    con.commit()
    con.close()

def Save_pet_vac(E, P_NS, P_Vac):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE pet set NS = ?, Vac= ? WHERE Host = ?", (P_NS, P_Vac, E))
    con.commit()
    con.close()

def Modify_pet_pet(E, P_Name, P_Gender, P_Birth):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE pet SET Name = ? WHERE Host = ? AND Name <> ? ", (P_Name,E, P_Name))
    cursor.execute("UPDATE pet SET Gender = ? WHERE Host = ? AND Gender <> ? ", (P_Gender,E, P_Gender))
    cursor.execute("UPDATE pet SET Birth = ? WHERE Host = ? AND Birth <> ? ", (P_Birth,E, P_Birth))
    con.commit()
    con.close()

def Modify_pet_size(E, P_Kind,P_Size):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE pet SET Kind = ? WHERE Host = ? AND Kind <> ? ", (P_Kind,E, P_Kind))
    cursor.execute("UPDATE pet SET Size = ? WHERE Host = ? AND Size <> ? ", (P_Size,E, P_Size))
    con.commit()
    con.close()

def Modify_pet_vac(E, P_NS, P_Vac):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE pet SET NS = ? WHERE Host = ? AND NS <> ? ", (P_NS,E, P_NS))
    cursor.execute("UPDATE pet SET Vac = ? WHERE Host = ? AND Vac <> ? ", (P_Vac,E, P_Vac))
    con.commit()
    con.close()

#Host, H_key, Address, Type, Room, Area, Elevator, Parking
def Save_House(E,H_Address, H_Type, H_Room, H_Area, H_Elevator, H_Parking):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    key = E + "#Home"
    cursor.execute("INSERT INTO house(Host, H_key, Address, Type, Room, Area, Elevator, Parking) VALUES (?,?,?,?,?,?,?,?)", (E,key,H_Address, H_Type, H_Room, H_Area, H_Elevator, H_Parking))
    con.commit()
    con.close()

#petsitter로 등록할 경우 해당고객의 F_Petsitter를 1로 업데이트
def Update_AP(E):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE member SET AP = 1 WHERE Email = ? ", (E,))
    con.commit()
    con.close()

def Modify_image(Host, Asset, Path):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("UPDATE image  SET Path =? WHERE Host =? AND Asset =? And Path <> ?", (Path, Host, Asset, Path))
    con.commit()
    con.close()

def Save_image(Host, Asset, Path):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO image (Host, Asset, Path) VALUES (?, ?, ?)", (Host, Asset, Path))
    con.commit()
    con.close()

def Read_member(E):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM member WHERE Email = ?", (E, ))
    data = cursor.fetchall()
    con.commit()
    con.close()
    return data

def Read_pet(E):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM pet WHERE Host = ?", (E, ))
    data = cursor.fetchall()
    con.commit()
    con.close()
    return data

def Read_house(E):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM house WHERE Host = ?", (E, ))
    data = cursor.fetchall()
    con.commit()
    con.close()
    return data

def Get_image(E, Asset):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("SELECT Path FROM image WHERE Host = ? AND Asset = ? ", (E, Asset))
    data = cursor.fetchall()
    con.commit()
    con.close()
    if data =="":
        return 0
    return data

def Delete_member(E):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM member WHERE Email=?", (E, ))
    con.commit()
    con.close()

def Delete_pet(E):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM pet WHERE Host=?", (E, ))
    con.commit()
    con.close()

def Delete_house(E):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM house WHERE Host=?", (E, ))
    con.commit()
    con.close()

def Delete_petsitter(E):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM petsitter WHERE Host=?", (E, ))
    con.commit()
    con.close()

def Delete_image(Host, Asset):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM image WHERE Host=? AND Asset =?", (Host, Asset, ))
    con.commit()
    con.close()

#총마리수로 검색하는 경우
#result : Host, cost, total, address, type
def Search_bytotal(T, L, M, S, S_date, E_date):
    con = sqlite3.connect("petsitting.db")
    cursor = con.cursor()
    cursor.execute("SELECT Host, Cost, Total FROM petsitter WHERE Total >= ? AND Large >= ? AND Midium >= ? AND Small >=? AND Start_Date <=? AND End_Date >= ? AND Except_Date NOT BETWEEN Start_Date AND End_Date", (T, L, M, S, S_date, E_date))
    data = cursor.fetchall()
    cursor.execute("SELECT COUNT(Host) FROM petsitter WHERE Total >= ? AND Large >= ? AND Midium >= ? AND Small >=? AND Start_Date <=? AND End_Date >= ? AND Except_Date NOT BETWEEN Start_Date AND End_Date", (T, L, M, S, S_date, E_date))
    cnt = cursor.fetchone()
    if data ==[]:
        return 0
    cursor2 = con.cursor()
    i=0
    result2 = []
    while i<cnt[0]:
        a = data[i][0]
        cursor2.execute("SELECT Address, Type, Room FROM house WHERE Host = ?", (a, ))
        data2 = cursor2.fetchall()
        if data2 ==[]:
            return 0
        result = data[i] + data2[0]
        result2 .append(result)
        i=i+1
    con.commit()
    con.close()
    return result2
