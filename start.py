# start.py

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


#python -m venv venv
#venv\Scripts\activate
# Instalar dependencias
#pip install -r requirements.txt
# ⚠️ Esto borra el entorno virtual actual
#rmdir /s /q venv