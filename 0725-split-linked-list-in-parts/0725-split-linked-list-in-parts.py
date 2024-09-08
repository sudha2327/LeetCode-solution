class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        # Initialize the length of the list and a temporary node to iterate through the list
        list_length, current_node = 0, root
        # Calculate the total length of the list
        while current_node:
            list_length += 1
            current_node = current_node.next
      
        # Reset the current_node back to the beginning of the list
        current_node = root
        # Determine the size of each part and the extra nodes to distribute
        part_size, extra_nodes = divmod(list_length, k)
        # Initialize the result list with None placeholders for each part
        result = [None for _ in range(k)]

        # Split the list into k parts
        for i in range(k):
            # The beginning of the current part
            part_head = current_node
            # Calculate the number of nodes this part should have
            current_part_size = part_size + (i < extra_nodes)

            # Iterate through the current part's nodes, stopping before the last node
            for j in range(current_part_size - 1):
                if current_node:
                    current_node = current_node.next
          
            # If there are nodes in the current part, disconnect this part from the next one
            if current_node:
                # Temporarily store the next part
                next_part = current_node.next
                # Disconnect the current part from the rest of the list
                current_node.next = None
                # Move the current_node to the beginning of the next part
                current_node = next_part
          
            # Update the result with the head of the current part
            result[i] = part_head
      
        return result