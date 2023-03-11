def string_checking(some_text):
    if type(some_text) == str:
        print('Right')
        # print(some_text + 'abc')
    elif type(some_text) == list:
        print('There is a list')
    else:
        print('Wrong')
s=1
a = '1289'
b = 19
c= []
string_checking(a)
string_checking(b)
string_checking(c)