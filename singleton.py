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


# Override new method
from datetime import datetime

class XYZ:
    ins = None
    
    def __new__(cls):
        print("Creating Instance")
        if not XYZ.ins:
            XYZ.ins = super(XYZ, cls).__new__(cls)
        return XYZ.ins
    
    def __init__(self, *args, **kwargs):
        self.time = datetime.now()

a = XYZ()
print(a.time)

b = XYZ()
print(b.time)

print(a == b)

# Singlton Class 
class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

s1 = Singleton.get_instance()
s2 = Singleton.get_instance()
print(s1 is s2)  # Output: True

s3 = Singleton() # This will raise an error
