

int searchInsert(int* nums, int numsSize, int target){
    
//     int mid;
//     int s=0;
//     int i=0;
//     int b=1;
//     int l=numsSize;
//     if(l>=s){
//         mid=s+l/2;
        
//         if(nums[mid]==target){
//             return mid;
//         }else if(nums[mid]<target){
            
//             return searchInsert(nums,mid+1,target);
            
//         }else{
//             return searchInsert(nums,mid-1,target);
//         }
        
//         for(i=0;i<numsSize;i++){
             
//           if(nums[i]!=target){
//               if(nums[i]>=target){
//                     b++;
//               }
//           }
//       }
//     }
    
    
//     return b;
    
    int mid;
    int low = 0;
    int high = numsSize-1;
    
    while( low <= high) {
        
        mid = (low + high) / 2;
        
        if(nums[mid] == target)
            return mid;
        
        if( target > nums[mid]) 
            low = mid+1;
        else
            high = mid-1;
        
    }
    if(low > (numsSize-1))
        return mid+1;
    else {
        if(target > nums[mid])
                return mid+1;
        else 
                return mid;
 
    }

}