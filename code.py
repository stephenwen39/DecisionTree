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

  if num_of_clasA == 3: #如果元素種類為3個
    b_c = [0,0,0] #就建構一個三元素的陣列
    for i in array:
      if i[atts_index] == 0: #依據當前的column來跑
        b_c[0] += 1
      elif i[atts_index] == 1:
        b_c[1] += 1
      else:
        b_c[2] += 1

  elif num_of_clasA == 2: #分不同case
    b_c = [0,0]
    for i in array:
      if i[atts_index] == 0:
        b_c[0] += 1
      else:
        b_c[1] += 1

  else:
    b_c = [len(array)]
  return b_c
    
def weight(atts_index, num_of_clasA, array): #計算entropy with branch weight
  
  ans_ = []
  b_c = count(atts_index, num_of_clasA, array) #計算每個atts出現的次數

  for j in range(0,num_of_clasA): #跑遍所有的atts種類數量，在這個case可能是3或2
    clas = [0,0] #這個陣列用來裝yes與no的個數
    for i in array: #對所有資料進行「如果用這個屬性作為樹根，下面會有多少yes與no的計算
      if i[atts_index] == j:
        if i[4] == 0:
          clas[0] += 1
        else:
          clas[1] += 1
    #print(type(ans_),type(b_c),type(array),b_c[j])
    ans_.append(b_c[j]/len(array)*(entropy(clas[0],clas[1],0))) #計算entropy with branch weight
  return ans_
  
def find(array, parent_entropy):
  ans = []
  for i in range(0,4): #對所有的column
    cunt = []
    for j in array: #計算個別column出現的attributes種類數量
      
      if j[i] not in cunt:
        cunt.append(j[i])
    
    length = len(cunt) #len(cunt)是代表atts種類數量
    
    ans.append(parent_entropy - sum(weight(i,length,array))) #父節點減去子節點的總和，總共會有四個，因為有四個屬性
  return ans #回傳gainration
  
'''
print(answer[0]/entropy(5,3,4))
print(answer[1]/entropy(3,5,4))
print(answer[2]/entropy(6,6,0))
print(answer[3]/entropy(7,5,0))
'''
