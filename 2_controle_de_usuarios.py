from flask import Flask, request

app = Flask(__name__)
#Exibir caracteres especiais sem bug
app.config['JSON_AS_ASCII'] = False
users_data = {
    1: {
        'id':1,
        'name':'João'
    },
    2: {
        'id':2,
        'name':'Beatriz'
    },
    3: {
        'id':3,
        'name':'Aline'
    }
}

def response_users():
    return {'users': list(users_data.values())}

@app.route('/')
def root():
    return '<h1>API com Flask</h1>'

@app.route('/users')
def list_users():
    return response_users()

#Deve receber a requisição post e o body deve conter um JSon similar a: {"name": "Thiago"}
@app.route('/users', methods=['POST'])
def create_user():
    body = request.json

    ids = list(users_data.keys())

    #Se houver valor em IDS, new_id será o ultimo numero + 1
    if ids:
        new_id = ids[-1] + 1
    else:
        new_id = 1

    users_data[new_id] = {
        'id': new_id,
        #valor do name (resposta da requisição)
        'name': body['name']
    }

    return response_users()

@app.route('/users/<int:user_id>', methods=['PUT'])
def update(user_id: int):
    body = request.json
    name = body.get('name')

    if user_id in users_data:
        users_data[user_id]['name'] = name
    return response_users()


#Deve ser passado na url da requisicao o Id que será usada pela f
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete(user_id: int):
    user = users_data.get(user_id)
    if user:
        del users_data[user_id]
    return response_users()

app.run(debug=True)