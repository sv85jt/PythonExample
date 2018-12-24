
color = {'apple':'red', 'banana':'yellow', 'chiku':'brown'}

print ("\nThe color of apple is {}".format(color['apple']))
print ('The color of chiku is {}'.format(color['chiku']))


color['orange']='orange'
print ( color )

print ('Length of color dict {}'.format(len(color)))


del color['chiku']
print ('Length of color dict {}'.format(len(color)))
print ( color )
