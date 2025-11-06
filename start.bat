@echo off
ECHO Iniciando microsservicos...

:: ATENCAO: Verifique se este eh o caminho certo para seu Python
SET PYTHON_EXE=C:\Python313\python.exe

:: Pega o caminho da pasta atual onde o start.bat esta
SET BASE_DIR=%~dp0

:: Verifica se o Python existe
if not exist "%PYTHON_EXE%" (
    ECHO ERRO: Python nao encontrado em %PYTHON_EXE%
    ECHO Por favor, edite o start.bat e corrija o caminho na linha 5.
    pause
    exit /b
)

:: Inicia o Servico de Citacoes (Porta 5001)
ECHO Iniciando Servico Citacoes...
start "Servico Citacoes (5001)" cmd /k "%PYTHON_EXE% %BASE_DIR%servico_citacoes\app.py"

:: Inicia o Servico Diario (Porta 5000)
ECHO Iniciando Servico Diario...
start "Servico Diario (5000)" cmd /k "%PYTHON_EXE% %BASE_DIR%servico_diario\app.py"

ECHO Prontinho! Os dois servicos estao sendo iniciados em janelas separadas.