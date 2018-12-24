
contacts = {
            'sham':'9849002385',
            'kajal': '852'
}

for contact in contacts:
   print ('Contact number of {} is {}'.format(contact, contacts[contact]))


for name,contact in contacts.items():
    print ('{} contact number is {}'.format(name,contact))
