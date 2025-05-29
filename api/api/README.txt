Instalar as dependências 

pip install bcrypt
pip install PyJWT
pip install datetime
pip install flask
pip install hashlib

ou 

python3 -m pip install bcrypt --break-system-packages
python3 -m pip install PyJWT --break-system-packages
python3 -m pip install datetime --break-system-packages
python3 -m pip install flask --break-system-packages
python3 -m pip install hashlib --break-system-packages

Depois executar os scripts

python3 MD5Api.py

Para API vulnerável MD5Api
Exemplo de retorno do shell
----------------------------------
 * Serving Flask app 'MD5Api'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 806-844-528
----------------------------------
Agora só acessar os métodos da api com curl

Comandos shell pegar token com credencial do usuário para acesso
curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "teste", "password": "123senha"}'
curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "admin", "password": "senha123"}'

{
  "token": "c370daca2aebfc52cb1cfa6ccb7df526"
}

Comando shell para verificar autorização
curl -X GET http://127.0.0.1:5000/dados -H "Authorization: c370daca2aebfc52cb1cfa6ccb7df526"

{
  "message": "Acesso concedido! Usuario: teste"
}

--------------
Agora executar API com a vulnerabilidade corrigida 
python3 BCRYPTApi.py

Comandos shell pegar token com credencial do usuário para acesso
curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "teste", "password": "123senha"}'
curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "admin", "password": "senha123"}'

{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdGUiLCJleHAiOjE3NDc4OTg1NTh9.1Tz2-l-E6TTNUhn8G5-QAvDQK7pgAv-q7ft_OCnnr8c"
}

Aqui já dá pra perceber que o token é bem maior e ele muda a cada execução 

Ai o resto da execução é igual

Comando shell para verificar autorização
curl -X GET http://127.0.0.1:5000/dados -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdGUiLCJleHAiOjE3NDc4OTg1NTh9.1Tz2-l-E6TTNUhn8G5-QAvDQK7pgAv-q7ft_OCnnr8c"

{
  "message": "Acesso concedido! Usuario: teste"
}


O arquivo de senha.txt é igual para os 2 scripts como base de dados para a senha

admin:senha123
teste:123senha
--------------------

Esse exemplo dá pra capturar pacotes e mostrar no wireshark


