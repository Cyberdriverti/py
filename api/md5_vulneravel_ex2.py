# arquivo: inseguro_md5_gui.py

import tkinter as tk
from tkinter import messagebox
import hashlib

hash_inseguro = None

# Lista simulada de senhas comuns (dicionário)
dicionario_comum = [
    "123456", "senha", "admin", "senha123", "qwerty", "12345678", "abcdef", "000000"
]

# Função para gerar hash MD5
def armazenar_md5(senha: str) -> str:
    return hashlib.md5(senha.encode()).hexdigest()

# Verificar se o hash corresponde
def verificar_md5(senha: str, hash_armazenado: str) -> bool:
    return armazenar_md5(senha) == hash_armazenado

# Salvar a senha (hash MD5)
def salvar():
    global hash_inseguro
    senha = entry_senha.get()
    if not senha:
        messagebox.showwarning("Erro", "Digite uma senha.")
        return
    hash_inseguro = armazenar_md5(senha)
    messagebox.showinfo("Salvo", f"Senha armazenada em MD5 (inseguro).\nHash: {hash_inseguro}")

# Verificar se a senha está correta
def verificar():
    tentativa = entry_tentativa.get()
    if not tentativa:
        messagebox.showwarning("Erro", "Digite a senha para verificar.")
        return
    if not hash_inseguro:
        messagebox.showwarning("Erro", "Nenhuma senha armazenada.")
        return

    if verificar_md5(tentativa, hash_inseguro):
        messagebox.showinfo("Resultado", "✅ Acesso concedido (MD5 - inseguro)")
    else:
        messagebox.showerror("Resultado", "❌ Acesso negado (MD5 - inseguro)")

# Simular ataque de dicionário
def ataque_dicionario():
    if not hash_inseguro:
        messagebox.showwarning("Erro", "Nenhuma senha armazenada para atacar.")
        return

    resultado = "Iniciando ataque de dicionário...\n\n"
    for tentativa in dicionario_comum:
        hash_teste = armazenar_md5(tentativa)
        resultado += f"Tentando: {tentativa} -> {hash_teste}\n"
        if hash_teste == hash_inseguro:
            resultado += f"\n💀 SENHA QUEBRADA: {tentativa}"
            messagebox.showinfo("Ataque bem-sucedido", resultado)
            return

    resultado += "\n❌ Senha não encontrada no dicionário."
    messagebox.showerror("Ataque falhou", resultado)

# Interface gráfica
janela = tk.Tk()
janela.title("Senha Insegura com MD5")

# Cadastro
tk.Label(janela, text="Cadastrar senha:").pack()
entry_senha = tk.Entry(janela, show='*')
entry_senha.pack()
tk.Button(janela, text="Salvar Senha (MD5)", command=salvar).pack(pady=5)

# Verificação
tk.Label(janela, text="Verificar senha:").pack()
entry_tentativa = tk.Entry(janela, show='*')
entry_tentativa.pack()
tk.Button(janela, text="Verificar Senha", command=verificar).pack(pady=5)

# Ataque de dicionário
tk.Label(janela, text="Teste de quebra de senha com ataque de dicionário:").pack(pady=5)
tk.Button(janela, text="Executar Ataque", fg="red", command=ataque_dicionario).pack(pady=5)

janela.mainloop()
