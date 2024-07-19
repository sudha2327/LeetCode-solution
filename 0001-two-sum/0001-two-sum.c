

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int* re;
        re=(int*)malloc(sizeof(sizeof(int)* *returnSize));
    //int s=1;
      //  returnSize[s];
        for(int i=0;i<numsSize;i++){
            for(int j=i+1;j<numsSize;j++){
                //int sum=nums[i]+nums[j];
                if(nums[i]+nums[j]==target){
                    re[0]=i;
                    re[1]=j;
                    break;
                   
                }
            }
        }
   return re;
}
