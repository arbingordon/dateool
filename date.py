from sys import argv as argv
from sys import exit as exit
from time import sleep as sleep
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
fixes = ["st", "nd", "rd", "th",
       "\n", "\r", "\t", ",",]

fmt = argv[1]
t = " ".join(argv[2:])
t = t.strip()
print(t)
for i in range(len(months)):
    t = t.replace(months[i], "M" + str(i+1))
for i in range(len(months)):
    t = t.replace(months[i][:3], "M" + str(i+1))
for fix in fixes:
    t = t.replace(fix,"")
t = t.replace("-"," ")
t = t.split()
if len(t) == 3:
    y = ""
    m = ""
    d = ""
    for e in t:
        if(len(e) == 4):
            y = e
            t.remove(e)
    for e in t:
        if(e.find("M") != -1):
            m = e.replace("M","").zfill(2)
            t.remove(e)
    d = t[0].zfill(2)
    if(y != "" and m != "" and d != ""):
        out = fmt.replace("YYYY",y)
        out = out.replace("MM",m)
        out = out.replace("DD",d)
        out = out.replace("MONTH",months[int(m)])
        out = out.replace("MON",months[int(m)][:3])
        with open("date","w") as f:
            f.write(out)
        if(slp):
            sleep(count)
        exit(0)
    else:
        exit(1)

exit(1)