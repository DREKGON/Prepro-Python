""" Prepro 61 """

def main():
    """ Ascending Sort """
    num = int(input())
    emplist = []

    for _ in range(num):
        num1 = int(input())
        emplist.append(num1)

    emplist.sort()

    for i in emplist:
        print(i)

main()
