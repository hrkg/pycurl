import pycurl

class MyCurl:
    curl = None

    def __new__(cls):
        cls.curl = pycurl.Curl()
        return cls

    def set_url(url):
        MyCurl.curl.setopt(MyCurl.curl.URL, url)

    def set_buffer(buffer):
        MyCurl.curl.setopt(MyCurl.curl.WRITEDATA, buffer)
        return buffer

    def exec():
        MyCurl.curl.perform()

    def close():
        MyCurl.curl.close()

    
