import requests

def buscar_cve(cve_id):
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        print("\n🔹 Resposta da API:", dados)  # Exibe o JSON completo para análise
        return dados
    else:
        print("❌ Erro ao buscar CVE:", response.status_code)
        return None

# Teste
cve_id = input("Digite o CVE (exemplo: CVE-2021-34527): ")
dados_cve = buscar_cve(cve_id)

if dados_cve:
    print("\n🔹 Informações da CVE:")
    
    if 'CVE_data_meta' in dados_cve:
        print(f"ID: {dados_cve['CVE_data_meta']['ID']}")
    if 'summary' in dados_cve:
        print(f"Descrição: {dados_cve['summary']}")
else:
    print("❌ CVE não encontrada.")