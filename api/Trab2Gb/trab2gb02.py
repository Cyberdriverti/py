import requests

def buscar_cve(cve_id):
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        print("🔹 Resposta da API:", dados)  # Adiciona esta linha para visualizar o JSON
        return dados
    else:
        print("❌ Erro ao buscar CVE:", response.status_code)
        return None

# Teste
cve_id = input("Digite o CVE (exemplo: CVE-2021-34527): ")
dados_cve = buscar_cve(cve_id)

if dados_cve:
    if 'id' in dados_cve:
        print(f"🔹 ID: {dados_cve['id']}")
    else:
        print("❌ A resposta da API não contém o campo 'id'.")