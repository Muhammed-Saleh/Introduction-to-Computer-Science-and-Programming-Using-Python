def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))    
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios

###########################################################
def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats

def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return 0.0    

test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
           [['bruce', 'wayne'],[10.0, 8.0, 74.0]],
           [['captain', 'america'], [8.0,10.0,96.0]],
           [['deadpool'], []]]    