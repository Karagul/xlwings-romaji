import xlwings as xw
from pykakasi import kakasi as k

def hello_xlwings():
    wb = xw.Book.caller()
    wb.sheets[0].range("A1").value = "Hello xlwings!"


@xw.func
def hello(name):
    return "hello {0}".format(name)


@xw.func
def to_romaji(name):
    if not name:
        return ''

    kakasi = k()
    kakasi.setMode("H","a")
    kakasi.setMode("r","Passport")

    conv = kakasi.getConverter()
    return conv.do(name)