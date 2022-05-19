def count_by(x,n):
    multi_array = []
    count_amount = n
    manip_num = x
    while count_amount > 0:
        manip_num * x
        multi_array.append(manip_num)
        manip_num += x
        count_amount -= 1
    return(multi_array)

# Could use range() that has three parameters (min, max and iterate by!) 

count_by(1, 10)