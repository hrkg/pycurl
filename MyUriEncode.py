import urllib.parse
import sys

class MyUriEncode:

    @staticmethod
    def getUrl():
    
        f = lambda query : urllib.parse.quote_plus(query, 'utf-8')

        first_part = 'http://***'
        last_part  = '***'

        url = lambda encoded_query : first_part + encoded_query + last_part

        return url(f(sys.argv[1]))
