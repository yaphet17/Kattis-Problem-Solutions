def days(num_statues):
    printer=1
    day=0
    while printer<num_statues:
        printer*=2
        day+=1
    day+=1
    print(day)
days(int(input()))
        
    
