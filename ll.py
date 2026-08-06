#LINKED LIST CONCEPTS
print("\n")
print("--------------------------------------------- Welcome to Linked List Concepts ------------------------------------------\n")

print("""
1. Add a node at Beginning
2. Add a node at End
3. Add a node at Position
4. Delete at Beginning
5. Delete at End
6. Delete at Position
7. Update a Node
8. Search a Node
9. Count Nodes
10. Traverse Linked List
11. Reverse Linked List
12. Middle Node
13. Detect Cycle
14. Find Cycle Start
15. Create Cycle (for testing)
16. Exit
""")

print("-" * 80)

---------------------------------------------------------------------------------------------------------------------------------------
# --------------------- Node Class ---------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# --------------------- Initial Linked List ---------------------

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

---------------------------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================================
#                INSERT OPERATIONS
# ======================================================================================================================================

# ---------- Add at Beginning ----------

def addAtStart(head, new_node):
    new_node.next = head
    print("Node added successfully at the beginning.")
    return new_node


# ---------- Add at End ----------

def addAtEnd(head, new_node):

    if head is None:
        print("Linked List was empty. Node added as Head.")
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node

    print("Node added successfully at the end.")
    return head


# ---------- Add at Position ----------

def addAtPos(head, new_node, pos):

    if pos <= 0:
        print("Invalid Position!")
        return head

    if pos == 1:
        return addAtStart(head, new_node)

    current = head
    count = 1

    while current and count < pos - 1:
        current = current.next
        count += 1

    if current is None:
        print("Position out of range!")
        return head

    new_node.next = current.next
    current.next = new_node

    print(f"Node inserted successfully at position {pos}")
    return head

---------------------------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================================
#                DELETE OPERATIONS
#======================================================================================================================================

# ---------- Delete Beginning ----------

def delAtStart(head):

    if head is None:
        print("Linked List is Empty!")
        return None

    print(f"Deleted Node : {head.data}")

    return head.next


# ---------- Delete End ----------

def delAtEnd(head):

    if head is None:
        print("Linked List is Empty!")
        return None

    if head.next is None:
        print(f"Deleted Node : {head.data}")
        return None

    current = head

    while current.next.next:
        current = current.next

    print(f"Deleted Node : {current.next.data}")

    current.next = None

    return head


# ---------- Delete at Position ----------

def delAtPos(head, pos):

    if head is None:
        print("Linked List is Empty!")
        return None

    if pos <= 0:
        print("Invalid Position!")
        return head

    if pos == 1:
        return delAtStart(head)

    current = head
    count = 1

    while current.next and count < pos - 1:
        current = current.next
        count += 1

    if current.next is None:
        print("Position out of range!")
        return head

    print(f"Deleted Node : {current.next.data}")

    current.next = current.next.next

    return head

---------------------------------------------------------------------------------------------------------------------------------------
    
# =====================================================
#              SEARCH OPERATION
# =====================================================

def searchNode(head, target):

    if head is None:
        print("Linked List is Empty!")
        return

    current = head
    position = 1

    while current:

        if current.data == target:
            print(f"Node found at position {position}")
            return

        current = current.next
        position += 1

    print("Node not found!")

---------------------------------------------------------------------------------------------------------------------------------------

# =====================================================
#              UPDATE OPERATION
# =====================================================

def updateNode(head, old_value, new_value):

    if head is None:
        print("Linked List is Empty!")
        return head

    current = head

    while current:

        if current.data == old_value:
            current.data = new_value
            print("Node updated successfully!")
            return head

        current = current.next

    print("Node not found!")
    return head

---------------------------------------------------------------------------------------------------------------------------------------

# =====================================================
#              COUNT NODES
# =====================================================

def countNode(head):

    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    print(f"Total Nodes : {count}")

    return count

---------------------------------------------------------------------------------------------------------------------------------------

