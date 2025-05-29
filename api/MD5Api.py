
# Código Vulnerável (Texto Puro + MD5)
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Função para carregar credenciais do arquivo senha.txt
def carregar_usuarios():
    usuarios = {}
    with open("senha.txt", "r") as f:
        for linha in f:
            partes = linha.strip().split(":")
            if len(partes) == 2:
                usuarios[partes[0]] = partes[1]  # username -> senha em texto puro
    return usuarios

usuarios = carregar_usuarios()

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in usuarios and usuarios[username] == password:  # Comparação direta 😱
        token = hashlib.md5(password.encode()).hexdigest()  # Gerando token MD5
        return jsonify({"token": token}), 200

    return jsonify({"error": "Credenciais inválidas"}), 401

@app.route("/dados", methods=["GET"])
def dados():
    token = request.headers.get("Authorization")
    for user, senha in usuarios.items():
        if token == hashlib.md5(senha.encode()).hexdigest():
            return jsonify({"message": f"Acesso concedido! Usuario: {user}"}), 200

    return jsonify({"error": "Acesso negado"}), 403

if __name__ == "__main__":
    app.run(debug=True)

#Comandos shell pegar token com credencial do usuário para acesso
#curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "teste", "password": "123senha"}'
#curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "admin", "password": "senha123"}'

#Comandos shell consultar dados com token
#curl -X GET http://127.0.0.1:5000/dados -H "Authorization: c370daca2aebfc52cb1cfa6ccb7df526"
#curl -X GET http://127.0.0.1:5000/dados -H "Authorization: e7d80ffeefa212b7c5c55700e4f7193e"
