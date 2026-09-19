@echo off
title Multi-Account Selfbot Manager
:menu
cls
echo ====================================================
echo        DISCORD MULTI-ACCOUNT SELFBOT MANAGER
echo ====================================================
echo 1. Launch Account 1 [GAMER Persona]
echo 2. Launch Account 2 [MUSIC Persona]
echo 3. Launch Account 3 [GAMER Persona]
echo 4. Launch Account 4 [MUSIC Persona]
echo 5. Reset/Clear All Stored User Tokens
echo 6. Exit
echo ====================================================
set /p choice="Select an option (1-6): "

if "%choice%"=="1" (
    echo Starting Account 1 (Gamer)...
    python selfbot.py gamer acc1
    pause
    goto menu
)
if "%choice%"=="2" (
    echo Starting Account 2 (Music)...
    python selfbot.py music acc2
    pause
    goto menu
)
if "%choice%"=="3" (
    echo Starting Account 3 (Gamer)...
    python selfbot.py gamer acc3
    pause
    goto menu
)
if "%choice%"=="4" (
    echo Starting Account 4 (Music)...
    python selfbot.py music acc4
    pause
    goto menu
)
if "%choice%"=="5" (
    if exist config.json del config.json
    echo [!] All saved tokens cleared.
    pause
    goto menu
)
if "%choice%"=="6" exit
