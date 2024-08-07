chart: list[str] = input().split(',')
changes: list[str] = input().split(',')

for change in changes:
    # change = change.split()
    # name = change[0]
    # delta =  change[1]

    name, delta = change.split()
    index: int = chart.index(name)
    chart.insert(index - int(delta), chart.pop(index))
print(chart)

"""
ЕгорКрид,LOBODA,МаксБарских,ДимаБилан,Artik&Asti
ДимаБилан +1,LOBODA -2,ЕгорКрид -3
"""
