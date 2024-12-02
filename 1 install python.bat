cd %~dp0
@echo off
python-3.11.8-amd64.exe /quiet PrependPath=1 Include_test=0

echo Python 3.11.8 has been installed for the current user and added to PATH.
pause
