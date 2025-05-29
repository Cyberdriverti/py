from cvss import CVSS3

def calcular_cvss(cvss_vector):
    try:
        score = CVSS3(cvss_vector).score()
        return score
    except Exception as e:
        return {"erro": f"Erro ao calcular CVSS: {str(e)}"}