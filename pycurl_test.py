import re
import pycurl
import wget

from io import BytesIO
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):

        if (len(attrs) == 0):
            return
        for attr in attrs:
            if (attr[1] is None):
                break
            if (re.compile('http').search(attr[1])):
                # jpg jpeg png bmp に一致するURLのみ処理を行うようにする
                if (re.compile(r'(jpg|jpeg|png|bmp)$').search(attr[1])):
                    print(attr[1])
                    # wgetで取得特定のディレクトリ以下に保存する
                    url = attr[1]
                    filename = wget.download(url,'./pictures/')

    def return_dictionary(self):
        return self.dictionary
    

c = pycurl.Curl()
c.setopt(c.URL, "http://www.yahoo.co.jp")

buffer = BytesIO()
c.setopt(c.WRITEDATA, buffer)

c.perform()
c.close()

body = buffer.getvalue().decode('utf-8')

parser = MyHTMLParser() 
parser.feed(body)
