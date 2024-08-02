chart: list[str] = input().split(',')
changes: list[str] = input().split(',')

for change in changes:
    name, delta = change.split()
    index = chart.index(change[:len(change) - 3]) 

    pos = int(change[len(change) - 2: len(change)])  
    
    chart.insert(pos, change[:len(change) - 3])  

print(chart)
