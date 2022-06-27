input0 ={
        "Chennai": "Banglore",
        "Bombay": "Delhi",
        "Goa": "Chennai",
        "Delhi": "Goa"
    }

def city_dic(input0,src):
    dest=input0.get(src)
    if not dest:
        return False
    print(src+'>'+dest)
    city_dic(input0,dest)

def tickets(input0):
    des = input0.values()
    for k,v in input0.items():
        if k not in des:
            city_dic(input0, k)
            return True

tickets(input0)

input1="()}"

def compare(first,sec):
    if first=="(" and sec==")":
        return True
    if first =="{" and sec=="}":
        return True
    if first =="[" and sec == "]":
        return True
    return False

def check_bracket(input1):
    stack=[]
    for x in input1:
        if x =="(" or x=="{" or x=="[":
            stack.append(x)
        elif x==")" or x=="}" or x=="]":
            if len(stack)==0:
                return False
            elem=stack.pop()
            if not compare(elem,x):
                return False
    if len(stack)==0:
        return True
    else:
        return False

