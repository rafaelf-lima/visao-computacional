# Visão Computacional - Ibmec (2025.1)

Repositório dedicado ao projeto de Visão Computacional.

Grupo: Rafael Lima, Bernardo Loureiro, Luis Pastura, Daniel Gripa, João Araujo e Lucca Lanzellotti.

## Customizações Realizadas - AP2 (Navigation of UAVs in GPS-Denied Environments Using Computer Vision with Transformers)

Durante o desenvolvimento deste projeto de graduação, o grupo realizou diversas customizações no código-base e na configuração do modelo para atender às necessidades específicas da ideia-base do projeto para a AP2. Desse modo, abaixo as customizações realizadas (#3):

### 1. Integração do DINOv2 com uma Interface Web Interativa
- Desenvolvemos uma interface web utilizando o framework **Streamlit**, permitindo o envio, visualização e comparação de imagens de satélite de forma prática e acessível.
- Implementamos uma interface de usuário que exibe as imagens carregadas lado a lado, além de exibir o resultado da similaridade calculada entre elas.

### 2. Pré-processamento de Imagens
- Incluímos uma função de redimensionamento automático das imagens para 224×224 pixels, garantindo compatibilidade com o pipeline de pré-processamento do DINOv2 e padronizando a entrada de dados.

### 3. Pipeline de Similaridade Visual
- Implementamos uma rotina de rotação para lidar com imagens capturadas em diferentes orientações, considerando rotações de 0° e 180°, conforme descrito no paper.
- Adaptamos o cálculo de similaridade usando a métrica de cosseno entre os embeddings gerados pelo modelo, selecionando automaticamente a maior similaridade e o melhor ângulo de rotação encontrado.

### 4. Critério de Decisão
- Definimos um limiar de similaridade (0.87) com base em experimentação, para classificar as imagens como sendo do mesmo local ou não.
- Esse valor foi ajustado considerando o desempenho do modelo nos testes preliminares realizados.

### 5. Uso do Modelo Pré-treinado com Ajustes
- Utilizamos o modelo DINOv2 pré-treinado como base e configuramos o pipeline para uso local, garantindo que o sistema funcione mesmo em ambientes onde a conexão com a internet seja limitada.
- Implementamos cache para otimizar o tempo de carregamento e reduzir a dependência de rede.

### 6. Documentação e Explicação Didática
- Toda a lógica do projeto foi documentada de forma clara no paper para facilitar o entendimento, incluindo a apresentação do pipeline de similaridade e as etapas realizadas no relatório técnico e na apresentação em PowerPoint.
- Buscamos manter a explicação das etapas de processamento alinhada ao objetivo da AP2 e à motivação prática do projeto.
