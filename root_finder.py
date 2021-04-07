import math
'''
A = [[0,0,0,0,0],
     [0,0,0,1,0],
     [1,0,0,0,1],
     [2,1,0,0,1],
     [2,2,1,0,1],
     [2,2,1,1,0],
     [1,2,1,1,1],
     [0,1,0,0,0],
     [0,2,1,0,1],
     [2,1,1,0,1],
     [0,1,1,1,1],
     [1,1,0,1,1]]
'''

def entropy(Y, N, Z):
  if Y == 0:
    return 0
  elif N == 0:
    return 0
  elif Z == 0:
    return -(Y/(Y+N) * math.log(Y/(Y+N),2) + 
            N/(Y+N) * math.log(N/(Y+N),2))
  else:
    return -(Y/(Y+N+Z) * math.log(Y/(Y+N+Z),2) + 
            N/(Y+N+Z) * math.log(N/(Y+N+Z),2) +
            Z/(Y+N+Z) * math.log(Z/(Y+N+Z),2))
    
def count(atts_index, num_of_clasA, array):

  if num_of_clasA == 3: #if the number of element is three
    b_c = [0,0,0] #create a list with 3 elements
    for i in array:
      if i[atts_index] == 0: #processing in current column
        b_c[0] += 1
      elif i[atts_index] == 1:
        b_c[1] += 1
      else:
        b_c[2] += 1

  elif num_of_clasA == 2: #case by case
    b_c = [0,0]
    for i in array:
      if i[atts_index] == 0:
        b_c[0] += 1
      else:
        b_c[1] += 1

  else:
    b_c = [len(array)]
  return b_c
    
def weight(atts_index, num_of_clasA, array): #entropy with branch weight
  
  ans_ = []
  b_c = count(atts_index, num_of_clasA, array) #coculate the number of attributes

  for j in range(0,num_of_clasA): #for every single attributes value
    clas = [0,0] #list For Coculate The Number Of YES and NO
    for i in array: #對所有資料進行，如果用這個屬性作為樹根，下面會有多少yes與no的計算
      if i[atts_index] == j:
        if i[4] == 0:
          clas[0] += 1
        else:
          clas[1] += 1
    #print(type(ans_),type(b_c),type(array),b_c[j])
    ans_.append(b_c[j]/len(array)*(entropy(clas[0],clas[1],0))) #entropy with branch weight
  return ans_
  
def find(array, parent_entropy):
  ans = []
  for i in range(0,4): #forAllcolumn
    cunt = []
    for j in array: #AttributesNumberPerColumn
      
      if j[i] not in cunt:
        cunt.append(j[i])
    
    length = len(cunt) #len(cunt)is theNumberOfAttributes
    
    ans.append(parent_entropy - sum(weight(i,length,array))) #ParentNode - sum(ChildNode), 4 inTotal
  return ans #回傳gainration
  
'''
print(answer[0]/entropy(5,3,4))
print(answer[1]/entropy(3,5,4))
print(answer[2]/entropy(6,6,0))
print(answer[3]/entropy(7,5,0))
'''
