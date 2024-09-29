@echo off
setlocal enabledelayedexpansion

set ADB_PATH=C:\path\to\your\platform-tools
set PATH=%PATH%;%ADB_PATH%

if "%~1"=="" (
    echo Usage: %0 ^<search_query_1^> ^<search_query_2^> ... ^<search_query_N^>
    exit /b 1
)

adb shell am start -n com.microsoft.bing/com.microsoft.sapphire.app.main.SapphireMainActivity
timeout /t 5

set index=0

:loop
if "%~1"=="" goto endloop

set query=%~1
shift

if !index! == 0 (
    adb shell input tap 500 600
) else (
    adb shell input tap 400 160
)

timeout /t 5

rem Replace spaces with '%20'
set query=!query: =%%20!
adb shell input text "!query!"
adb shell input keyevent 66
echo Search query '!query!' submitted
timeout /t 5

rem Delete the query
adb shell input tap 400 160
timeout /t 1

rem Calculate the length of the query
set query_length=0
for /l %%i in (0, 1, 255) do (
    set "char=!query:~%%i,1!"
    if "!char!"=="" goto end_length
    set /a query_length+=1
)
:end_length

rem Simulate backspace for the length of the query
for /l %%j in (1, 1, !query_length!) do (
    adb shell input keyevent 67
)

set /a index+=1
goto loop

:endloop
timeout /t 3
adb shell am force-stop com.microsoft.bing