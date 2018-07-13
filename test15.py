""" Prepro 61 """

def main():
    """ Find Distance Between 2 Points """
    num = input()
    num = num.split(", ")
    list_new = []
    for i in num:
        i = int(i)
        list_new.append(i)
    sorted(list_new)
    print(list_new)

main()
