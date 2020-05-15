def primary():
   print("Keep it logically awesome.")

   f = open("/storage/emulated/0/python programs/python-random-quote-master/python-random-quote-master/quotes.txt")
   quotes = f.readlines()
   f.close()

   print(quotes)

if __name__== "__main__":
  primary()
