class Error(Exception):
    pass

class AreaOutOfSpaceError(Error):
    def __init__(self, area):
        self.area = area

class TaskDoesNotExistError(Error):
    def __init__(self, num):
        self.num = num

class AreaDoesNotExistError(Error):
    def __init__(self, area):
        self.area = area