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
    "https://www.foxnews.com/video/5614615980001",
    "https://www.foxnews.com/video/5614626175001"
]

# Caminhos dos arquivos de saída
output_files = ["FXN.m3u8", "FXNB.m3u8"]

# Itera sobre as URLs e os arquivos de saída
for url, output_file in zip(urls, output_files):
    with open(output_file, "w") as f:
        f.write(url + "\n")  # Escreve apenas a URL no arquivo

    # Executa o comando allfinder
    command = ["allfinder"] + [url] + ["-o", output_file]
    subprocess.run(command, check=True)

    print(f"Lista gerada com sucesso para {url}, arquivo: {output_file}")
