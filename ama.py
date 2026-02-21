import subprocess

# Lista de URLs
urls = [
"https://g1.globo.com/sp/campinas-regiao/videos-jornal-da-eptv-1-edicao-campinas-e-piracicaba/video/assista-a-integra-do-eptv-1-campinaspiracicaba-desta-sexta-20-de-fevereiro-de-2026-14365619.ghtml",
"https://g1.globo.com/df/distrito-federal/df1/video/df1-edicao-de-20022026-14364837.ghtml",
"https://globoplay.globo.com/v/14354933/?s=0s"
]

# Monta o comando
command = ["allfinder"] + urls + ["-o", "lista_final.m3u"]

# Executa
subprocess.run(command, check=True)

print("Lista gerada com sucesso!")
