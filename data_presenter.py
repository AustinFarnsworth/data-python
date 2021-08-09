open_file = open("CupcakeInvoices.csv")

for line in open_file:
    line = line.split(',')
    cupcakes = line[2]
    print(cupcakes)



total = []

def calculation(amount, price):
    return amount * price

for line in open_file:
    line = line.rstrip('\n').split(',')
    total.append(calculation(int(line[3]), float[4]))


print(total)


open_file.close()










