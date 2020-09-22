# %%
class Singleton:

    obj = None

    def __init__(self):
        """ Constructor
        """
        if Singleton.obj is None:
            Singleton.obj = self
        else:
            raise Exception("You cannot create another Singleton object")

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance
        """
        if not Singleton.obj:
            Singleton()
        return Singleton.obj

obj = Singleton()
same_obj = Singleton.get_instance()
print(obj, same_obj)
# (<__main__.Singleton instance at 0x10dd143f8>, <__main__.Singleton instance at 0x10dd143f8>)
another_obj = Singleton() # this will error out
print(another_obj)
"""
Traceback (most recent call last):
  File "singleton.py", line 24, in <module>
    another_obj = Singleton() # this will error out
  File "singleton.py", line 11, in __init__
    raise Exception("You cannot create another Singleton object")
Exception: You cannot create another Singleton object
"""


# %%
