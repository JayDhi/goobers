import requests
import re

url_file = open('url', 'r+')
file = open('result.md', 'a+')
urls = url_file.readlines()
excurl = []
ef = open('exc.md', 'a+')
for i in range(0, len(urls)):
    urls[i] = urls[i].strip()
for url in urls:
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/51.0.2704.63 Safari/537.36'}
        r = requests.get(url, headers = headers, timeout = 10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.content.decode('utf-8')
        title=re.findall('<title>(.+)</title>',html)
        print(title)
        result = '- [ ] '+ str(title) + '(' + str(url) + ')'
        file.write(result+'\n')
    except:
        ef.write(url)
        ef.write('\n')

ef.close()
file.close()
