def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance

@singleton
class AppCreator:
    def __init__(self):
        pass

obj1 = AppCreator()

try:
  obj2 = AppCreator()
except Exception as error:
  print(error)
