
# 自定义异常
class RunTimeException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

    def get_error_msg(self):
        return self.value
