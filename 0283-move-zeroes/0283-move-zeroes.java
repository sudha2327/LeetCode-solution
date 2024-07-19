class Solution {
    public void moveZeroes(int[] nums) {
 
           ArrayList<Integer> m=new ArrayList<Integer>();
           ArrayList<Integer> m1=new ArrayList<Integer>();
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                m.add(nums[i]);
                
            }else{
                m1.add(nums[i]);
            }
            
        }
      m1.addAll(m);
        for(int i=0;i<nums.length;i++){
            nums[i]=m1.get(i);
        }
       
    }
}