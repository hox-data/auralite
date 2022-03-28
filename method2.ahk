#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


countFileResults := 0
countFileOdds := 0

Loop, 
{
    Loop, 19
    {
        Run, https://www.bet365.com/#/AVR/B24/R^1/
        Sleep, 1200
        WinMaximize, A
        Sleep, 3800
        Loop, 56
        {
            Sleep, 60
            Send, {Tab}
            Sleep, 140
        }
        Sleep, 350
        Send, {Enter}
        Sleep, 380
        Send {F12}
        Sleep, 1220
        Send ^c
        Sleep, 1500
        FileAppend, %clipboard%, %A_ScriptDir%\pages\results\results%countFileResults%.html
        countFileResults ++
        Sleep, 2500
        Send, ^w
        Sleep, 2000
        Run, https://www.bet365.com/#/AVR/B24/R^1/
        WinMaximize, A
        Sleep, 3000
        Send {F12}
        Sleep, 1100
        Send ^c
        Sleep, 3000
        FileAppend, %clipboard%, %A_ScriptDir%\pages\odds\odds%countFileOdds%.html
        countFileOdds ++
        Sleep, 2500
        Send, ^w
        Sleep, 146750

    }

    Run, https://www.bet365.com/#/AVR/B24/R^1/
    Sleep, 1200
    WinMaximize, A
    Sleep, 3800
    Loop, 56
    {
        Sleep, 60
        Send, {Tab}
        Sleep, 140
    }
    Sleep, 350
    Send, {Enter}
    Sleep, 380
    Send {F12}
    Sleep, 1220
    Send ^c
    Sleep, 1500
    FileAppend, %clipboard%, %A_ScriptDir%\pages\results\results%countFileResults%.html
    countFileResults ++
    Sleep, 2500
    Send, ^w
    Sleep, 2000
    Run, https://www.bet365.com/#/AVR/B24/R^1/
    WinMaximize, A
    Sleep, 3000
    Send {F12}
    Sleep, 1100
    Send ^c
    Sleep, 3000
    FileAppend, %clipboard%, %A_ScriptDir%\pages\odds\odds%countFileOdds%.html
    countFileOdds ++
    Sleep, 2500
    Send, ^w
    Sleep, 140750

}

esc::exitapp
;Total time active 33750
;Time for each run 180500
;Total idle time span 146750