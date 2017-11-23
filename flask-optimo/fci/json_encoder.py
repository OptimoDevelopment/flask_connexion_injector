import datetime

from flask.json import JSONEncoder


class CustomJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            serial = obj.isoformat()
            return serial

        #  Add more types for yours project

        return JSONEncoder.default(self, obj)
