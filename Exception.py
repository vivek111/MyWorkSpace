a=10
b=9
try:
    a/b
except Exception as e:
    print(e)
else:
    print('It gets executed if exception is not raised')
finally:
    print('By default it gets executded')
print(__name__)
