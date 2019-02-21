'''
归并排序是建立在归并操作上的一种有效的排序算法。
该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，
再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。

算法描述
1.把长度为n的输入序列分成两个长度为n/2的子序列；
2.对这两个子序列分别采用归并排序；
3.将两个排序好的子序列合并成一个最终的排序序列。

算法分析
归并排序是一种稳定的排序方法。和选择排序一样，归并排序的性能不受输入数据的影响，
但表现比选择排序好的多，因为始终都是O(nlogn）的时间复杂度。代价是需要额外的内存空间。
'''
class Solution:
    def mergeSort(self,arr):
        if len(arr)<=1:
            return arr
        mid = len(arr) // 2
        left = self.mergeSort(self,arr[:mid])
        right = self.mergeSort(self,arr[mid:])
        return self.merge(self,left,right)

    def merge(self,left,right):
        i,j=0,0
        result = []
        while i<len(left) and j<len(right):
            if left[i] <=right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

if __name__=='__main__':
    nums = [22, 17, 11, 15,1,4,25,13,21,3]
    s = Solution
    print(s.mergeSort(s,nums))