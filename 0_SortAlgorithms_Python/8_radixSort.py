'''
桶排序(基数排序）是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。
桶排序 (Bucket sort)、基数排序(Radix sort)的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，
每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。

算法描述
1.设置一个定量的数组当作空桶；
2.遍历输入数据，并且把数据一个一个放到对应的桶里去；
3.对每个不是空的桶进行排序；
4.从不是空的桶里把排好序的数据拼接起来。

算法分析
桶排序最好情况下使用线性时间O(n)，桶排序的时间复杂度，
取决与对各个桶之间数据进行排序的时间复杂度，因为其它部分的时间复杂度都为O(n)。
很显然，桶划分的越小，各个桶之间的数据越少，排序所用的时间也会越少。但相应的空间消耗就会增大。
'''
import math
class Solution:
    def radixSort(self,arr,radix=10):
        k = int(math.ceil(math.log(max(arr),radix))) #计算位数，排序k轮
        bucket = [[] for i in range(radix)]
        for i in range(1,k+1):
            for j in arr:
                bucket[int(j/(radix**(i-1))%(radix**i))].append(j)
            del arr[:]
            for z in bucket:
                arr += z
                del z[:]
        return arr


if __name__=='__main__':
    nums = [22, 17, 11, 15,1,4,25,13,21,3]
    s = Solution
    print(s.radixSort(s,nums))