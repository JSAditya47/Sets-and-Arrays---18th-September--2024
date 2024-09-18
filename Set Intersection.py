setx = {"green", "blue"}
sety = {"blue", "yellow"}

print("Original Set Elements: ")
print(setx)
print(sety)
print()

print("\nIntersection of Two Said Sets: ")
setz = setx.intersection(sety)
print( setz )

print("\nUNION of Two Said Sets: ")
setv = setx.union(sety)
print(setv)

print("\nDifference of Two Said Sets:")
setk = setx.difference(sety)
print(setk)