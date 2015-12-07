from MyHTMLParser import MyHTMLParser
from MyCurl       import MyCurl
from MyBuffer     import MyBuffer
from MyBody       import MyBody
import sys



curl = MyCurl()
curl.set_url(sys.argv[1])

buffer = MyBuffer()
curl = buffer.set_write_setting(curl)

curl.exec()
curl.close()

body = MyBody

body = buffer.get_value(body)


parser = MyHTMLParser() 
parser.feed(body)

