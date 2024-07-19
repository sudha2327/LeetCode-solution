

int maxSubArray(int* nums, int numsSize){
    
    int max_so_for=INT_MIN,max_find=0,i=0;
    
    for(i=0;i<numsSize;i++){
        max_find=max_find+nums[i];
        
        if(max_so_for<max_find){
            max_so_for=max_find;
        }
        if(max_find<0){
            max_find=0;
        }
    }
    
    return max_so_for;

}