// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
     long l=0, h=n-1;
        long m;
        while(l<=h)
        {
            m=(l+h)/2;
            
            if(isBadVersion(m))
                h=m-1;
            else l=m+1;
        }
        return l;
    }
};