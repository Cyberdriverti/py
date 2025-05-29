from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hmac, hashlib

# Criptografia sem autenticar (inseguro)
def criptografar_sem_hmac(msg, chave, iv):
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(msg, AES.block_size))

# Criptografia com HMAC (seguro)
def criptografar_com_hmac(msg, chave, iv, chave_hmac):
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(msg, AES.block_size))
    mac = hmac.new(chave_hmac, ciphertext, hashlib.sha256).digest()
    return ciphertext + mac

# Verifica integridade e descriptografa (inseguro)
def descriptografar_sem_hmac(dados, chave, iv, chave_hmac):
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(bytes(dados)), AES.block_size)

# Verifica integridade e descriptografa (seguro)
def descriptografar_com_hmac(dados, chave, iv, chave_hmac):
    ciphertext = dados[:-32]
    mac_recebido = dados[-32:]
    mac_calculado = hmac.new(chave_hmac, ciphertext, hashlib.sha256).digest()
    if not hmac.compare_digest(mac_recebido, mac_calculado):
        return b"ERRO: dados modificados"
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size)

def main():
    msg = b"mensagem secreta"
    chave = get_random_bytes(32)
    iv = get_random_bytes(16)
    chave_hmac = get_random_bytes(32)

    # Criptografia insegura
    cripto_inseguro = criptografar_sem_hmac(msg, chave, iv)
    alterado_inseguro = bytearray(cripto_inseguro)
    alterado_inseguro[0] ^= 0x01  # altera um byte

    # Criptografia segura
    cripto_seguro = criptografar_com_hmac(msg, chave, iv, chave_hmac)
    alterado_seguro = bytearray(cripto_seguro)
    alterado_seguro[0] ^= 0x01  # altera um byte

    try:
        resultado_inseguro = descriptografar_sem_hmac(alterado_inseguro, chave, iv, chave_hmac)
    except ValueError:
        resultado_inseguro = b"ERRO: dados corrompidos"

    resultado_seguro = descriptografar_com_hmac(bytes(alterado_seguro), chave, iv, chave_hmac)

    print("Resultado sem HMAC :", resultado_inseguro.decode(errors="ignore"))
    print("Resultado com HMAC :", resultado_seguro.decode(errors="ignore"))

if __name__ == "__main__":
    main()