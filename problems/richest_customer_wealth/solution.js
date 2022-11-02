/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    
    var largestAmount = 0;
    
    for(let i = 0; i < accounts.length; i++){
        let newAmount = 0;
        
        for(let j = 0; j < accounts[i].length; j++){
            
            newAmount += accounts[i][j]
            // console.log(newAmount)
            
            if (newAmount > largestAmount){
            largestAmount = newAmount
            }
        }     
    }
    
    return largestAmount
};