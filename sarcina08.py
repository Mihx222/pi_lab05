terms = 11
result = list(map(lambda x: 2 ** x, range(terms)))

print("Puterile lui 2 pana la:", terms)
for i in range(terms):
    print("2 la puterea ", i, " este: ", result[i])
