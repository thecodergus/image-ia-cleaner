import sys
import os
from PIL import Image


def copiar_somente_pixels(caminho_imagem):
    try:
        # Verifique se o arquivo existe
        if not os.path.isfile(caminho_imagem):
            print(f"Erro: O arquivo '{caminho_imagem}' não existe.")
            return

        # Abrir a imagem original
        imagem_original = Image.open(caminho_imagem)

        # Forçar conversão para RGB para descartar canais ou dados extras
        imagem_pixels = imagem_original.convert("RGB")

        # Criar uma nova imagem estritamente com os dados de pixels
        nova_imagem = Image.new("RGB", imagem_pixels.size)
        nova_imagem.putdata(list(imagem_pixels.getdata()))

        # Gerar o novo nome de arquivo com _cleaned e extensão .jpg
        diretorio, nome_arquivo = os.path.split(caminho_imagem)
        nome_base, _ = os.path.splitext(nome_arquivo)
        novo_nome = f"{nome_base}_cleaned.jpg"
        caminho_novo = os.path.join(diretorio, novo_nome)

        # Salvar a imagem nova em formato JPEG
        nova_imagem.save(caminho_novo, format="JPEG")

        print(f"Nova imagem limpa criada e salva como: {caminho_novo}")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")


if __name__ == "__main__":
    # Esperar que o caminho da imagem seja passado como argumento ao script
    if len(sys.argv) != 2:
        print("Uso: python script.py <caminho_da_imagem>")
    else:
        caminho_imagem = sys.argv[1]
        copiar_somente_pixels(caminho_imagem)
