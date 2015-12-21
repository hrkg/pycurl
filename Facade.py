from MyHTMLParser import MyHTMLParser
from MyCurl       import MyCurl
from MyBody       import MyBody
from io           import BytesIO
import sys

class Facade:

    def __new__(cls):
        return cls

    def downloadPictures():
        curl = MyCurl()
        curl.set_url(sys.argv[1])
        
        buffer = BytesIO()
        buffer = curl.set_buffer(buffer)
        
        curl.exec()
        curl.close()
        
        body = buffer.getvalue().decode('utf-8')
        
        parser = MyHTMLParser() 
        parser.feed(body)
