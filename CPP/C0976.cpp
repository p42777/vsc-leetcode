#include <iostream>
using namespace std;

class Solution{
    public:
        int largestPerimeter(vector<int> &nums){

            int n = nums.size();
            int prev = n - 3; // the smallest side of the triangle
            int next = n - 2; // the second largest side of the triangle
            int last = n - 1; // the largest side of the triangle

            sort(nums.begin(), nums.end()); // sort array

            while (nums[prev] + nums[next] <= nums[last]){ // triangle inequality must be satisfied
                last--;
                next--;
                prev--;
                if (prev < 0) return 0; 
            }
            return nums[prev] + nums[next] + nums[last]; // return the perimeter
        }
};