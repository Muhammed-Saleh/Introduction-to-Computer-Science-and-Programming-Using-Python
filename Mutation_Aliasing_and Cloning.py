######################################################
cool = ['blue', 'green', 'grey']         
chill = ['blue', 'green', 'grey']         
print(cool)
print(chill)
chill[2] = 'bleu'
print(cool)
print(chill)
######################################################
cool = ['blue', 'green', 'grey']         
chill = cool[:]
chill.append('black')
print(chill)
print(cool)
######################################################
warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]
print(warm)
print(hot)
print(brightcolors)
brightcolors.append(hot)
print(brightcolors)
hot.append('pink')
print(hot)
print(brightcolors)
print(hot+warm)
######################################################
def remove_dups(l1,l2):
    for e in l1:
        if e in l2:
            l1.remove(e)

l1 = [1, 2, 3, 4]
l2 = [1, 2, 5, 6]            

remove_dups(l1,l2)
######################################################
def remove_dups_new(l1, l2):
    l1_copy = l1[:]
    for e in l1_copy:
        if e in l2:
            l1.remove(e)

l1 = [1, 2, 3, 4]
l2 = [1, 2, 5, 6]            

remove_dups_new(l1, l2)
######################################################
