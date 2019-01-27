/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include<stdlib.h>
#include<stdio.h>
int* twoSum(int* nums, int numsSize, int target) {
    int * ret = (char*)malloc(2*sizeof(int));  // 初值都是0，可以当作数组使用
    printf("%ld\n",sizeof(*(ret)));
    printf("%d\n",*(ret+1));
    int i, j;
    for(i=0;i<numsSize;i++){
        for(j=i+0;j<numsSize;j++){
            if (nums[i]+nums[j] == target){
                *ret=i;
                *(ret+1)=j;
                return ret;
            }
        }
    }
    return ret;
}

int main(){
    int nums[5]={1,2,3,4,5};
    int max=5;
    int target = 5;
    int* ret;
    ret = twoSum(nums,max,target);
    int i=0;
    for(;i<2;i++){
        printf("%d\n",*(ret+i));
    };
    printf("%d\n",*ret);
    return 0;
}