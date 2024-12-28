# Utiliser une image Python comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requis dans le conteneur
COPY requirements.txt .
COPY main.py .
COPY gui.py .
COPY visualization.py .
COPY frequency_analysis.py .
COPY audio_processing.py .
COPY constants.py .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port par défaut pour GUI (si utilisé avec frameworks spécifiques comme Flask ou Streamlit)
#EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "main.py"]
