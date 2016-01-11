import re
import wget

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):

        if (len(attrs) == 0):
            return

        self.getLinks(attrs)

    def getLinks(self, attrs):

        for attr in attrs:

            if (attr[1] is None):
                break

            if (re.compile('http').search(attr[1])):
                self.checkExtension(attr[1])

    def checkExtension(self, url):

        # jpg jpeg png bmp に一致するURLのみ処理を行うようにする
        if (re.compile(r'(jpg|jpeg|png|bmp)$').search(url)):
            print(url)
            self.download(url)

    def download(self, url):

        # wgetで取得特定のディレクトリ以下に保存する
        filename = wget.download(url,'./pictures/')

    def collectLink(self, url):
        print('collect => ')
        print(url)
        print('collect <= ')
