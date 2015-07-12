import re
import pycurl
from io import BytesIO

c = pycurl.Curl()
c.setopt(c.URL, "http://www.yahoo.co.jp")
buffer = BytesIO()
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue().decode('utf-8')
# print(body)
match = re.search('https(.*)', body)
print(match)
