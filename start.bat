@echo off
ECHO Iniciando microsservicos...

:: Pega o caminho da pasta atual onde o start.bat esta
SET BASE_DIR=%~dp0

:: Tenta encontrar o Python automaticamente
SET PYTHON_EXE=

:: Tenta usar 'python' do PATH primeiro
python --version >nul 2>&1
if %errorlevel% == 0 (
    SET PYTHON_EXE=python
    goto :python_found
)

:: Tenta usar 'py' launcher
py --version >nul 2>&1
if %errorlevel% == 0 (
    SET PYTHON_EXE=py
    goto :python_found
)

:: Tenta caminhos comuns do Python no Windows
if exist "C:\Python313\python.exe" (
    SET PYTHON_EXE=C:\Python313\python.exe
    goto :python_found
)
if exist "C:\Python312\python.exe" (
    SET PYTHON_EXE=C:\Python312\python.exe
    goto :python_found
)
if exist "C:\Python311\python.exe" (
    SET PYTHON_EXE=C:\Python311\python.exe
    goto :python_found
)
if exist "C:\Python310\python.exe" (
    SET PYTHON_EXE=C:\Python310\python.exe
    goto :python_found
)
if exist "C:\Python39\python.exe" (
    SET PYTHON_EXE=C:\Python39\python.exe
    goto :python_found
)
if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
    SET PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python313\python.exe
    goto :python_found
)
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    SET PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python312\python.exe
    goto :python_found
)
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    SET PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python311\python.exe
    goto :python_found
)
if exist "%ProgramFiles%\Python313\python.exe" (
    SET PYTHON_EXE=%ProgramFiles%\Python313\python.exe
    goto :python_found
)
if exist "%ProgramFiles%\Python312\python.exe" (
    SET PYTHON_EXE=%ProgramFiles%\Python312\python.exe
    goto :python_found
)

:: Se nao encontrou, mostra erro
ECHO.
ECHO ========================================
ECHO ERRO: Python nao encontrado!
ECHO ========================================
ECHO.
ECHO Tente uma das seguintes opcoes:
ECHO 1. Instale o Python e adicione ao PATH do Windows
ECHO 2. Adicione manualmente o caminho do Python no inicio deste arquivo
ECHO 3. Use o Python Launcher (py -3) se instalado
ECHO.
ECHO Para definir manualmente, adicione esta linha apos a linha 5:
ECHO SET PYTHON_EXE=C:\caminho\para\seu\python.exe
ECHO.
pause
exit /b

:python_found
ECHO Python encontrado: %PYTHON_EXE%
ECHO.

:: Inicia o Servico de Citacoes (Porta 5001)
ECHO Iniciando Servico Citacoes...
start "Servico Citacoes (5001)" cmd /k "%PYTHON_EXE% %BASE_DIR%servico_citacoes\app.py"

:: Inicia o Servico Diario (Porta 5000)
ECHO Iniciando Servico Diario...
start "Servico Diario (5000)" cmd /k "%PYTHON_EXE% %BASE_DIR%servico_diario\app.py"

ECHO Prontinho! Os dois servicos estao sendo iniciados em janelas separadas.