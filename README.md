# Estimativa de Horários por Ponto de Apoio - MTB

Este projeto foi criado para ajudar organizadores e participantes de provas de mountain bike a estimar os horários de passagem em pontos de apoio (PAs), com base na distância e em diferentes velocidades médias.

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)

## Acesse o app online:

Acesse o app publicado no Streamlit Cloud:  
[https://projeto-horarios-ciclismo-3uddtrfm4mt9lbeqplkzek.streamlit.app](https://projeto-horarios-ciclismo-3uddtrfm4mt9lbeqplkzek.streamlit.app)

---

## Funcionalidades

- Entrada da **distância dos pontos de apoio** (em km).
- Entrada de diferentes **velocidades médias estimadas** (em km/h).
- Cálculo automático do **horário estimado de passagem** por cada ponto.
- Interface amigável e responsiva usando Streamlit.

---

## Exemplo de uso

- Largada: 08:00
- Distâncias dos PAs: `10, 17, 23, 36, 49, 54`
- Velocidades médias: `21, 25, 29`

Resultado:

| Ponto     | Distância (km) | 21 km/h | 25 km/h | 29 km/h |
|-----------|----------------|---------|---------|---------|
| Largada   | 0              | 08:00   | 08:00   | 08:00   |
| PA1       | 10             | 08:28   | 08:24   | 08:21   |
| ...       | ...            | ...     | ...     | ...     |

---

## Tecnologias utilizadas

- [Python 3.10](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

---

## Como rodar localmente

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto-horarios-ciclismo.git

cd projeto-horarios-ciclismo

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

streamlit run app.py

 Deploy com Streamlit Cloud
Faça login no Streamlit Cloud.

Conecte seu repositório do GitHub.

Escolha o arquivo app.py como script principal.

Aguarde a publicação e acesse o link gerado!

---
Ideias futuras
 - Permitir salvar/exportar os horários como PDF ou Excel

 - Estimativas com base em altimetria (elevação acumulada)

 - Personalização de pontos de apoio com nomes e horários limites

---

Contato
Desenvolvido por Gustavo Savi
[Linkedin](www.linkedin.com/in/gustavo-savi)