# =====================================================
#              TRAVERSE LINKED LIST
# =====================================================

def traverseLL(head):

    if head is None:
        print("Linked List is Empty!")
        return

    current = head

    print("Linked List : ", end="")

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")

---------------------------------------------------------------------------------------------------------------------------------------

# =====================================================
#              REVERSE LINKED LIST
# =====================================================

def revLL(head):

    prev = None
    current = head

    while current:

        next_node = current.next
        current.next = prev

        prev = current
        current = next_node

    print("Linked List Reversed Successfully!")

    return prev

---------------------------------------------------------------------------------------------------------------------------------------

# =====================================================
#              MIDDLE NODE
# =====================================================

def middleNode(head):

    if head is None:
        print("Linked List is Empty!")
        return None

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

    print(f"Middle Node : {slow.data}")

    return slow

---------------------------------------------------------------------------------------------------------------------------------------

# =====================================================
#              DETECT CYCLE
# =====================================================

def detectCycle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            print("Cycle Detected!")
            return True

    print("No Cycle Exists!")

    return False

---------------------------------------------------------------------------------------------------------------------------------------

# =====================================================
#              FIND CYCLE START
# =====================================================

def cycleStart(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:

            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next

            print(f"Cycle starts at node : {slow.data}")

            return slow

    print("No Cycle Exists!")

    return None

---------------------------------------------------------------------------------------------------------------------------------------

# =====================================================
#              CREATE CYCLE (FOR TESTING)
# =====================================================

def createCycle(head, position):

    if head is None:
        print("Linked List is Empty!")
        return head

    cycle_node = None
    current = head
    count = 1

    while current.next:

        if count == position:
            cycle_node = current

        current = current.next
        count += 1

    if cycle_node is None:
        print("Invalid Position!")
        return head

    current.next = cycle_node

    print(f"Cycle created successfully at position {position}")

    return head

---------------------------------------------------------------------------------------------------------------------------------------

# =====================================================
#                 MAIN PROGRAM
# =====================================================

while True:

    try:
        choice = int(input("\nEnter your choice : "))

    except ValueError:
        print("Please enter a valid number!")
        continue

    # ===============================================

    if choice == 1:

        data = int(input("Enter node value : "))
        head = addAtStart(head, Node(data))

    # ===============================================

    elif choice == 2:

        data = int(input("Enter node value : "))
        head = addAtEnd(head, Node(data))

    # ===============================================

    elif choice == 3:

        data = int(input("Enter node value : "))
        pos = int(input("Enter position : "))

        head = addAtPos(head, Node(data), pos)

    # ===============================================

    elif choice == 4:

        head = delAtStart(head)

    # ===============================================

    elif choice == 5:

        head = delAtEnd(head)

    # ===============================================

    elif choice == 6:

        pos = int(input("Enter position : "))

        head = delAtPos(head, pos)

    # ===============================================

    elif choice == 7:

        old = int(input("Enter old value : "))
        new = int(input("Enter new value : "))

        head = updateNode(head, old, new)

    # ===============================================

    elif choice == 8:

        target = int(input("Enter value to search : "))

        searchNode(head, target)

    # ===============================================

    elif choice == 9:

        countNode(head)

    # ===============================================

    elif choice == 10:

        traverseLL(head)

    # ===============================================

    elif choice == 11:

        head = revLL(head)

    # ===============================================

    elif choice == 12:

        middleNode(head)

    # ===============================================

    elif choice == 13:

        detectCycle(head)

    # ===============================================

    elif choice == 14:

        cycleStart(head)

    # ===============================================

    elif choice == 15:

        pos = int(input("Create cycle at position : "))
        head = createCycle(head, pos)

    # ===============================================

    elif choice == 16:

        print("\nThank you for using the Linked List Program!")
        break

    # ===============================================

    else:

        print("Invalid Choice! Please select a valid option.")
-------------------------------------------------------------------------------------------------------------------------------------
