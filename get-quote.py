import random
#def primary():
  # print("Keep it logically awesome.")
f = open("/storage/emulated/0/python programs/python-random-quote-master/python-random-quote-master/quotes.txt")
quotes = f.readlines()
f.close()
print(len(quotes))

last = len(quotes) -1
rnd = random.randint(0, last)

print(quotes[13])


"""if __name__== "__main__":
  primary()"""
