import requests

def buscar_cve(cve_id):
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        return dados
    else:
        print("❌ Erro ao buscar CVE:", response.status_code)
        return None

# Teste
cve_id = input("Digite o CVE (exemplo: CVE-2021-34527): ")
dados_cve = buscar_cve(cve_id)

if dados_cve:
    print("\n🔹 Informações da CVE:")
    
    if 'id' in dados_cve:
        print(f"ID: {dados_cve['id']}")
    if 'summary' in dados_cve:
        print(f"Descrição: {dados_cve['summary']}")
    if 'Published' in dados_cve:
        print(f"Publicado em: {dados_cve['Published']}")
    if 'Last modified' in dados_cve:
        print(f"Última atualização: {dados_cve['Last modified']}")
else:
    print("❌ CVE não encontrada.")