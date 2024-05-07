from PIL import Image

def escalar_imagem (imagem, escala):  
    largura, altura = imagem. size
    nova_largura = int(largura * escala)
    nova_altura = int(altura * escala)
    nova_imagem = Image.new("RGB", (nova_largura, nova_altura)) 
    
    def escalar_quadrante(x, y, w, h) : #coordenadas, largura e altura do quadrante
        if w <= 1 or h <= 1 : 
            cor = imagem.getpixel((x,y)) 
            nova_imagem.putpixel((int(x * escala), int(y * escala)), cor) 
        else:
            pt_medio_x = x +  w // 2
            pt_medio_y = y + h //2

            escalar_quadrante(x, y, pt_medio_x - x, pt_medio_y - y)
            escalar_quadrante(pt_medio_x, y, x + w - pt_medio_x, pt_medio_y - y)
            escalar_quadrante(x, pt_medio_y, pt_medio_x - x, y + h - pt_medio_y)
            escalar_quadrante(pt_medio_x, pt_medio_y, x + w -pt_medio_x, y + h - pt_medio_y)

   
    escalar_quadrante(0, 0, largura, altura)
    return nova_imagem

imagem = Image.open(".\leao_cinza.jpg")
nova_imagem = escalar_imagem(imagem, 0.25)
nova_imagem.show()