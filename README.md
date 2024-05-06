# Redimencionador de imagens
Este projeto foi feito em python com a biblioteca Pillow para a maipilação de imagens
ele utiliza uma função recursiva aninhada para escalar uma imagem. dividindo-a em quadrantes menores e, em seguida, escalando cada quadrante separadamente.

# Detalhando o projeto

A função 'escalar_imagem' recebe uma imagem e um fator de escala 
  - pega os valores de largura e altura da imagem original 'imagem. size'
  - cria uma imagem vazia (preenchida com pixels pretos por padrão) com as dimenções escalonadas 'Image.new("RGB", (nova_largura, nova_altura))'
  
A função 'escalar_quadrante' recebe como parametros as coordenadas e dimenções do quadrante inicial (que é a imagem toda)
  - O caso base da recurção se dá quando a largura e altura do quadrante for menor ou igual a zero
      - pega pixel da imagem original

