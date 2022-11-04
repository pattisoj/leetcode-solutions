/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let count = 0;
    
    for (let i = 0; i < nums.length; i++) {

        if (i < nums.length - 1 && nums[i] == nums[i + 1]) {
            continue;
        }
        
        nums[count] = nums[i];
        count++;
    }

    return count;
 };

    /*
    My initial code to sole this problem works to remove duplicates from the nums array.
    However, the description of the problem requires a different type of solution to account for languages where it is impossible to change the length of the array.
    Hence the code above.

    for(let i = 0; i < nums.length; i++){
        if(nums[i+1] === nums[i]){
            nums.splice(i, 1)
        }
    }

    return nums
    */
