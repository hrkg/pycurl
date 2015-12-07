from io import BytesIO

class MyBuffer:
    buffer = None

    def __new__(cls):
        cls.buffer = BytesIO()
        return cls
 
    def set_write_setting(curl):
        curl.setopt(curl.WRITEDATA, self.buffer)
        return curl

    def get_value(body):
        return MyBuffer.buffer.getvalue().decode('utf-8')
