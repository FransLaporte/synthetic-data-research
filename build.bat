@echo off
setlocal
pushd "%~dp0"
if errorlevel 1 exit /b 1
where xelatex >nul 2>nul
if errorlevel 1 goto missing
where biber >nul 2>nul
if errorlevel 1 goto missing

xelatex -interaction=nonstopmode -halt-on-error main.tex
if errorlevel 1 goto failed
biber main
if errorlevel 1 goto failed
xelatex -interaction=nonstopmode -halt-on-error main.tex
if errorlevel 1 goto failed
xelatex -interaction=nonstopmode -halt-on-error main.tex
if errorlevel 1 goto failed
echo.
echo Build complete: %CD%\main.pdf
popd
exit /b 0

:missing
echo ERROR: XeLaTeX and Biber must be on PATH. Install MiKTeX or TeX Live.
goto failed

:failed
echo ERROR: Build failed. Check the output above and main.log or main.blg.
popd
exit /b 1
