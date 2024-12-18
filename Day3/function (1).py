def GetValues(query):
    d = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thrusday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }
    return d[query]

n = int(input("enter the n :"))
print(GetValues(n))

   