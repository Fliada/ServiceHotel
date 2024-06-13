from sqlalchemy.ext.declarative import declarative_base

class BaseObj(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BaseObj, cls).__new__(cls)
        return cls.instance