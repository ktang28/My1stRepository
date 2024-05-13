import math
def avg(ls):
    for i in ls:
        avg_result = sum(ls)/len(ls)
    return avg_result

ls = [1,2,3,5,6]
result = avg(ls)
print(result)


