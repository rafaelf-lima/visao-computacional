# Importação das bibliotecas necessárias
import cv2                   # OpenCV para processamento de imagem
import numpy as np           # NumPy para manipulação de arrays
import matplotlib.pyplot as plt  # (não usada aqui, mas útil para visualizações em notebooks)

# ------------------------------
# Carregamento da imagem
# ------------------------------
img = cv2.imread("pessoa.jpg")  # Lê a imagem "pessoa.jpg" no formato BGR (padrão da OpenCV)

# ------------------------------
# Redimensionamento da imagem
# ------------------------------
scale_percent = 80  # Reduz a imagem para 80% do tamanho original
width = int(img.shape[1] * scale_percent / 100)  # Novo valor da largura
height = int(img.shape[0] * scale_percent / 100)  # Novo valor da altura
dim = (width, height)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)  # Redimensiona usando interpolação ideal para redução

# ------------------------------
# Conversão para escala de cinza
# ------------------------------
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Converte imagem BGR para tons de cinza

# ------------------------------
# Aplicação do filtro bilateral e detecção de bordas com Canny
# ------------------------------
# O filtro bilateral suaviza a imagem sem perder bordas
bilateral = cv2.bilateralFilter(gray, 9, 75, 75)
# Aplica detector de bordas de Canny com thresholds de 50 e 150
edges_bilateral_canny = cv2.Canny(bilateral, 50, 150)

# ------------------------------
# Conversão de centímetros para pixels (assumindo 96 DPI)
# ------------------------------
pixels_largura_2cm = int(96 * 2 / 2.54)  # ~75.59 pixels → largura máxima permitida para contornos (2 cm)
pixels_altura_2cm = int(96 * 2 / 2.54)   # ~75.59 pixels → altura máxima permitida para contornos (2 cm)
# OBS: Os dois valores são iguais aqui, mas poderiam ser ajustados separadamente se desejado

# ------------------------------
# Encontrar contornos na imagem de bordas
# ------------------------------
contornos, _ = cv2.findContours(edges_bilateral_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# RETR_EXTERNAL → considera apenas os contornos externos
# CHAIN_APPROX_SIMPLE → elimina pontos redundantes para reduzir o uso de memória

# ------------------------------
# Criação de imagem preta (máscara) para desenhar apenas os contornos filtrados
# ------------------------------
mascara = np.zeros_like(edges_bilateral_canny)  # Cria uma imagem do mesmo tamanho, mas só com pixels 0 (preto)

# ------------------------------
# Filtro de contornos por tamanho (descarta contornos maiores que 2 cm)
# ------------------------------
for contorno in contornos:
    x, y, w, h = cv2.boundingRect(contorno)  # Obtém o retângulo delimitador do contorno

    # Mantém apenas contornos cuja largura E altura sejam menores ou iguais a 2 cm
    if w <= pixels_largura_2cm and h <= pixels_altura_2cm:
        cv2.drawContours(mascara, [contorno], -1, 255, thickness=cv2.FILLED)
        # Desenha o contorno na imagem "mascara" preenchido com branco (255)

# ------------------------------
# Exibição da imagem final com os contornos filtrados
# ------------------------------
cv2.imshow("Contornos filtrados (sem horizontais > 2cm e verticais > 2cm)", mascara)
cv2.waitKey(0)           # Espera o usuário pressionar qualquer tecla
cv2.destroyAllWindows()  # Fecha todas as janelas abertas pela OpenCV
