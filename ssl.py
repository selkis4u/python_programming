class Node:

    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.link is not None:
            curr = curr.link
        curr.link = new_node

    def insert_after(self, target_data, data):
        curr = self.head
        while curr is not None:
            if curr.data == target_data:
                new_node = Node(data,curr.link)
                curr.link = new_node
                return True
            curr = curr.link
        return False

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.link
            curr.link = prev
            prev = curr
            curr = next_node
        self.head = prev

    def delete_last(self):
        if self.head is None:
            return None
        if self.head.link is None:
            data = self.head.data
            self.head = None
            return data
        prev = self.head
        curr = self.head.link
        while curr.link is not None:
            prev = curr
            curr = curr.link
        prev.link = None
        return curr.data


    def __str__(self):
        elements = []
        curr = self.head
        while curr is not None:
            elements.append(str(curr.data))
            curr = curr.link
        return(f"({', '.join(elements)})")

if __name__ == "__main__":
    sll = LinkedList()

print("1. 빈 리스트에 노드3개를 넣습니다.")
for item in ["월", "수", "일"]:
    sll.append(item)
print(f"L= {sll}")

print("2. '수'뒤에 '금' 넣기")
sll.insert_after("수", "금")
print(f"L= {sll}")

print("3. 리스트를 역순으로 바꾸기")
sll.reverse()
print(f"L= {sll}")

print("4. 리스트의 마지막을 제거합니다.")
sll.delete_last()
print(f"L= {sll}")
sll.delete_last()
print(f"L= {sll}")
