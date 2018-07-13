""" Prepro 61 """

def main():
    """ Sorted Score """
    data = list()
    amount = int(input())

    for _ in range(amount):
        name = input()
        score = int(input())
        data.append([score, name])

    for i in sorted(data):
        print(i[0], i[1])

main()
