code = """
def bar(x):
    for i in x:
        print(i)
"""
ldict = {}
exec(code, ldict, ldict)
testcode = """
def test1():
    bar([5,2])
test1()
"""
try:
    exec(testcode, ldict, ldict)
    print(ldict)
except:
    print("assertion error")