import tkinter as tk
from tkinter import messagebox
from collections import Counter
import random
import pandas as pd

# Lista para armazenar os números inseridos e os jogos gerados
numeros_inseridos = []
jogos_gerados = []


# Função para limpar as caixas de entrada
def limpar_caixas():
    for entry in entries_numeros:
        entry.delete(0, tk.END)


# Função para inserir os números e armazená-los
def inserir_numeros():
    numeros = []
    for entry in entries_numeros:
        numero = entry.get().strip()
        if numero.isdigit():
            numeros.append(int(numero))
        else:
            messagebox.showerror("Erro de Inserção", "Por favor, insira apenas números inteiros.")
            return

    if len(numeros) != 15:
        messagebox.showerror("Erro de Inserção", "Por favor, insira exatamente 15 números.")
    else:
        numeros_inseridos.append(numeros)
        messagebox.showinfo("Inserção Concluída", "Números inseridos com sucesso!")
        limpar_caixas()


# Função para gerar um jogo baseado nos números mais frequentes inseridos
def gerar_jogo():
    if not numeros_inseridos:
        messagebox.showerror("Erro", "Nenhum número inserido ainda. Insira pelo menos um jogo.")
        return

    # Contagem de frequência de cada número nos números inseridos
    contagem_numeros = Counter()
    for numeros in numeros_inseridos:
        for numero in numeros:
            contagem_numeros[numero] += 1

    # Ordenando os números por frequência
    numeros_ordenados = sorted(contagem_numeros.items(), key=lambda x: x[1], reverse=True)

    # Selecionando 15 números dos mais frequentes ou completando aleatoriamente se não houverem 15 números frequentes
    numeros_jogo = [numero for numero, frequencia in numeros_ordenados][:15]
    while len(numeros_jogo) < 15:
        numero_aleatorio = random.randint(1, 25)
        if numero_aleatorio not in numeros_jogo:
            numeros_jogo.append(numero_aleatorio)

    jogos_gerados.append(numeros_jogo)
    messagebox.showinfo("Jogo Gerado", f"Jogo gerado: {numeros_jogo}")


# Função para ver os números inseridos
def ver_numeros_inseridos():
    if numeros_inseridos:
        msg = "Números Inseridos:\n\n"
        for i, numeros in enumerate(numeros_inseridos, start=1):
            msg += f"Jogo {i}: {numeros}\n"
        messagebox.showinfo("Números Inseridos", msg)
    else:
        messagebox.showinfo("Números Inseridos", "Nenhum número foi inserido ainda.")


# Função para ver os jogos gerados
def ver_jogos_gerados():
    if jogos_gerados:
        msg = "Jogos Gerados:\n\n"
        for i, jogo in enumerate(jogos_gerados, start=1):
            msg += f"Jogo {i}: {jogo}\n"
        messagebox.showinfo("Jogos Gerados", msg)
    else:
        messagebox.showinfo("Jogos Gerados", "Nenhum jogo foi gerado ainda.")


# Função para exportar os jogos gerados para um arquivo PDF
def exportar_para_pdf():
    if not jogos_gerados:
        messagebox.showerror("Erro", "Nenhum jogo gerado ainda.")
        return

    try:
        from fpdf import FPDF
    except ImportError:
        messagebox.showerror("Erro", "O módulo fpdf não está instalado. Instale-o usando 'pip install fpdf'.")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Jogos Gerados", ln=True, align='C')

    for i, jogo in enumerate(jogos_gerados, start=1):
        pdf.cell(200, 10, txt=f"Jogo {i}: {jogo}", ln=True, align='L')

    pdf_output = "jogos_gerados.pdf"
    pdf.output(pdf_output)
    messagebox.showinfo("Exportação Concluída", f"Jogos gerados foram exportados para {pdf_output}")


