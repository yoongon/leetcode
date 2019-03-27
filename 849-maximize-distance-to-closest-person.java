class Solution {
    public int maxDistToClosest(int[] seats) {
        int l=0, r=seats.length-1;
        while (seats[l]==0) {
            l++;
        }
        while (seats[r]==0) {
            r--;
        }
        
        int res = Math.max(l, seats.length-r-1);
        int base = l;
        for (int i=l; i<r+1; i++) {
            if (seats[i] == 1) {
                res = Math.max(res, (int)Math.ceil((i-base-1)/2.0)); // int 변환은 이렇게
                base = i;
            }
        }
        return res;
    }
}
