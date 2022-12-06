/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var oddEvenList = function(head) {
    if(!head || !head.next || !head.next.next) {
        return head
    }

    let cur = head
    let next = head.next

    while(next && next.next) {
        const temp = next.next
        const temp2 = cur.next

        cur.next = temp
        next.next = temp.next
        temp.next = temp2

        cur = cur.next
        next = next.next
    }

    return head
};