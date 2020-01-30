melon_cost = 1.00

def account(file_path):
    f=open(file_path)
    for line in f:
        line=line.strip()
        words=line.split('|')
        #print (words)
        customer1_name = words[1]
        customer1_melons = int(words[2])
        customer1_paid = float(words[3])
        customer1_expected = customer1_melons * melon_cost
        if customer1_expected != customer1_paid:
            print(f"{customer1_name} paid ${customer1_paid:.2f},",
            f"expected ${customer1_expected:.2f}"
            )

account('customer-orders.txt')

