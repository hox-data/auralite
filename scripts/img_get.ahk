#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance Force


Loop 
{
	Run, https://www.bet365.com/#/AVR/B24/R^1/
	Sleep, 3000
	Send {F12}
	Send {F5}
	Sleep, 3000
	Send, ^+p
	Sleep, 576
	SendRaw, capture screenshot
	Sleep, 380
	Send, {Enter}
	Sleep, 1200
	Send, ^w
}

esc::exitapp
return
