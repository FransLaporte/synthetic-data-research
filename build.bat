@echo off
setlocal
set "target=%~1"
if "%target%"=="" set "target=main"
if /i "%target%"=="all" goto all
if /i "%target%"=="main" goto build
if /i "%target%"=="proposal" goto build
if /i "%target%"=="presentation" goto build
echo Usage: build.bat [main^|proposal^|presentation^|all]
exit /b 1

:all
call "%~f0" main
if errorlevel 1 exit /b 1
call "%~f0" proposal
if errorlevel 1 exit /b 1
call "%~f0" presentation
exit /b %errorlevel%

:build
pushd "%~dp0"
if errorlevel 1 exit /b 1
where xelatex >nul 2>nul
if errorlevel 1 goto missing
where biber >nul 2>nul
if errorlevel 1 goto missing

xelatex -interaction=nonstopmode -halt-on-error "%target%.tex"
if errorlevel 1 goto failed
biber "%target%"
if errorlevel 1 goto failed
xelatex -interaction=nonstopmode -halt-on-error "%target%.tex"
if errorlevel 1 goto failed
xelatex -interaction=nonstopmode -halt-on-error "%target%.tex"
if errorlevel 1 goto failed
echo.
echo Build complete: %CD%\%target%.pdf
popd
exit /b 0

:missing
echo ERROR: XeLaTeX and Biber must be on PATH. Install MiKTeX or TeX Live.
goto failed

:failed
echo ERROR: Build failed. Check the output above and %target%.log or %target%.blg.
popd
exit /b 1
