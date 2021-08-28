import requests as rq


print("""
_ ___      ____ ____ ____ ___  ___  ____ ____ 
| |__]     | __ |__/ |__| |__] |__] |___ |__/ 
| |    ___ |__] |  \ |  | |__] |__] |___ |  \ 
                                              
Team : Fexa
Code By Meguminz Ras Kitsune😎

user python always work😎

Note: qouta habis tukar proxy/ip:v
""")
inp = input("List OniiChan : ")
list = open(inp,"r").read().split("\n")

for i in list:
        ip = i.replace("http://","").replace("https://","").replace("/","")
        resp = rq.get("https://api.hackertarget.com/reverseiplookup/?q={}".format(ip))
        print(resp.text)
        for x in resp.text:
          open('grabbedOnichan.txt', 'a').write(x)