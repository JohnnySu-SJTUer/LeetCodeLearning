'''
快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，
其中一部分记录的关键字均比另一部分的关键字小，
则可分别对这两部分记录继续进行排序，以达到整个序列有序。

算法描述
快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：

1.从数列中挑出一个元素，称为 “基准”（pivot）；
2.重新排序数列，所有元素比基准值小的摆放在基准前面，
所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

算法分析
快速排序是通常被认为在同数量级（O(nlog2n)）的排序方法中平均性能最好的。
但若初始序列按关键码有序或基本有序时，快排序反而蜕化为冒泡排序。
为改进之，通常以“三者取中法”来选取基准记录，
即将排序区间的两个端点与中点三个记录关键码居中的调整为支点记录。快速排序是一个不稳定的排序方法。
'''
class Solution:
    def quickSort(self,arr,left,right):
        if left >= right:
            return arr
        key = arr[left]
        low = left
        high = right
        while left <right:
            while left<right and arr[right]>=key:
                right -= 1
            arr[left] = arr[right]
            while left<right and arr[left]<=key:
                left += 1
            arr[right] = arr[left]
        arr[right] = key
        self.quickSort(self,arr,low,left-1)
        self.quickSort(self,arr,left+1,high)
        return arr


if __name__=='__main__':
    nums = [22, 17, 11, 15,1,4,25,13,21,3]
    s = Solution
    print(s.quickSort(s,nums,0,len(nums)-1))