import subprocess

# Lista de URLs
urls = [
"https://www.foxnews.com/video/5614615980001"
]

# Monta o comando
command = ["allfinder"] + urls + ["-o", "lista_final.m3u"]

# Executa
subprocess.run(command, check=True)

print("Lista gerada com sucesso!")
