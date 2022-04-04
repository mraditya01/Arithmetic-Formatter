def arithmetic_arranger(problems, d=bool()):
  num1, num2, dasht, answer= "","","",""
  if len(problems) >5:
    return "Error: Too many problems."
  for n in range(len(problems)):
    a=problems[n].split(" ")
    dash, space1, space2 = "", "", " "
    if a[1] == "/" or a[1] == "*":
      return "Error: Operator must be '+' or '-'."
    elif any(c.isalpha() for c in a[0]) == True or any(c.isalpha() for c in a[2]):
      return "Error: Numbers must only contain digits."
    elif len(a[0]) > 4 or len(a[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    if len(a[0]) > len(a[2]):
      space1= " "
      dash = (len(a[0]) + 2) * "-"
      space2 = (len(a[0])-len(a[2])+1)*" "
    elif len(a[0]) < len(a[2]):
      space2= " "
      dash = (len(a[2]) + 2) * "-"
      space1 = (len(a[2])-len(a[0])+1)*" "
    else:
      space1=" "
      space2=" "
      dash=(len(a[2])+2)*"-"
    if n==0:
      space=""
      space3=" "
    else:
      space="    "
      space3="     "
    num1 += f"{space3}{space1}{a[0]}"
    num2 += f"{space}{a[1]}{space2}{a[2]}"
    dasht += f"{space}{dash}"
    space4 = (len(dash) - len(f"{eval(a[0]+a[1]+a[2])}")) * " "
    answer += f"{space}{space4}{eval(a[0]+a[1]+a[2])}"
  if d == True:
    return f"{num1}\n{num2}\n{dasht}\n{answer}"
  elif d == False:
    return f"{num1}\n{num2}\n{dasht}"

