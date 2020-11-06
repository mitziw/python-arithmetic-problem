import pandas as pd
import numpy as np

def arithmetic_arranger(problems, solve=False):
  j: int = 0
  k: int = 0
  l: int = 0
  errmsg: str = ""
  if len(problems) == 0:
    return print("\nError: No problems submitted.")
  if len(problems) > 5:
    return print("\nError: Too many problems.")
  
  df = pd.DataFrame(problems)
  dlist: list = []
  for j in range(0, len(df)):
    dlist.append(df[0][j].split(" "))
    j += 1
  mystr1: str = ""
  mystr2: str = ""
  mystr3: str = ""
  result: list = []
  for k in range(0, len(dlist) - 1):
    a, b, c = dlist[k][0], dlist[k][1], dlist[k][2]
    if a.isdigit():
    elif c.isdigit():
    else:
      return print("\nError: Numbers must only contain digits.")
    if c.isdigit():
      pass
    
    if b == "+":
    elif b == "-":
    else:
      
        
        else:
        if (int(dlist[k][0]) == False
          return print("\nError: Numbers must only contain digits.")
        if int(dlist[k][2]) == False:
          return print("\nError: Numbers must only contain digits.")
        if len(int(dlist[k][0])) >= 4:
          return print("\nError: Numbers cannot be more than four digits.")
        if len(int(dlist[k][2])) >= 4:
          return print("\nError: Numbers cannot be more than four digits.")

    mystr1 += dlist[k][0].rjust(6, " ") + "    "
    mystr2 += dlist[k][1].rjust(1) + dlist[k][2].rjust(5, " ") + "    "
      
    k += 1
  
  mystr3 = (mystr3.rjust(6, "-") + mystr3.rjust(4, " ")) * len(dlist)
  return print(mystr1 + "\n" + mystr2 + "\n" + mystr3)


arithmetic_arranger(["32 + 698", "3801 * 2", "45 + 43", "123 + 49"])
