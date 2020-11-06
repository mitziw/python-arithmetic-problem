import pandas as pd
import json
import re

acron = pd.read_csv('intlunions.csv', header=1,
                    index_col=0, squeeze=True).to_dict()

def getLANName(abrev):
  for i in acron:
    if i == abrev:
      return(acron[abrev])


with open("locals.csv", "r") as f:
  next(f)
  next(f)
  for line in f:
    for h in line:
      print(h.split(","))

optouts = ["GENPUB", "IAFF", "NPMHU", "UBC", "UTU"]

f = open("out.txt", "r")
optouts = f.read()
#print(optouts.split("\n"))

f.close()
 


  

