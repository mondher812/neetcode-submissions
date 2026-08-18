class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        store = {}
        n = 1
        c = head

        while c:
            store[n] = c
            c = c.next
            n += 1

        n -= 1

        c = head
        l = 2

        for i in range(n - 1):
            if i % 2 == 0:
                c.next = store[n - (i // 2)]
            else:
                c.next = store[l]
                l += 1

            c = c.next

        c.next = None