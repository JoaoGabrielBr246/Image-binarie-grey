from PIL import Image
import os

path = input("Insira o caminho da imagem: ")

if os.path.isfile(path):  
    img = Image.open(path)
else:
    print("Arquivo não encontrado. Por favor, tente novamente.")
    exit() 

# Função para converter uma imagem em tons de cinza
def to_grayscale(image):
    width, height = image.size
    grayscale_image = Image.new('RGB', (width, height))
    
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))  # Pegando os valores RGB
            # Convertendo para tons de cinza usando a fórmula
            gray_value = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
            grayscale_image.putpixel((x, y), (gray_value, gray_value, gray_value))
    
    return grayscale_image

# Função para converter uma imagem em binária
def to_binary(image, threshold=128):
    width, height = image.size
    binary_image = Image.new('RGB', (width, height))
    
    for y in range(height):
        for x in range(width):
            gray_value = image.getpixel((x, y))[0]  # Pegando o valor de cinza
            # Aplicando o limiar
            if gray_value > threshold:
                binary_image.putpixel((x, y), (255, 255, 255))  # branco
            else:
                binary_image.putpixel((x, y), (0, 0, 0))  # preto
    
    return binary_image

# Carregando a imagem original
original_image = img.convert('RGB')

# Convertendo a imagem colorida para tons de cinza
grayscale_image = to_grayscale(original_image)

# Convertendo a imagem em tons de cinza para imagem binária
binary_image = to_binary(grayscale_image)

# Salvando as imagens como JPG
grayscale_image.save('imagem_grayscale.jpg', 'JPEG')
binary_image.save('imagem_binaria.jpg', 'JPEG')

print("Imagens salvas como 'imagem_grayscale.jpg' e 'imagem_binaria.jpg'.")

# Pergunta se o usuário deseja visualizar as imagens
print("Deseja visualizar as imagens geradas?")
print("1-) SIM\n2-) NÃO")
convert = int(input("Digite sua opção: "))  # Corrigindo a conversão para inteiro

if convert == 1:
    grayscale_image.show()
    binary_image.show()
    img.show()
else:
    print("Programa finalizado!")
