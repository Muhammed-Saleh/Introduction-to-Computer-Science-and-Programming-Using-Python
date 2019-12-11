nameHandle = open('Kids', 'w')
for i in range(2):
    name = input('Enter name: ')
    nameHandle.write(name + '\')
nameHandle.close()
########################
nameHandle = open('Kids', 'r')
for line in nameHandle:
    print(line)
nameHandle.close()            
