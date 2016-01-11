from MyHTMLParser import MyHTMLParser
from MyCurl       import MyCurl
from MyBody       import MyBody
from io           import BytesIO
from MyUriEncode  import MyUriEncode
import urllib.parse

class Facade:

    def __new__(cls):
        return cls

    def downloadPictures():

        curl = MyCurl()
        curl.set_url(MyUriEncode.getUrl())
        
        buffer = BytesIO()
        buffer = curl.set_buffer(buffer)
        
        curl.exec()
        curl.close()
        
        body = buffer.getvalue().decode('utf-8')
        
        parser = MyHTMLParser() 
        parser.feed(body)
