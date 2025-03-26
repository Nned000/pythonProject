result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b

data = {10: 2, 2: 5, 123: 4, 18: 0, 0: 15, 8 : 4}  #тут не може бути списків

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError:
        print("Value Error")
    except IndexError:
        print("Index Error")
    except ZeroDivisionError:
        print("Zero Devision Error")


print(result)