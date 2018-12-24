
def dash():
   print ("------------------------------")

def start():
   print ("\n----- START -----\n")

def end():
   print ("\n----- END -----\n")

start()
dash()
animals = ['cow','dog','cat','mokey','tiger','lion','zebra']
print ('List of animals {}'.format(animals))

dash()
sorted_animals = sorted ( animals )
print ('List of sorted animals {}'.format(sorted_animals))
end()


print ('List of animals {}'.format(animals))
animals.sort()
print ('List of sort animals {}'.format(animals))

