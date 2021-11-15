import pickle

class MyClass():
    def __init__(self, param):
        self.param = param

def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
        print("successful")
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

obj = MyClass(10)
save_object(obj)
