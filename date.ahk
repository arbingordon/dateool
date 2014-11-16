;Run this file, edit RunWait line as desired
;for your formatting preferences


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