# Função para exportar os jogos gerados para um arquivo Excel
def exportar_para_excel():
    if not jogos_gerados:
        messagebox.showerror("Erro", "Nenhum jogo gerado ainda.")
        return

    df = pd.DataFrame(jogos_gerados, columns=[f"Número {i + 1}" for i in range(15)])
    excel_output = "jogos_gerados.xlsx"
    df.to_excel(excel_output, index=False)
    messagebox.showinfo("Exportação Concluída", f"Jogos gerados foram exportados para {excel_output}")


# Configuração do tkinter
root = tk.Tk()
root.title("Análise e Geração de Jogo")

# Lista de Entry para os números do jogo
entries_numeros = []
for i in range(15):
    label = tk.Label(root, text=f"Número {i + 1}:")
    label.grid(row=i, column=0, padx=10, pady=5)

    entry = tk.Entry(root, width=10)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries_numeros.append(entry)

# Botão para inserir os números
button_inserir = tk.Button(root, text="Inserir Números", command=inserir_numeros)
button_inserir.grid(row=15, column=0, columnspan=2, pady=10)

# Botão para ver os números inseridos
button_ver_inseridos = tk.Button(root, text="Ver Números Inseridos", command=ver_numeros_inseridos)
button_ver_inseridos.grid(row=16, column=0, columnspan=2, pady=10)

# Botão para gerar jogo
button_gerar = tk.Button(root, text="Gerar Jogo", command=gerar_jogo)
button_gerar.grid(row=17, column=0, columnspan=2, pady=5)

# Botão para ver os jogos gerados
button_ver_jogos = tk.Button(root, text="Ver Jogos Gerados", command=ver_jogos_gerados)
button_ver_jogos.grid(row=18, column=0, columnspan=2, pady=5)

# Botão para exportar jogos gerados para PDF
button_exportar_pdf = tk.Button(root, text="Exportar para PDF", command=exportar_para_pdf)
button_exportar_pdf.grid(row=19, column=0, columnspan=2, pady=5)

# Botão para exportar jogos gerados para Excel
button_exportar_excel = tk.Button(root, text="Exportar para Excel", command=exportar_para_excel)
button_exportar_excel.grid(row=20, column=0, columnspan=2, pady=5)

root.mainloop()
import tkinter as tk
from tkinter import messagebox
from collections import Counter
import random
import pandas as pd

# Lista para armazenar os números inseridos e os jogos gerados
numeros_inseridos = []
jogos_gerados = []


# Função para limpar as caixas de entrada
def limpar_caixas():
    for entry in entries_numeros:
        entry.delete(0, tk.END)


# Função para inserir os números e armazená-los
def inserir_numeros():
    numeros = []
    for entry in entries_numeros:
        numero = entry.get().strip()
        if numero.isdigit():
            numeros.append(int(numero))
        else:
            messagebox.showerror("Erro de Inserção", "Por favor, insira apenas números inteiros.")
            return

    if len(numeros) != 15:
        messagebox.showerror("Erro de Inserção", "Por favor, insira exatamente 15 números.")
    else:
        numeros_inseridos.append(numeros)
        messagebox.showinfo("Inserção Concluída", "Números inseridos com sucesso!")
        limpar_caixas()


# Função para gerar um jogo baseado nos números mais frequentes inseridos
def gerar_jogo():
    if not numeros_inseridos:
        messagebox.showerror("Erro", "Nenhum número inserido ainda. Insira pelo menos um jogo.")
        return

    # Contagem de frequência de cada número nos números inseridos
    contagem_numeros = Counter()
    for numeros in numeros_inseridos:
        for numero in numeros:
            contagem_numeros[numero] += 1

    # Ordenando os números por frequência
    numeros_ordenados = sorted(contagem_numeros.items(), key=lambda x: x[1], reverse=True)

    # Selecionando 15 números dos mais frequentes ou completando aleatoriamente se não houverem 15 números frequentes
    numeros_jogo = [numero for numero, frequencia in numeros_ordenados][:15]
    while len(numeros_jogo) < 15:
        numero_aleatorio = random.randint(1, 25)
        if numero_aleatorio not in numeros_jogo:
            numeros_jogo.append(numero_aleatorio)

    jogos_gerados.append(numeros_jogo)
    messagebox.showinfo("Jogo Gerado", f"Jogo gerado: {numeros_jogo}")


