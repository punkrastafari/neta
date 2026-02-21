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
    # Executa o comando allfinder para buscar as m3u8
    command = ["allfinder"] + [url] + ["-o", output_file]
    subprocess.run(command, check=True)

    # Agora, vamos limpar o arquivo gerado para remover as linhas desnecessárias
    with open(output_file, "r") as f:
        lines = f.readlines()

    # Filtra apenas as linhas que são URLs (removendo #EXTM3U e #EXTINF)
    cleaned_lines = [line.strip() for line in lines if not line.startswith("#")]

    # Grava as URLs no arquivo .m3u8, sem as linhas de #EXTM3U ou #EXTINF
    with open(output_file, "w") as f:
        for line in cleaned_lines:
            if line:  # Adiciona apenas linhas não vazias
                f.write(line + "\n")

    print(f"Lista gerada com sucesso para {url}, arquivo: {output_file}")
