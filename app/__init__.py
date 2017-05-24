from flask import Flask
from . import function
from . import new
app = Flask(__name__)
from app import views


try:

    function.Make_db_member()
    function.Make_db_house_new()
    function.Make_db_pet()
    function.Make_db_petsitter()
    function.Make_db_image()
    function.Make_db_tran()
    new.Make_db_petsitter_info()
    new.Make_db_user_search()
    new.Make_db_petsitter_num()
    new.Make_db_charge()
    # views.loop_insert()
except:
    print("db is already existed")
