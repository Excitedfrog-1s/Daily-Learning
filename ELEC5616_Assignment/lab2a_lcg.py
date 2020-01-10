a, b = 23, 21
c = 2**8 - 1

# To show what happens when you select a bad set of values,
# set c = 2**8 and watch what happens to 'x % 2'
# It will always flip between 0 and 1 -- i.e. is 100% predictable


def lcg_generate(x):
    return (a * x + b) % c


# This generates a full set of cards: each suit with each type
# To understand the syntax, Google for "list comprehensions"
cards = [s + n for s in "SDHC" for n in "A23456789XJQK"]
# The list comprehension above is equivalent to the for loops below
# cards = []
# for suit in 'SDHC':
#     for card_type in "A23456789XJQK":
#         cards.append(suit + card_type)

if __name__ == "__main__":
    x = 19
    print("Starting the LCG with seed =", x)
    for i in range(15):
        x = lcg_generate(x)
        print("%s (%d %d)" % (cards[x % 52], x, x % 2))
