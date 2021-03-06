import json
import sys
from pprint import pprint

sys.path.append("../")
from common.object import Object


class DumpCite:
    def print(self):
        pprint(vars(self))

    def to_json(self):
        ret = Object()
        for attr, value in self.__dict__.items():
            if value != "":
                setattr(ret, attr, value)

        return json.dumps(ret, default=lambda o: o.__dict__)
