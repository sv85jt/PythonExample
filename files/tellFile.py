rank = open('rank.log')

print ('current position {}'.format(rank.tell()))
print (rank.read())
print ('current position {}'.format(rank.tell()))


rank.seek(20)
print ('current position {}'.format(rank.tell()))
print (rank.read())



