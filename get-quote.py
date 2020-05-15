def main():
   print("Keep it logically awesome.")

   f = open("/storage/emulated/0/python programs/quotes.txt")
   quotes = f.readlines()
   f.close()

   print(quotes)

if __name__== "__main__":
  main()
