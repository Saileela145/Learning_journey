a=[12,23,24,45,24,67,87,49,34,55,12,23]
even=0
odd=0
for n in a:
    if n%2==0:
       even+=1
    else:
       odd+=1
print("even numbers:",even)
print("odd numbers:",odd)
