import subprocess
import tkinter as tk
from tkinter import messagebox

def root(text_area, insertText):
    text_area.delete("1.0", tk.END) 
    text_area.insert(tk.END, insertText)

def desligar():
    try:
        tempo = int(textArea.get("1.0", tk.END).strip())
        minutos = tempo // 60
        resposta = messagebox.askyesno("Confirmação", f"Você deseja desligar seu computador em {minutos} minutos?")
        if resposta:
            comando = fr'shutdown /s /f /t {tempo}'
            subprocess.run(comando, shell=True)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def reiniciar():
    try:
        tempo = int(textArea.get("1.0", tk.END).strip())
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

B_width0 = 15

B_width = 23
B_height = 2

ct = tk.Tk()
ct.title("Control")
ct.geometry("400x190+200+250")
ct.resizable(False, False)

container = tk.Frame(ct)
container.pack(padx=0, pady=5)
textArea = tk.Text(container, height=1, width=20, font=("Arial", 23), borderwidth=5)
textArea.grid(row=0, column=0, padx=0, pady=0)

containerButton0 = tk.Frame(ct)
containerButton0.pack(padx=0, pady=0)
button10 = tk.Button(containerButton0, text="10 minutos!", width=B_width0, height=B_height, command=lambda: root(textArea, "600"))
button10.grid(row=0, column=0, padx=0, pady=0)
button30 = tk.Button(containerButton0, text="30 minutos!", width=B_width0, height=B_height, command=lambda: root(textArea, "1800"))
button30.grid(row=0, column=1, padx=0, pady=0)
button60 = tk.Button(containerButton0, text="60 minutos!", width=B_width0, height=B_height, command=lambda: root(textArea, "3600"))
button60.grid(row=0, column=2, padx=0, pady=0)

containerButton1 = tk.Frame(ct)
containerButton1.pack(padx=0, pady=0)
buttonDesliga = tk.Button(containerButton1, text="Desligar", width=B_width, height=B_height, command=desligar)
buttonDesliga.grid(row=0, column=0, padx=0, pady=0)
buttonReiniciar = tk.Button(containerButton1, text="Reiniciar", width=B_width, height=B_height, command=reiniciar)
buttonReiniciar.grid(row=0, column=1, padx=0, pady=0)

containerButtonCancel = tk.Frame(ct)
containerButtonCancel.pack(padx=0, pady=0)
buttonCancel = tk.Button(containerButtonCancel, text="Cancelar", width=B_width, height=B_height, command=cancelar)
buttonCancel.grid(row=0, column=0, padx=5, pady=0)

ct.mainloop()
