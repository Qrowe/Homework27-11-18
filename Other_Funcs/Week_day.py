today=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
condition=['Sober', 'Headache']
def Party_hard(a):
    if today == 'Saturday':
        print('Party!')
    elif today == 'Sunday':
        def Condition():
            if condition == 'Headache':
                print ('Recover, then rest.')
            else:
                print('Rest.')
        Condition('Headache')
    else:
        print('Work, work, work.')
Party_hard('Saturday')
