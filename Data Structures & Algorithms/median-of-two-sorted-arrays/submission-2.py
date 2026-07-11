class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #merging two list
        m=len(nums1)
        n=len(nums2)
        c=[0]*(m+n)
        k=i=j=0
        while(i<m and j<n):
            if nums1[i]<nums2[j]:
                c[k]=nums1[i]
                i+=1
            else:
                c[k]=nums2[j]
                j+=1
            k+=1
        while(i<m):
            c[k]=nums1[i]
            k+=1
            i+=1
        while(j<n):
            c[k]=nums2[j]
            k+=1
            j+=1

        #median                
        # median=0.0
        if len(c)%2==0:
            index1=(0+(len(c)-1))//2
            index2=index1+1
            median=(c[index1]+c[index2])/2
        else:
            index=(0+(len(c)-1))//2
            median=c[index]
        return median
