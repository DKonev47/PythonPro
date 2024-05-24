from flask import Flask, request

import sqlite3


def dict_factory(cursore, row):
    d = {}
    for idx, col in enumerate(cursore.description):
        d[col[0]] = row[idx]
    return d


def get_from_db(query, many=True):
    con = sqlite3.connect('db_DZ-2.db')
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute(query)
    if many:
        res = cur.fetchall()
    else:
        res = cur.fetchone()
    con.close()
    return res


def insert_to_db(query):
    con = sqlite3.connect('db_DZ-2.db')
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    con.close()


app = Flask(__name__)


@app.route("/")
def index():
    index_html = """<html>
    <a href=/user>user</a><br>
    <a href=/fitness_center>fitness_center</a><br>
    <a href=/register>get_register</a><br>
    <a href=/fitness_center/1/trainer>fitness_center/1/trainer</a><br>
    <a href=/fitness_center/1/trainer/1>fitness_center/1/trainer/1</a><br>
    <a href=/fitness_center/1/trainer/1/score>fitness_center/1/trainer/1/rating</a><br>
    </html>
    """
    return index_html


@app.post('/register')
def post_user_register():
    form_data = request.form
    insert_to_db(f"""insert into user (login, password, birth_date, phone) 
                    values (\'{form_data['login']}\', \'{form_data['password']}\',
                            \'{form_data['birth_date']}\', \'{form_data['phone']}\')""")
    user_name = {form_data['login']}
    return f'user \"{user_name}\" registered'


@app.get('/register')
def get_user_register():
    return f"""<form action='/register' method='post'>
         <label for="login">login:</label><br>
         <input type="text" id="login" name="login"><br>
         <label for="password">password:</label><br>
         <input type="password" id="password" name="password"><br>
         <label for="birth_date">birth_date:</label><br>
         <input type="date" id="birth_date" name="birth_date"><br>
         <label for="phone">phone:</label><br>
         <input type="text" id="phone" name="phone"><br><br>
         <input type="submit" value="Submit">
       </form>"""


@app.post('/login')
def post_user_login():
    return 'new user is logged in'


@app.get('/login')
def get_user_login():
    return 'please enter credentials'


@app.post('/user')
def post_user_info():
    return 'user data were modified'


@app.get('/user')
def get_user_info():
    res = get_from_db('select login, phone, birth_date from user', True)
    return str(res)


@app.put('/user')
def put_user():
    return 'user info was successfully updated'


@app.post('/funds')
def post_funds():
    return 'user account was successfully funded'


@app.get('/funds')
def get_funds():
    return 'user deposit value'


@app.get('/fitness_center')
def get_fitness_center():
    res = get_from_db('select * from fitness_center')
    return str(res)


@app.get('/fitness_center/<gym_id>/services/')
def get_services(gym_id):
    return f'fitness_center {gym_id} services list'

@app.get('/fitness_center/<gym_id>/services/<service_id>')
def get_service_info(gym_id, service_id):
    return f'fitness_center {gym_id} services {service_id} info'


@app.get('/fitness_center/<gym_id>/trainer/')
def get_trainers(gym_id):
    res = get_from_db(f'select * from trainer where fitness_center_id={gym_id}', True)
    return str(res)


@app.get('/fitness_center/<gym_id>/trainer/<coach_id>/')
def get_coach_info(gym_id, coach_id):
    res = get_from_db(f'select * from trainer where fitness_center_id={gym_id} and id={coach_id}', True)
    return str(res)


@app.get('/fitness_center/<gym_id>/trainer/<coach_id>/score')
def get_coach_score(gym_id, coach_id):
    res = get_from_db(f'SELECT * FROM trainer_rating WHERE trainer_id = {coach_id}', True)
    return str(res)


@app.post('/fitness_center/<gym_id>/trainer/<coach_id>/score')
def post_coach_score(gym_id, coach_id):
    return f'fitness_center {gym_id} trainer {coach_id} score was added'


@app.put('/fitness_center/<gym_id>/trainer/<coach_id>/score')
def put_coach_score(gym_id, coach_id):
    return f'fitness_center {gym_id} trainer {coach_id} score was updated'


@app.get('/user/reservations')
def get_reservations():
    return f'get_reservations'


@app.post('/user/reservations')
def post_reservations():
    return f'post_reservations'


@app.get('/user/reservations/<reservation_id>')
def get_reservations_id(reservation_id):
    return f'get_reservations_id {reservation_id}'


@app.put('/user/reservations/<reservation_id>')
def put_reservations_id(reservation_id):
    return f'put_reservations_id {reservation_id}'


@app.delete('/user/reservations/<reservation_id>')
def delete_reservations_id(reservation_id):
    return f'delete {reservation_id}'


@app.get('/user/checkout')
def get_checkout():
    return f'get_checkout'


@app.post('/user/checkout')
def post_checkout():
    return f'post_checkout'


@app.put('/user/checkout')
def put_checkout():
    return f'put_checkout'


@app.get('/fitness_center/<gym_id>')
def get_fitness_center_id(gym_id):
    return f'get_fitness_center_id {gym_id}'


# @app.get('/fitness_center/<gym_id>/loyality_programs')
# def get_loyality_programs():
#     return f'loyality_programs {gym_id}' # Не определились


if __name__ == '__main__':
    app.run()