# Função para ver os números inseridos
def ver_numeros_inseridos():
    if numeros_inseridos:
        msg = "Números Inseridos:\n\n"
        for i, numeros in enumerate(numeros_inseridos, start=1):
            msg += f"Jogo {i}: {numeros}\n"
        messagebox.showinfo("Números Inseridos", msg)
    else:
        messagebox.showinfo("Números Inseridos", "Nenhum número foi inserido ainda.")


# Função para ver os jogos gerados
def ver_jogos_gerados():
    if jogos_gerados:
        msg = "Jogos Gerados:\n\n"
        for i, jogo in enumerate(jogos_gerados, start=1):
            msg += f"Jogo {i}: {jogo}\n"
        messagebox.showinfo("Jogos Gerados", msg)
    else:
        messagebox.showinfo("Jogos Gerados", "Nenhum jogo foi gerado ainda.")


# Função para exportar os jogos gerados para um arquivo PDF
def exportar_para_pdf():
    if not jogos_gerados:
        messagebox.showerror("Erro", "Nenhum jogo gerado ainda.")
        return

    try:
        from fpdf import FPDF
    except ImportError:
        messagebox.showerror("Erro", "O módulo fpdf não está instalado. Instale-o usando 'pip install fpdf'.")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Jogos Gerados", ln=True, align='C')

    for i, jogo in enumerate(jogos_gerados, start=1):
        pdf.cell(200, 10, txt=f"Jogo {i}: {jogo}", ln=True, align='L')

    pdf_output = "jogos_gerados.pdf"
    pdf.output(pdf_output)
    messagebox.showinfo("Exportação Concluída", f"Jogos gerados foram exportados para {pdf_output}")


# Função para exportar os jogos gerados para um arquivo Excel
def exportar_para_excel():
    if not jogos_gerados:
        messagebox.showerror("Erro", "Nenhum jogo gerado ainda.")
        return

    df = pd.DataFrame(jogos_gerados, columns=[f"Número {i + 1}" for i in range(15)])
    excel_output = "jogos_gerados.xlsx"
    df.to_excel(excel_output, index=False)
    messagebox.showinfo("Exportação Concluída", f"Jogos gerados foram exportados para {excel_output}")


# Configuração do tkinter
root = tk.Tk()
root.title("Análise e Geração de Jogo")

# Lista de Entry para os números do jogo
entries_numeros = []
for i in range(15):
    label = tk.Label(root, text=f"Número {i + 1}:")
    label.grid(row=i, column=0, padx=10, pady=5)

    entry = tk.Entry(root, width=10)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries_numeros.append(entry)

# Botão para inserir os números
button_inserir = tk.Button(root, text="Inserir Números", command=inserir_numeros)
button_inserir.grid(row=15, column=0, columnspan=2, pady=10)

# Botão para ver os números inseridos
button_ver_inseridos = tk.Button(root, text="Ver Números Inseridos", command=ver_numeros_inseridos)
button_ver_inseridos.grid(row=16, column=0, columnspan=2, pady=10)

# Botão para gerar jogo
button_gerar = tk.Button(root, text="Gerar Jogo", command=gerar_jogo)
button_gerar.grid(row=17, column=0, columnspan=2, pady=5)

# Botão para ver os jogos gerados
button_ver_jogos = tk.Button(root, text="Ver Jogos Gerados", command=ver_jogos_gerados)
button_ver_jogos.grid(row=18, column=0, columnspan=2, pady=5)

# Botão para exportar jogos gerados para PDF
button_exportar_pdf = tk.Button(root, text="Exportar para PDF", command=exportar_para_pdf)
button_exportar_pdf.grid(row=19, column=0, columnspan=2, pady=5)

# Botão para exportar jogos gerados para Excel
button_exportar_excel = tk.Button(root, text="Exportar para Excel", command=exportar_para_excel)
button_exportar_excel.grid(row=20, column=0, columnspan=2, pady=5)

root.mainloop()
