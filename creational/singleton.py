"""
The Singleton guarantees that only one object of a particular class is ever created during the lifetime of an application."""


class SingleTon:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SingleTon, cls).__new__(cls)
        return cls._instance # if there was instance it returns that instance again.