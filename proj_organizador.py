import os 
from tkinter.filedialog import askdirectory  #biblioteca para abrir pop up
caminho = askdirectory(title="Selecione uma pasta") 
#print(caminho) #apresenta o caminho da pasta C/
lista_arquivos = os.listdir(caminho)
#print(lista_arquivos) #lista os arquivos de uma pasta
#dicionario de arquivos 
locais = {
    "Imagens": [".png", ".jpg"],
    "Planilhas": [".xlsx"],
    "PDFs": [".pdf"],
    "csv": [".csv"],
    "pkt": [".pkt"],
    "PowerPoint": [".pptx"],
    "Python": [".py"],
}
for arquivos in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivos}")
    for pasta in locais:
        if extensao in locais[pasta]:
                if not os.path.exists(f"{caminho}/{pasta}"):
                    os.mkdir(f"{caminho}/{pasta}")
                os.rename(f"{caminho}/{arquivos}", f"{caminho}/{pasta}/{arquivos}")

