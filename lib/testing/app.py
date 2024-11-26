def interpolate_welcome(name = "Jane"):
   return f"Welcome {name}"

assert interpolate_welcome("Guido") == "Welcome Guido"

print(interpolate_welcome())