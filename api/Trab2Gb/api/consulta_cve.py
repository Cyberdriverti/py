import requests

def buscar_cve(cve_id):
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        return dados
    else:
        return {"erro": f"CVE {cve_id} não encontrada."}