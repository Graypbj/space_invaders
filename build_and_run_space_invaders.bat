@echo off
REM 1. Download and install Python 3 if not present
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python not found. Downloading and installing Python...
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe -OutFile python-installer.exe"
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1
    del python-installer.exe
    REM Reload PATH
    set PATH=%PATH%;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\Scripts\
) else (
    echo Python found.
)

REM 2. Upgrade pip, install PyInstaller and pygame
python -m pip install --upgrade pip
python -m pip install pyinstaller pygame

REM 3. Build the executable
python -m PyInstaller --onefile --name "space_invaders" main.py

REM 4. Copy assets (assuming assets folder)
if exist "assets" (
    xcopy assets dist\assets /E /I /Y
)

REM 5. Run the game
cd dist
start space_invaders.exe

echo All done! Your game is ready and running.
pause
