import subprocess
import tkinter as tk
from tkinter import messagebox

def desligar():
    try:
        tempo = int(visor.get("1.0", tk.END).strip())
        minutos = tempo // 60
        resposta = messagebox.askyesno("Confirmação", f"Você deseja desligar seu computador em {minutos} minutos?")
        if resposta:
            comando = fr'shutdown /s /f /t {tempo}'
            subprocess.run(comando, shell=True)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def reiniciar():
    try:
        tempo = int(visor.get("1.0", tk.END).strip())
        minutos = tempo // 60
        resposta = messagebox.askyesno("Confirmação", f"Você deseja reiniciar seu computador em {minutos} minutos?")
        if resposta:
            comando = fr'shutdown /r /f /t {tempo}'
            subprocess.run(comando, shell=True)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def cancelar():
    comando = "shutdown /a"
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    if resultado.returncode != 0:
        messagebox.showerror("Erro", "Não foi possível anular o desligamento do sistema porque o sistema não estava sendo desligado.")

B_width = 23
B_height = 2

ct = tk.Tk()
ct.title("Control")
ct.geometry("400x150+200+250")
ct.resizable(False, False)

container = tk.Frame(ct)
container.pack(padx=0, pady=5)
visor = tk.Text(container, height=1, width=20, font=("Arial", 23), borderwidth=5)
visor.grid(row=0, column=0, padx=0, pady=0)

containerButton = tk.Frame(ct)
containerButton.pack(padx=0, pady=0)
buttonDesliga = tk.Button(containerButton, text="Desligar", width=B_width, height=B_height, command=desligar)
buttonDesliga.grid(row=0, column=0, padx=0, pady=0)
buttonReiniciar = tk.Button(containerButton, text="Reiniciar", width=B_width, height=B_height, command=reiniciar)
buttonReiniciar.grid(row=0, column=1, padx=0, pady=0)

containerButtonCancel = tk.Frame(ct)
containerButtonCancel.pack(padx=0, pady=0)
buttonCancel = tk.Button(containerButtonCancel, text="Cancelar", width=B_width, height=B_height, command=cancelar)
buttonCancel.grid(row=0, column=0, padx=5, pady=0)

ct.mainloop()
