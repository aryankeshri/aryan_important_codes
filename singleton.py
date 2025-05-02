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
print(obj1)

try:
  obj2 = AppCreator()
  print(obj2)
except Exception as error:
  print(error)
