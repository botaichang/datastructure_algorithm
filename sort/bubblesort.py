# -*- coding: utf-8 -*-

import numpy as np 

#----------------------------------------------
# 冒泡排序
# 1.对每一次的轮循中，见到逆序元素就交换其位置，因此，一次轮训完后，会将最大（小）的元素放在最后
# 2.在下次轮循时，访问的元素个数就可以比上次少1，因为一个元素已经排好
# 3.时间复杂度O(n^2)
#----------------------------------------------
def bubblesort(arr):
   n = len(arr)
   for j in range(n,0,-1):
      for i in range(1,j,1):
          if arr[i-1] > arr[i]:
              arr[i],arr[i-1] = arr[i-1],arr[i]
   return arr


if __name__ == '__main__':

    arr = [3, 4, 5,9,8,1,7,6,2,9,10,11,15,13]
    print('before ',arr)
    bubblesort(arr)
    print('after',arr)
