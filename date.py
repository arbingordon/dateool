#date.py
#date.py formatstring clipboard
#example:
#date.py YYYYMMDD "Jan 1st 2013"
#   -> 20130101

from sys import argv as argv
from sys import exit as exit
from time import sleep as sleep
import re
import pyperclip
slp = False
count = 3
months = ["January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December",]
french_months = ["janvier",
                 "février",
                 "mars",
                 "avril",
                 "mai",
                 "juin",
                 "juillet",
                 "août",
                 "septembre",
                 "octobre",
                 "novembre",
                 "décembre",]
fixes = ["st", "nd", "rd", "th",
         "\n", "\r", "\t", ","]

fmt = argv[1]
argstr = " ".join(argv[2:])
t = argstr
t = t.strip()
print("\"" + t + "\"")

for i in range(len(months)):
    if t != t.replace(months[i], "!M!O!N!T!H!" + str(i+1)):
        print(t + " -> " + t.replace(months[i], "!M!O!N!T!H!" + str(i+1)))
        t = t.replace(months[i], "!M!O!N!T!H!" + str(i+1))
    
for i in range(len(months)):
    t = t.replace(months[i][:3], "!M!O!N!T!H!" + str(i+1))
    
for i in range(len(french_months)):
    t = t.replace(french_months[i], "!M!O!N!T!H!" + str(i+1))

# process fixes afterward to not destroy month text info
for fix in fixes:
    t = t.replace(fix,"")
t = t.split()
print(t)
if True:
    y = ""
    m = ""
    d = ""
    for e in t:
        if(len(e) == 4):
            try:
                a = int(e)
                if(a > 0):
                    print(e)
                    y = e
                    t.remove(e)
            except:
                pass

    for e in t:
        if(e.find("!M!O!N!T!H!") != -1):
            print(e)
            m = e.replace("!M!O!N!T!H!","").zfill(2)
            t.remove(e)

    for e in t:
        if(len(e) < 3):
            try:
                a = int(e)
                if(a > 0):
                    print(e)
                    d = e
                    t.remove(e)
            except:
                pass

    for e in t:
  
      patterns = ["(\d\d\d\d).(\d\d).(\d\d)",
                  "(\d\d)/(\d\d)/(\d\d\d\d)",
                  "(\d\d)\-(\d\d)\-(\d\d\d\d)"]
      keys = [[1,2,3],
             [3,1,2],
             [3,1,2]]
      for i in range(len(patterns)):
        pattern = patterns[i]
        key = keys[i]
        found = re.search(pattern,e)
        if found:
          y = found.group(key[0])
          m = found.group(key[1])
          d = found.group(key[2])
  
    if(y != "" and m != "" and d != ""):
        out = fmt.replace("YYYY",y)
        out = out.replace("MM",m)
        out = out.replace("DD",d)
        out = out.replace("MONTH",months[int(m)-1])
        out = out.replace("MON",months[int(m)-1][:3])
        out = out.replace("YY",y[2:])
        pyperclip.copy(out)
        #input()
        exit(0)
    else:
        #with open("date","w") as f:
        #    f.write(argstr.strip("\n\r\t"))
        exit(1)
        #input()
#with open("date","w") as f:
#            f.write(argstr.strip("\n\r\t"))
#exit(0)
exit(1)