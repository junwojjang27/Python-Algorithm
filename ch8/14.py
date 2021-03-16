def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1   
    
    if l1.val < l2.val:
        merge = l1
        l1 = l1.next
    else:
        merge = l2
        l2 = l2.next
    
    temp = merge        #temp로 바꾸는 부분이 포인트
    
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
            temp = temp.next
        else:
            temp.next=l2
            l2 = l2.next
            temp = temp.next
            
            
    if not l1:
        temp.next=l2
    else:
        temp.next = l1
            
    return merge