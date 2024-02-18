from sympy.logic import SOPform, POSform
from sympy import symbols
from string import ascii_letters
# import csv

# filename = "test.csv"
# fromFile = True

# terms = [  # All the terms that result in a 1
#     #A B C D E
#     [0,0,0,0,1],
#     [0,0,0,1,1],
#     [0,0,1,0,0],
#     [0,0,1,0,1],
#     [0,0,1,1,0],
#     [0,1,0,0,0],
#     [0,1,0,0,1],
#     [0,1,1,0,1],
#     [1,0,0,0,0],
#     [1,0,0,0,1],
#     [1,0,1,0,0],
#     [1,0,1,1,0],
#     [1,0,1,1,1],
#     [1,1,0,0,0],
#     [1,1,0,1,1],
#     [1,1,1,0,0],
#     [1,1,1,0,1],
#     [1,1,1,1,0],
#     [1,1,1,1,1],
# ]


def simplify(terms_out):
    nos = len(terms_out[0])
    if nos <= 26:
        all_symbols = symbols(" ".join( ascii_letters[26:nos + 26] ))
        
        sop = str(SOPform(all_symbols, terms_out))
        pos = str(POSform(all_symbols, terms_out))
        return clean(sop) if len(sop) < len(pos) else clean(pos)

    else: 
        raise RuntimeError("What type of boolean expression is THAT!! The english language does not have enough letters for this type of calculations...")


def clean(ip_str):
    result = ""
    i = 0

    while i < len(ip_str):
        if ip_str[i] == '~':
            result += ip_str[i + 1] + "'"
            i += 2 
        else:
            result += ip_str[i]
            i += 1

    return result.replace(" | ", " + ").replace(" & ", "")



# terms = list(csv.reader(open(filename))) if fromFile else terms
