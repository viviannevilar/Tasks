def f_to_c(tempc):
    tempf = (tempc - 32)*5/9
    return tempf


tempc = [32, 113, 26.6]
for i in tempc:
    print(f"{i}C = {f_to_c(i)}F")

