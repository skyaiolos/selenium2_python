; ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("Open","","Edit1")

; Wait 10 seconds for the Upload window to appear
WinWait("[CLASS:#32770]","",10)

; Set the File name text on the Edit field
ControlSetText("Open","","Edit1","D:\TestUpfile.txt")
Sleep(2000)

; Click on the open button
ControlClick("Open","","Button1");