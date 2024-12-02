cd %~dp0
@echo off
setlocal enabledelayedexpansion

echo Upgrading pip to the latest version, please wait...
python -m pip install --upgrade pip >NUL 2>&1
echo Pip has been upgraded.

echo Installing required Python packages...
set /a "count=0"
set /a "total=10"
set "packages=numpy opencv-python pywin32 mss hidapi requests pyqt5 Pillow termcolor keyboard pyfiglet PyAutoGUI pycryptodome regex"

for %%p in (%packages%) do (
    set /a "count+=1"
    set /a "percent=(count*100)/total"
    echo Installing %%p, progress: !percent!%%
    python -m pip install %%p >NUL 2>&1
)

echo All required Python packages have been installed.

pause
