""" Prepro 61 """

def main():
    """ Prohibited Items """
    prohibited = ["addictive substances", "cigarettes", "weapons", "alcohol", "illegal items"]
    items_list = list()
    num = int(input())

    for _ in range(num):
        item = input().lower()
        if item not in prohibited:
            items_list.append(item)

    for i in items_list:
        print(i.lower())

main()
