# Function calling


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()



def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


'''
aa = range (0 ,1000)

y=34554556460455456405654050684516122545415455121245
x=23545138421451821851216845354685357879565563321545
print (x*y)
while(1):
    a=1


#0 1 1 2 3 5
# x y z
def dictionairy():
    # Declaring hash function
    key_value = {}

    # Initializing the value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 2
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    importers = {'Salvador': 1234,
                 'Nicaragua': 152,
                 'Spain': 252,
                 'itali':23
                 }

    exporters = {'Spain': 252,
                 'Nicaragua': 251,
                 }

    aa = (importers.keys() - exporters.keys())
    print (aa)
    for a in aa:
        exporters[a] =0
    print (exporters)


#    print("Task 3:-\nKeys and Values sorted",
#          "in alphabetical order by the value")

    # Note that it will sort in lexicographical order
    # For mathematical way, change it to float
    out = sorted(key_value.items(), key= lambda kv: (kv[1], kv[0]))
    print(out)

def main():
    # function calling 
    dictionairy()


# main function calling
if __name__ == "__main__":
    main() '''
