import tkinter as tk
from tkinter import messagebox
import random
import string

class GeradorSenhas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Senhas")
        self.root.geometry("400x500")
        self.root.configure(bg='#ffffff')

        # Título
        self.titulo = tk.Label(root, text="Gerador de Senhas", font=("Arial", 20, "bold"), bg='#f0f0f0')
        self.titulo.pack(pady=20)

        # Frame para opções
        self.frame_opcoes = tk.Frame(root, bg='#f0f0f0')
        self.frame_opcoes.pack(pady=10)

        # Checkbuttons para tipos de caracteres
        self.usar_maiusculas = tk.BooleanVar(value=True)
        self.cb_maiusculas = tk.Checkbutton(self.frame_opcoes, text="Maiúsculas (A-Z)", 
                                           variable=self.usar_maiusculas, bg='#f0f0f0')
        self.cb_maiusculas.pack(anchor='w', pady=5)

        self.usar_minusculas = tk.BooleanVar(value=True)
        self.cb_minusculas = tk.Checkbutton(self.frame_opcoes, text="Minúsculas (a-z)", 
                                           variable=self.usar_minusculas, bg='#f0f0f0')
        self.cb_minusculas.pack(anchor='w', pady=5)

        self.usar_numeros = tk.BooleanVar(value=True)
        self.cb_numeros = tk.Checkbutton(self.frame_opcoes, text="Números (0-9)", 
                                        variable=self.usar_numeros, bg='#f0f0f0')
        self.cb_numeros.pack(anchor='w', pady=5)

        self.usar_especiais = tk.BooleanVar(value=True)
        self.cb_especiais = tk.Checkbutton(self.frame_opcoes, text="Caracteres Especiais (!@#$%)", 
                                          variable=self.usar_especiais, bg='#f0f0f0')
        self.cb_especiais.pack(anchor='w', pady=5)

        # Frame para comprimento da senha
        self.frame_comprimento = tk.Frame(root, bg='#f0f0f0')
        self.frame_comprimento.pack(pady=10)

        self.label_comprimento = tk.Label(self.frame_comprimento, text="Comprimento da senha:", 
                                        bg='#f0f0f0')
        self.label_comprimento.pack(side='left')

        self.comprimento = tk.StringVar(value="12")
        self.entrada_comprimento = tk.Entry(self.frame_comprimento, textvariable=self.comprimento, 
                                          width=5)
        self.entrada_comprimento.pack(side='left', padx=5)

        # Botão gerar senha
        self.botao_gerar = tk.Button(root, text="Gerar Senha", command=self.gerar_senha,
                                   bg='#4CAF50', fg='white', font=("Arial", 12), 
                                   relief='raised', padx=20)
        self.botao_gerar.pack(pady=20)

        # Campo para mostrar a senha
        self.senha_gerada = tk.StringVar()
        self.entrada_senha = tk.Entry(root, textvariable=self.senha_gerada, 
                                    font=("Arial", 14), width=25)
        self.entrada_senha.pack(pady=10)

        # Botão copiar senha
        self.botao_copiar = tk.Button(root, text="Copiar Senha", command=self.copiar_senha,
                                    bg='#2196F3', fg='white', font=("Arial", 12),
                                    relief='raised', padx=20)
        self.botao_copiar.pack(pady=10)

    def gerar_senha(self):
        try:
            comprimento = int(self.comprimento.get())
            if comprimento <= 0:
                messagebox.showerror("Erro", "O comprimento deve ser maior que zero!")
                return
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido para o comprimento!")
            return

        caracteres = ""
        if self.usar_maiusculas.get():
            caracteres += string.ascii_uppercase
        if self.usar_minusculas.get():
            caracteres += string.ascii_lowercase
        if self.usar_numeros.get():
            caracteres += string.digits
        if self.usar_especiais.get():
            caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?"

        if not caracteres:
            messagebox.showerror("Erro", "Selecione pelo menos um tipo de caractere!")
            return

        senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
        self.senha_gerada.set(senha)

    def copiar_senha(self):
        senha = self.senha_gerada.get()
        if senha:
            self.root.clipboard_clear()
            self.root.clipboard_append(senha)
            messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")
        else:
            messagebox.showwarning("Aviso", "Nenhuma senha gerada para copiar!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeradorSenhas(root)
    root.mainloop()
