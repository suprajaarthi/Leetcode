class Solution(object):
    def middleNode(self, head):       
        slow = head
        fast = head
        while fast != None and fast.next != None : #if fast.next is not None yet, then fast.next.next would only be none the worst case scinario, it wouldn't throw it doesn't exist error            
            slow = slow.next
            fast = fast.next.next         

        return slow
      
      '''
      We will have two pointers (slow and fast)
They start at the head and the slow move one step and the fast move two steps
--> Since the fast is moving 2x speed than the slow, by the time the fast reach to the end the slow would be half way to the end
--> Thus when the fast hit the end we return the slow (the middel)*

'''
