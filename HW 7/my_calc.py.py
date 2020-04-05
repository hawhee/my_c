def calc(a,b):
  op = str(input("Введите знак: "))
  try:
    a, b = float(a), float(b)
  except Exception as err:
      print(err)
  if op == "+":
    return a+b
  elif op == "-":
    return a-b
  elif op == "*":
    return a*b
  elif op == "/":
    try:
      return a/b
    except ZeroDivisionError:
      print("На ноль делить нельзя!")
