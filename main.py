file = open('Codingal (1).txt','r')
print(file.read())
file.close()

file = open('Codingal (1).txt','r')
print("/n Read in parts /n")
print(file.read(8))
file.close()

file = open('Codingal (1).txt','a')
file.write("\n Hi! I am penguin and I am 1 year old.")
file.close()