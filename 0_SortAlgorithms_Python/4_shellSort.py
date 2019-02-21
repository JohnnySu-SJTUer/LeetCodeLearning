'''
1959年Shell发明，第一个突破O(n2)的排序算法，是简单插入排序的改进版。
它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。

算法描述
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：

1.选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
2.按增量序列个数k，对序列进行k 趟排序；
3.每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，
分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

算法分析
希尔排序的核心在于间隔序列的设定。既可以提前设定好间隔序列，也可以动态的定义间隔序列。
动态定义间隔序列的算法是《算法（第4版）》的合著者Robert Sedgewick提出的。
'''
class Solution:
    def shellSort(self,arr):
        gap = 0
        while(gap<len(arr)/3):
            gap = gap*3+1
        while(gap>0):
            for i in range(gap,len(arr)):
                temp = arr[i]
                j = i-gap
                while(j>=0 and arr[j]>temp):
                    arr[j+gap] = arr[j]
                    j = j - gap
                arr[j+gap] = temp
            gap = gap//3

        return arr

if __name__=='__main__':
    nums = [22, 17, 11, 15,1,4,25,13,21,3]
    s = Solution
    print(s.shellSort(s,nums))