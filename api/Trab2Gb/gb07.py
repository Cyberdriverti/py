import requests

def buscar_cve(cve_id):
    url = f"https://cve.edgewatch.net/api/cves/{cve_id}"
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

    if 'cve' in dados_cve and 'id' in dados_cve['cve']:
        print(f"ID: {dados_cve['cve']['id']}\n")

    if 'summary' in dados_cve['cve']:
        print(f"Descrição: {dados_cve['cve']['summary']}\n")

    if 'cvss' in dados_cve['cve']:
        print(f"Pontuação CVSS: {dados_cve['cve']['cvss']}\n")

    if 'impact' in dados_cve['cve']:
        print(f"Impacto: {dados_cve['cve']['impact']}\n")
else:
    print("❌ CVE não encontrada.")