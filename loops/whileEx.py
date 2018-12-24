

def start():
   print ("----- START -----")

def end():
   print ("----- END -----")

start()

animals = ['dog','cat','horse','cow']

count = 0
animals.append('goat')
#animals.clear()

while count < len(animals):
    print ('Current animals is {}'.format(animals[count].upper()))
    count += 1

end ()
print ("---------- END ----------")
