def main():
    p=int(input("what is your age?"))
    if p < 18:
        print("You cant vote")
    elif p == 18:
        print("You can vote and you can be drafted")
    elif p >= 21:
        print("You can legally drink")

    if p==19:
        print("you can vote and you can be drafted")

    if p==20:
        print("You can vote and you can be drafted")


if __name__ == '__main__':
    main()