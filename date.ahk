;Run this file, edit RunWait line as desired
;for your formatting preferences


#Persistent
return

OnClipboardChange:
; work
;RunWait, python date.py "MM/DD/YYYY" "%clipboard%",,Hide UseErrorLevel
; home
RunWait, python date.py "YYYYMMDD" "%clipboard%",,Hide UseErrorLevel

return