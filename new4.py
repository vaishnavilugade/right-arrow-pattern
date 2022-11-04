

def rightarrow(a):
      for i in range(0, a):
           for j in range(0, i + 1):
                print("* ", end="")
           print(">")
      for i in range(a, -1 , -1):
          for j in range(0, i + 1):
               print("* ", end="")
          print(">")
 
pattern(10)