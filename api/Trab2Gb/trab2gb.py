import requests

def buscar_cve(cve_id):
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        return dados
    else:
        return None

# Exemplo de uso
cve_id = input("Digite o CVE (exemplo: CVE-2021-34527): ")
dados_cve = buscar_cve(cve_id)

if dados_cve:
    print(f"🔹 ID: {dados_cve['id']}")
    print(f"🔹 Descrição: {dados_cve['summary']}")
    print(f"🔹 Publicado em: {dados_cve['Published']}")
    print(f"🔹 Última atualização: {dados_cve['Last modified']}")
else:
    print("❌ CVE não encontrado.")