class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head is not None:
            temp_array = []
            node = head
            while node :
                temp_array.append(node.val)
                # print("node is {}".format(node.val))
                if node.next:
                    node = node.next
                else:
                    node = None            
            # print("array is {}".format(temp_array))        

            val_to_return = ListNode(temp_array[0])
            for i in range(1, len(temp_array)):
                node_to_add = ListNode(temp_array[i])
                node_to_add.next = val_to_return
                val_to_return = node_to_add

            # print("val to return is {}".format(val_to_return))
            return val_to_return
        else:
            return head
