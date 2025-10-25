setx = {"green", "blue"}
sety = {"blue", "yellow"}

print("Original set elements:")
print(setx)
print(sety)

print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)

a={1,2,3,5}
b={5,6,7}
print("union",a.union(b))#{1,2,3,5,6,7}
print("intersection",a.intersection(b))#{5}
print("Difference",a.difference(b))#{1,2,3}
print("Symmetric Difference:", a.symmetric_difference(b)) 
