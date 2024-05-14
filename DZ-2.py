from flask import Flask

app = Flask(__name__)


@app.post('/register')
def post_user_register():
    return 'new user registered'


@app.get('/register')
def get_user_register():
    return 'please sign in to register'


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
    return 'user information'


@app.put('/user')
def put_user():
    return 'user info was successfully updated'


@app.post('/funds')
def post_funds():
    return 'user account was successfully funded'


@app.get('/funds')
def get_funds():
    return 'user deposit value'


@app.get('/fitness_center/<gym_id>/services/')
def get_services(gym_id):
    return f'fitness_center {gym_id} services list'


@app.get('/fitness_center/<gym_id>/services/<service_id>')
def get_service_info(gym_id, service_id):
    return f'fitness_center {gym_id} services {service_id} info'


@app.get('/fitness_center/<gym_id>/trainer/')
def get_trainers(gym_id):
    return f'fitness_center {gym_id} trainer list'


@app.get('/fitness_center/<gym_id>/trainer/<coach_id>/')
def get_coach_info(gym_id, coach_id):
    return f'fitness_center {gym_id} trainer {coach_id} info'


@app.get('/fitness_center/<gym_id>/<coach_id>/score')
def get_coach_score(gym_id, coach_id):
    return f'fitness_center {gym_id} trainer {coach_id} score'


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


@app.get('/fitness_center/<gym_id>/loyality_programs')
def get_loyality_programs():
    return f'loyality_programs {gym_id}'









