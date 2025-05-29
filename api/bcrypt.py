# arquivo: seguro_bcrypt_gui.py

import tkinter as tk
from tkinter import messagebox
import bcrypt

hash_seguro = None
senha_salva = None

# Função para gerar hash bcrypt
def armazenar_bcrypt(senha: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode(), salt).decode()

# Verificar senha usando bcrypt
def verificar_bcrypt(senha: str, hash_armazenado: str) -> bool:
    return bcrypt.checkpw(senha.encode(), hash_armazenado.encode())

# Salvar senha (hash seguro)
def salvar():
    global hash_seguro, senha_salva
    senha = entry_senha.get()
    if not senha:
        messagebox.showwarning("Erro", "Digite uma senha.")
        return
    senha_salva = senha
    hash_seguro = armazenar_bcrypt(senha)
    messagebox.showinfo(
        "Senha Salva",
        f"✅ Senha cadastrada: {senha_salva}\n🔐 Hash gerado:\n{hash_seguro}"
    )

# Verificar se a senha está correta
def verificar():
    tentativa = entry_tentativa.get()
    if not tentativa:
        messagebox.showwarning("Erro", "Digite a senha para verificar.")
        return
    if not hash_seguro:
        messagebox.showwarning("Erro", "Nenhuma senha armazenada.")
        return

    if verificar_bcrypt(tentativa, hash_seguro):
        messagebox.showinfo(
            "Resultado",
            f"✅ Acesso concedido!\nSenha cadastrada: {senha_salva}\nHash armazenado:\n{hash_seguro}"
        )
    else:
        messagebox.showerror(
            "Resultado",
            f"❌ Acesso negado!\nSenha cadastrada: {senha_salva}\nHash armazenado:\n{hash_seguro}"
        )

# Interface gráfica
janela = tk.Tk()
janela.title("Senha Segura com bcrypt")

# Cadastro
tk.Label(janela, text="Cadastrar senha:").pack()
entry_senha = tk.Entry(janela, show='*')
entry_senha.pack()
tk.Button(janela, text="Salvar Senha (bcrypt)", command=salvar).pack(pady=5)

# Verificação
tk.Label(janela, text="Verificar senha:").pack()
entry_tentativa = tk.Entry(janela, show='*')
entry_tentativa.pack()
tk.Button(janela, text="Verificar Senha", command=verificar).pack(pady=5)

janela.mainloop()
