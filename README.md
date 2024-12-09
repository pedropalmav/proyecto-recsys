# Fine tuning LLMs for Conversational Recommender Systems

Nuestra investigación se basa en los siguientes papers:
- [LLM Redial](https://aclanthology.org/2024.findings-acl.529.pdf): dataset de entrenamiento
- [PEARL](https://aclanthology.org/2024.findings-acl.65.pdf): Métricas de evaluación de CRS
- [Aligning Large Language Models for Controllable Recommendations](https://arxiv.org/pdf/2403.05063): RLHF aplicado a CRS

# Estructura del Repositorio
Se encuentran 10 modelos que fueron evaluados. Entre estos, se encuentran los baselines y los modelos con LLM's a los que se les aplicó finetuning o CoT.
La ejecución de todos ellos resulta en la evaluación de los modelos con las métricas que fueron reportadas en el paper.
Los baselines corresponden a los archivos RandomBaseline.ipynb, MostPopularBaseline.ipynb, Llama_baseline.ipynb y Mistral_baseline.ipynb.

Para ejecutar RandomBaseline.ipynb y MostPopularBaseline.ipynb, simplemente se suben a Google Colab y se ejecutan las celdas.
Llama_baseline.ipynb y Mistral_baseline.ipynb (así como el resto de modelos con LLM's) necesitan tener de antemano una cuenta de huggingface con access tokens a los repositorios de Mistral y Llama.
Además, es necesario tener una cuenta de Weights & Bias (wandb.ai) para poder ejecutar los modelos con LLM's.
