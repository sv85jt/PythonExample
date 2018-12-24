
def get_name():
   name = input("what is your name : ")
   return name


def say_name (name):
   print ('My name is {} '.format(name))



def get_and_say_name():
   """ Get and Dispaly name """
   name = get_name()
   say_name(name)


get_and_say_name()


