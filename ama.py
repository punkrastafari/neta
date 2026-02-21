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

import subprocess

# Lista de URLs
urls = [
"https://www.foxnews.com/video/5614615980001"
]

# Monta o comando
command = ["allfinder"] + urls + ["-o", "FXN.m3u8"]

# Executa
subprocess.run(command, check=True)

print("Lista gerada com sucesso!")

import subprocess

# Lista de URLs
urls = [
"https://www.foxnews.com/video/5614626175001"
]

# Monta o comando
command = ["allfinder"] + urls + ["-o", "FXNB.m3u8"]

# Executa
subprocess.run(command, check=True)

print("Lista gerada com sucesso!")
