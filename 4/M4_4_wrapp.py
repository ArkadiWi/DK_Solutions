# wrapp getting 2 args
def cut(start: int, stop: int):
   def wrapper (function):
       def inner_wrapper(*args, **kwargs):
           return function(*args,**kwargs)[start:stop]
       return inner_wrapper
   return wrapper

@ cut(1,9)
def cut_some_string(string):
    if type(string) == int or type(string) == float:
        string = str(string)
    return string

def test_cut_list():
    @cut(1,5)
    def sample():
        return [1,2,3,4,5,6,7,8,9]

    assert sample() == [2,3,4,5]



print(cut_some_string('abecadło'))
print(cut_some_string(12548796))
print(cut_some_string([1,2,5,4,8,7,9,6]))
print(cut_some_string(['ade','bgr','dree','ddddddd']))
print(cut_some_string(1254.8796))
print(cut_some_string(''))