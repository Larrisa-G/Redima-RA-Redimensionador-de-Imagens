from PIL import Image

def escalar_imagem (imagem, escala):  
    largura, altura = imagem. size
    nova_largura = int(largura * escala)
    nova_altura = int(altura * escala)
    nova_imagem = Image.new("RGB", (nova_largura, nova_altura)) # cria imagem vazia preenchida com pixels pretos por padrão
    
    def escalar_quadrante(x, y, w, h)
        if w <= 1 or h <= 1 : #largura e altura do quadrante
            cor = imagem.getpixel((x,y)) #pega pixel da imagem original
            nova_imagem.putpixel((int(x * escala), (y * escala))) # altera pixel da nova imagem
        else:
            pt_medio_x = x +  w // 2 #calcula as coordenadas do ponto médio do quadrante
            pt_medio_y = y + h //2
            #divide o quadrante em paartes menores (repartindo de 4 em 4) até que atinjam o caso base (quadrantes de um único pixel).
            escalar_quadrante(x, y, pt_medio_x - x, pt_medio_y - y)
            escalar_quadrante(pt_medio_x, y, x + w - pt_medio_x, pt_medio_y - y)
            escalar_quadrante(x, pt_medio_y, pt_medio_x - x, y + h - pt_medio_y)
            escalar_quadrante(pt_medio_x, pt_medio_y, x + w -pt_medio_x, y + h - pt_medio_y)


imagem = Image.open(".\pepinof.png")
escalar_imagem(imagem, 2.0)
imagem.show()