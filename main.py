from PIL import Image

def escalar_imagem (imagem, escala):  
    largura, altura = imagem. size
    nova_largura = int(largura * escala)
    nova_altura = int(altura * escala)
    nova_imagem = Image.new("RGB", (nova_largura, nova_altura)) # cria imagem vazia preenchida com pixels pretos por padrão
    return nova_imagem

imagem = Image.open(".\pepinof.png")
escalar_imagem(imagem, 2.0)
imagem.show()