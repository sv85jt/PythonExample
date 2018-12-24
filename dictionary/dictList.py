
color = {
	'animals':['cow','dog','pig'],
        'birds': 'sparrow'
}

print ( color )

print ('List of animals ->  {}'.format(color['animals']))
print ('List of birds -> {}'.format(color['birds']))

print ("\n\n")
for item in color['animals']:
    print (item)
