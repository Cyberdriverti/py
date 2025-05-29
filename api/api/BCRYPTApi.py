#Código Seguro (bcrypt + JWT)
import bcrypt
import jwt
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
SECRET_KEY = "chave_super_secreta"

# Função para carregar credenciais do arquivo senha.txt (convertendo para bcrypt)
def carregar_usuarios():
    usuarios = {}
    with open("C:\Users\Ricardo\Documents\py\api\api\senha.txt", "r") as f:
        for linha in f:
            partes = linha.strip().split(":")
            if len(partes) == 2:
                senha_segura = bcrypt.hashpw(partes[1].encode(), bcrypt.gensalt()).decode()
                usuarios[partes[0]] = senha_segura  # username -> senha criptografada
    return usuarios

usuarios = carregar_usuarios()

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in usuarios and bcrypt.checkpw(password.encode(), usuarios[username].encode()):
        token = jwt.encode({"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=300)}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token}), 200

    return jsonify({"error": "Credenciais invalidas"}), 401

@app.route("/dados", methods=["GET"])
def dados():
    token = request.headers.get("Authorization")
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"message": f"Acesso concedido para {decoded['user']}!"}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expirado"}), 403
    except jwt.InvalidTokenError:
        return jsonify({"error": "Token invalido"}), 403

if __name__ == "__main__":
    app.run(debug=True)

#Comandos shell pegar token com credencial do usuário para acesso
#curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "teste", "password": "123senha"}'
#curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "admin", "password": "senha123"}'

#Comando para autenticar token
#curl -X GET http://127.0.0.1:5000/dados -H "Authorization: <TOKEN>"
