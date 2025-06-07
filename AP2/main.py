# app.py

import streamlit as st
from transformers import AutoProcessor, AutoModel
from PIL import Image
import torch
import numpy as np

# Título do app
st.title("🔍 Comparador de Imagens de Satélite com DINOv2 (Preciso e Invariante à Rotação)")

# Carregando modelo DINOv2 com cache
@st.cache_resource
def load_model():
    model = AutoModel.from_pretrained("facebook/dinov2-base")
    processor = AutoProcessor.from_pretrained("facebook/dinov2-base")
    return model, processor

model, processor = load_model()

# Upload de imagens
img1_file = st.file_uploader("📤 Envie a primeira imagem", type=["jpg", "jpeg", "png"])
img2_file = st.file_uploader("📤 Envie a segunda imagem", type=["jpg", "jpeg", "png"])

# Função para redimensionar imagens
def preprocess_image(image, size=(224, 224)):
    return image.resize(size)

# Função para calcular a melhor similaridade com rotações
def compute_best_similarity(image1, image2, processor, model):
    angles = np.arange(0, 360, 180)  # meio em meio grau
    max_similarity = -1
    best_angle = 0

    # Redimensionar
    image1 = preprocess_image(image1)
    image2 = preprocess_image(image2)

    inputs1 = processor(images=image1, return_tensors="pt")
    with torch.no_grad():
        feat1 = model(**inputs1).last_hidden_state.mean(dim=1)
        feat1 = torch.nn.functional.normalize(feat1, p=2, dim=1)

    for angle in angles:
        rotated_image2 = image2.rotate(angle)
        inputs2 = processor(images=rotated_image2, return_tensors="pt")

        with torch.no_grad():
            feat2 = model(**inputs2).last_hidden_state.mean(dim=1)
            feat2 = torch.nn.functional.normalize(feat2, p=2, dim=1)

        similarity = torch.nn.functional.cosine_similarity(feat1, feat2).item()
        if similarity > max_similarity:
            max_similarity = similarity
            best_angle = angle

    return max_similarity, best_angle

# Processamento principal
if img1_file and img2_file:
    image1 = Image.open(img1_file).convert("RGB")
    image2 = Image.open(img2_file).convert("RGB")

    st.image([image1, image2], caption=["Imagem 1", "Imagem 2"], width=300)

    # Calcular melhor similaridade considerando rotações e resize
    similarity, best_rotation = compute_best_similarity(image1, image2, processor, model)

    # Exibe resultado
    st.markdown("### 🔎 Resultado da Similaridade:")
    st.metric(label="Similaridade (Cosseno)", value=f"{similarity:.4f}")
    st.write(f"📐 Melhor rotação da imagem 2: **{best_rotation}°**")

    # Limiar de decisão
    THRESHOLD = 0.87

    if similarity > THRESHOLD:
        st.success("✅ As imagens são semelhantes — provavelmente representam o mesmo local.")
    else:
        st.error("❌ As imagens são diferentes — provavelmente representam locais distintos.")
