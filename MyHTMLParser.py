import re
import wget

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        return attrs;


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
