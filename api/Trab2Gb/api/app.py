from flask import Flask, request, jsonify
from consulta_cve import buscar_cve
from calcula_cvss import calcular_cvss

app = Flask(__name__)

@app.route('/cve/<cve_id>', methods=['GET'])
def consultar_cve(cve_id):
    dados = buscar_cve(cve_id)
    return jsonify(dados)

@app.route('/cvss', methods=['POST'])
def calcular_pontuacao():
    data = request.json
    vetor_cvss = data.get("cvss_vector")
    resultado = calcular_cvss(vetor_cvss)
    return jsonify({"pontuacao_cvss": resultado})

if __name__ == '__main__':
    app.run(debug=True)

