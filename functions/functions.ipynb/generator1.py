def get_cube(*args):
    for i in args:
        yield i**3


for i in get_cube(1,5,86) :
    print(i)       


def acronym_generator(listofword):
    for word in listofword:
        wl = word.split()
        acr = ''
        for w in wl:
            acr += w[0].upper()
        yield (acr)    

words = ['Project manager']   
for acr in acronym_generator(words):
    print(acr)     

        