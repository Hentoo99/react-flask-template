# === FASE 1 - Build frontend React ===
FROM node:20 AS frontend-build

WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# === FASE 2 - Backend Flask ===
FROM python:3.11-slim AS backend

WORKDIR /app

# Install Python dependencies
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copia tutto il backend
COPY backend/ ./backend/

# Copia i file statici React buildati
COPY --from=frontend-build /app/frontend/build ./backend/static

# Imposta variabili d'ambiente Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Espone la porta Flask
EXPOSE 5000

# Avvia Flask
CMD ["flask", "run"]