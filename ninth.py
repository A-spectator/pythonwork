
#52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
list=[2,3,5,4,9,6]
ll=[]
if len(list)>0:
    m=min(list)
    list.remove(m)
    ll.append(m)
print(ll)

