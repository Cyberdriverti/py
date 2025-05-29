
import requests

def buscar_cve(cve_id):
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        print("\n🔹 Resposta completa da API:\n", dados)  # Exibe o JSON completo
        return dados
    else:
        print(f"❌ Erro ao buscar CVE ({response.status_code})")
        return None

# Teste
cve_id = input("Digite o CVE (exemplo: CVE-2021-34527): ")
dados_cve = buscar_cve(cve_id)

if dados_cve:
    print("\n🔹 Informações da CVE:\n")

    if 'CVE_data_meta' in dados_cve and 'ID' in dados_cve['CVE_data_meta']:
        print(f"ID: {dados_cve['CVE_data_meta']['ID']}\n")

    if 'summary' in dados_cve:
        print(f"Descrição: {dados_cve['summary']}\n")

    if 'Published' in dados_cve:
        print(f"Publicado em: {dados_cve['Published']}\n")

    if 'Last modified' in dados_cve:
        print(f"Última atualização: {dados_cve['Last modified']}\n")
else:
    print("❌ CVE não encontrada.")