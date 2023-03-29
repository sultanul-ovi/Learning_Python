spam = 42 #global variable

def hello():
    global spam
    spam = 32 # local variable
    spam = spam + 1
    print(spam)


hello()
print(spam)

