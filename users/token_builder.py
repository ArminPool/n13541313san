import random
import string
from django.utils.timezone import localtime, now


class GetToken:
    token_list = []
    expire_time = 60
    createdtime = 0

    def __init__(self):
        self.createdtime = localtime(now())
        a = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
        self.token_list.append(a)

    def get_token(self):
        refrencedtime = localtime(now())
        if refrencedtime.parse_to_sec - self.createdtime.parse_to_sec < self.createdtime.expire_time:
            return self.token_list[0]
        else:
            return None

    def parse_to_sec(self, time):
        return time.hour * 3600 + time.minute * 60 + time.second
