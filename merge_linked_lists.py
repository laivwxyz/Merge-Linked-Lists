class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def make_linked_list(*data):
    new_data = sorted(list(data))
    if len(new_data) in range(0, 51):
        if int(new_data[0]) < -100 or int(new_data[-1]) > 100:
            raise Exception("Values should only be in the range -100 and 100.")
    else:
        raise Exception("The total number of nodes in both lists should not exceed 50")

    head = ListNode(int(new_data[0]))
    current = head
    for number in new_data[1:]:
        current.next = ListNode(int(number))
        current = current.next

    print("\033[96mUnmerged List: ", end="\033[0m")
    current = head
    while current:
        print(current.value, end=" ")
        if current.next is not None:
            print("→", end=" ")
        current = current.next
    print()
    print()

    return head

def merge_lists(list1, list2):
    temp = ListNode()
    tail = temp

    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    print("\033[96mMerged List: ", end="\033[0m")
    current = temp.next
    while current:
        print(current.value, end=" ")
        if current.next is not None:
            print("→", end=" ")
        current = current.next
    print()
    print()

list1 = make_linked_list(1, 2, 4)
list2 = make_linked_list(1, 3, 4)
merge_lists(list1, list2)