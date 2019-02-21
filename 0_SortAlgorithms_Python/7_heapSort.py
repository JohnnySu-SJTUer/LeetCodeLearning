'''
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：
即子结点的键值或索引总是小于（或者大于）它的父节点。

算法描述
1.将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
2.将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)
和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
3.由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)
调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2….Rn-2)
和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。
算法分析
'''
class Solution:
    # 堆排序
    def heapSort(self,arr):
        size = len(arr)
        self.buildHeap(self,arr,len(arr))
        for i in range(0,size)[::-1]:
            arr[0], arr[i] = arr[i], arr[0]
            self.adjustHeap(self, arr,0,i)
        return arr

    # 创建堆
    def buildHeap(self,arr,size):
        for i in range(0,(size//2))[::-1]:
            self.adjustHeap(self,arr,i,size)

    # 调整堆
    def adjustHeap(self,arr,i,size):
        lchild = 2*i+1
        rchild = 2*i+2
        max = i
        if i<size//2:
            if lchild<size and arr[lchild]>arr[max]:
                max = lchild
            if rchild<size and arr[rchild]>arr[max]:
                max = rchild
            if max != i:
                arr[max], arr[i] = arr[i], arr[max]
                self.adjustHeap(self,arr,max,size)

if __name__=='__main__':
    nums = [22, 17, 11, 15,1,4,25,13,21,3]
    s = Solution
    print(s.heapSort(s,nums))