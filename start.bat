@echo off
:: Ejecuta start.py como administrador

:: Verifica privilegios
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Ejecutando como administrador...
    call venv\Scripts\activate
    python start.py
) else (
    echo Solicitando permisos de administrador...
    powershell -Command "Start-Process cmd -ArgumentList '/c call venv\Scripts\activate ^&^& python start.py' -Verb RunAs"
)
