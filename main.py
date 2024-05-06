from PIL import Image

def escalar_imagem (imagem, escala):  
    largura, altura = imagem. size
    nova_largura = int(largura * escala)
    nova_altura = int(altura * escala)
    nova_imagem = Image.new("RGB", (nova_largura, nova_altura)) # cria imagem vazia preenchida com pixels pretos por padrão
    
    def escalar_quadrante(x, y, width, height)
        if w <= 1 or h <= 1 :
            cor = imagem.getpixel((x,y)) #pega pixel da imagem original
            nova_imagem.putpixel((int(x * escala), (y * escala))) # altera pixel da nova imagem




imagem = Image.open(".\pepinof.png")
escalar_imagem(imagem, 2.0)
imagem.show()