#!/bin/bash

export PATH=$PATH:/path/to/adb-folder

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <search_query_1> <search_query_2> ... <search_query_N>"
    exit 1
fi

adb shell am start -n com.microsoft.bing/com.microsoft.sapphire.app.main.SapphireMainActivity
sleep 5

for i in "$@"; do

    if [ "$1" == "$i" ]; then
        adb shell input tap 500 600
    else
        adb shell input tap 400 160
    fi
    sleep 5

    adb shell input text "$(echo "$i" | sed 's/ /%s/g')"
    
    adb shell input keyevent 66
    echo "Search query '$i' submitted"
    sleep 5
    
    query_length=${#i}

    adb shell input tap 400 160
    sleep 1
    for ((j=0; j<query_length; j++)); do
        adb shell input keyevent 67  
    done
done
sleep 3
adb shell am force-stop com.microsoft.bing