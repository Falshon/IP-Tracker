@echo off
REM Vérifiez si Python est installé
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python n'est pas installé. Veuillez installer Python avant de continuer.
    pause
    exit /b
)

REM Installe les bibliothèques à partir du fichier requirements.txt
echo Installation des bibliothèques Python...
pip install colorama
pip install requests
pip install pystyle
pip install beautifulsoup4
pip install phonenumbers
pip install selenium

echo Installation terminée.
pause
