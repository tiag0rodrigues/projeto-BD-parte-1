from flask import Flask, make_response, jsonify, request

Usuario = [
    {'cpf': 11122233344, 'nome': 'Jose', 'data_nascimento': '(2000, 4, 2)'}
]

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/usuarioG', methods=['GET'])
def get_Usuario():
    return make_response(
        jsonify(Usuario)
    )

@app.route('/usuarioP', methods=['POST'])
def post_usuario():
    user = request.json
    Usuario.append(user)
    
    f = open('usuario.txt', 'a')
    f.write('{}\n'.format(user))
    f.close()

    return user

app.run()
