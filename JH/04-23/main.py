'''
### 디버깅시 오류 정보 ###
 
# -1 : delete error
# -2 : search error
# -3 : print error


---------------------------------------------------------------------
노드 설정 -> Dnode (DoubleLinkedList)

(추가 : 만약 원형 링크드리스트를 구현한다고 한다면 delete_back or insert_back도 빠른 시간내에 구현이 가능)
 --> DoubleLinkedList와 가장 큰 차이점 기존O(n) -> O(1)작업으로 처리가능
LinkedList를 활용한 자료구조 : 트리, 해쉬테이블 등 기존 리스트 형식의 자료를 해결할 수 있음


insert_front : 노드를 앞에서 부터 추가
insert_index : 원하는 위치로 노드를 추가
delete_front : 제일 상단의 노드를 제거
search_data : 원하는 데이터를 찾아줌
delete_target : 원하는 데이터를 지워줌
print_nodes : 현재 연결된 LinkedList를 출력해줌( 디버깅 용도 )

'''

class Dnode:
    def __init__(self, data, prev = None, next = None): 
        self.data = data
        self.prev = prev
        self.next = next

class Snode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class DList:
    def __init__(self):
        self.head = None

    def insert_front(self, Dnode):
        if self.head == None:
            Dnode.next = None
            Dnode.prev = None
            self.head = Dnode
            return

        self.head.prev = Dnode
        Dnode.next = self.head
        Dnode.prev = None
        self.head = Dnode
        return

    def insert_index(self, index, Dnode):
        p = self.head
        if index == 0:
            self.insert_front(Dnode)
            return
        
        for _ in range(index):
            p = p.next

        p.prev.next = Dnode
        Dnode.prev = p.prev
        Dnode.next = p
        p.prev = Dnode
        return

    def print_index(self, index):
        p = self.head
        for _ in range(index):
            p = p.next
        return p.data

    def delete_front(self):
        target = self.head

        if target == None:
            return -1

        elif self.head.next == None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None
        return

    def search_data(self, data):
        if self.head == None:
            return -2
        p = self.head
        while p:
            if data == p.data:
                return p # p는 노드 정보
            p = p.next
        return -2

    def delete_target(self, target):
        p = self.head
        if p == None:
            return -1

        if p.data == target.data:
            self.delete_front()
            return

        while p.next != None:
            if p.data == target.data:
                p.next.prev = p.prev
                p.prev.next = p.next
            p = p.next
        return

    def print_nodes(self):
        p = self.head

        if p == None:
            print('비어있습니다.')
            return -3

        while p:
            if p.next != None:
                print(p.data, '- ', end = "")
            else:
                print(p.data)
                break
            p = p.next
        return


# 디버깅 용도
# node_1 = Dnode('데이터_1')
# node_2 = Dnode('데이터_2')

# LinkedList = DList()
# LinkedList.insert_front(node_1)
# LinkedList.print_nodes()

# LinkedList.insert_front(node_2)
# LinkedList.print_nodes()

# node_3 = Dnode('데이터_3')
# LinkedList.insert_front(node_3)

# node_4 = Dnode('데이터_4')
# LinkedList.insert_front(node_4)
# LinkedList.print_nodes()
# node_5 = Dnode('데이터_5')
# LinkedList.insert_index(2, node_4)
# LinkedList.print_nodes()

# LinkedList.insert_index(3, node_5)
# LinkedList.insert_index(2, node_4)
# LinkedList.print_nodes()
# LinkedList.delete_front()
# LinkedList.print_nodes()
# LinkedList.delete_front()
# LinkedList.print_nodes()



T = int(input())
for tc in range(1, 1+T):
    N, M, L = map(int, input().split())
    A = list(map(int, input().split()))
    A.reverse()
    LinkedList = DList()
    for data in A:
        temp = Dnode(data)
        LinkedList.insert_front(temp)

    for _ in range(M):
        index, data = map(int, input().split())
        temp = Dnode(data)
        LinkedList.insert_index(index, temp)

    # LinkedList.print_nodes()
    result = LinkedList.print_index(L)
    print('#{} {}'.format(tc, result))