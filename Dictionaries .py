grades = {'Ana':'B', 'John':'+A', 'Denise':'A', 'Katy':'A'}
print(grades)
print(grades['John'])
###########################################
grades = {'Ana':'B', 'John':'+A', 'Denise':'A', 'Katy':'A'}
grades['sylven'] = 'A'
print(grades['sylven'])
###########################################
grades = {'Ana':'B', 'John':'+A', 'Denise':'A', 'Katy':'A'}
grades['sylven'] = 'A'
print('sylven' in grades)
###########################################
grades = {'Ana':'B', 'John':'+A', 'Denise':'A', 'Katy':'A'}
del (grades['Ana'])
print(grades)
###########################################
grades = {'Ana':'B', 'John':'+A', 'Denise':'A', 'Katy':'A'}
print(grades.keys)
