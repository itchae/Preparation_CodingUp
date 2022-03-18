import re


def e_search_1():
    txt = "The rain in Spain"
    x = re.search("^The.*Spain$", txt)
    if x:
        print("YES! We have a match!")
    else:
        print("No match")


def e_search_2():
    txt = "The rain in Spain"
    x = re.search("\s", txt)

    print("The first white-space character is located in position:", x.start())


def e_search_3():
    txt = "The rain in Spain"
    x = re.search("Portugal", txt)
    print(x)


def e_findall_1():
    txt = "The rain in Spain"
    x = re.findall("ai", txt)
    print(x)


def e_findall_2():
    txt = "The rain in Spain"
    x = re.findall("Portugal", txt)
    print(x)


def e_split_1():
    txt = "The rain in Spain"
    x = re.split("\s", txt)
    print(x)


def e_split_2():
    txt = "The rain in Spain"
    x = re.split("\s", txt, 1)
    print(x)

def e_sub_1():
    txt = "The rain in Spain"
    x = re.sub("\s", "9", txt)
    print(x)

