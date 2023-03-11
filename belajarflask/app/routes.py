from app import app
from app.controller import DosenController, UserController
from flask import request


@app.route('/')
def index():
    return 'Hello Flask App'

@app.route('/dosen', methods=['GET', 'POST'])
def dosens():
    if request.method == 'GET':
        return DosenController.index()
    else:
        return DosenController.save()

@app.route('/createadmin', methods=['GET', 'POST'])
def admins():
    if request.method == 'POST':
        return UserController.buatAdmin()

@app.route('/dosen/<id>', methods=['GET', 'PUT','DELETE'])
def dosenDetail(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    elif request.method == 'PUT':
        return DosenController.ubah(id)
    elif request.method == 'DELETE':
        return DosenController.hapus(id)
    
@app.route('/login', methods=['POST'])
def logins():
    return UserController.login()
