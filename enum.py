fh=open('enum.txt','r')
res = fh.read()
doc = res.split('\n')
for count,item in enumerate(doc):
	print ({count,item})
	print (count,item)