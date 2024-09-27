def introspection_info(obj):
  info = {}
  info['type'] = type(obj).__name__
  info['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__')]
  info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
  info['module'] = obj.__module__ if hasattr(obj, '__module__') else 'None'
  if isinstance(obj, type):
    info['bases'] = obj.__bases__
    info['docstring'] = obj.__doc__
  elif isinstance(obj, list):
    info['length'] = len(obj)
  elif isinstance(obj, dict):
    info['length'] = len(obj)
    info['keys'] = list(obj.keys())
  elif isinstance(obj, str):
    info['length'] = len(obj)
    info['lower'] = obj.lower()
    info['upper'] = obj.upper()
  else:
    info['repr'] = repr(obj)
  return info
class MyClass:
  def __init__(self, value):
    self.value = value
  def my_method(self):
    return f"Метод класса: {self.value}"
my_object = MyClass(10)
object_info = introspection_info(my_object)
print(object_info)
number_info = introspection_info(42)
print(number_info)
