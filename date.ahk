; need to add support for:
; 1-Jun-1990 
; November 15th, 2002
; July 1st, 2008
; 23 March 09
; Jul 04, 2005

#Persistent
return

OnClipboardChange:
; work
;RunWait, python date.py "MM/DD/YYYY" "%clipboard%",,Hide UseErrorLevel
; home
RunWait, python date.py "YYYYMMDD" "%clipboard%",,Hide UseErrorLevel
if(%ErrorLevel% = 0)
{
;    MsgBox %ErrorLevel%
    FileRead, output, date
    ToolTip %clipboard%->%output%
    clipboard = %output%
    Sleep 1000
    ToolTip  ; Turn off the tip.
}

return