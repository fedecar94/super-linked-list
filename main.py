class LinkedList:
    lenght = 0

    class Node:
        def __init__(self, data=None) -> None:
            self.value = data
            self.next = None

        def __str__(self) -> str:
            return str(self.value)

        def __gt__(self, other):
            return self.value > other.value

        def __ge__(self, other):
            return self.value >= other.value

        def __lt__(self, other):
            return self.value < other.value

        def __le__(self, other):
            return self.value <= other.value

        def __eq__(self, other):
            return self.value == other.value

    next: Node = None

    def append(self, new_value) -> None:
        new_node = LinkedList.Node(new_value)
        current_node = self

        while True:
            if not current_node.next:
                current_node.next = new_node
                break

            current_node = current_node.next

        self.lenght += 1

    def insert(self, new_value) -> None:
        new_node = LinkedList.Node(new_value)
        current_node = self

        while True:
            if current_node.next:
                if new_node <= current_node.next:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    break

            else:
                current_node.next = new_node
                break

            current_node = current_node.next

        self.lenght += 1

    def sort(self) -> None:
        new_list = LinkedList()

        for val in self:
            new_list.insert(val)

        self.next = new_list.next

    def __iter__(self):
        self.current_node = self.next
        return self

    def __next__(self) -> any:
        if not self.current_node:
            raise StopIteration
        current_node = self.current_node
        self.current_node = self.current_node.next
        return current_node.value

    def _check_index(self, index: int) -> int:
        if index > self.lenght:
            raise IndexError('No value for that index')

        if index < 0:
            index = self.lenght + index

        return index

    def _get_at_index(self, index: int) -> Node:
        pivot = 0
        current_node = self.next

        while pivot < index and current_node:
            current_node = current_node.next
            pivot += 1

        return current_node

    def __getitem__(self, index: int) -> any:
        index = self._check_index(index)
        return self._get_at_index(index).value

    def __setitem__(self, index: int, val) -> None:
        index = self._check_index(index)
        self._get_at_index(index).value = val

    def __str__(self) -> str:
        return str(' -> '.join([str(x) for x in self]))


if __name__ == '__main__':
    import random
    randomlist1 = LinkedList()
    randomlist2 = LinkedList()

    for i in range(0, 10):
        n = random.randint(1, 30)
        randomlist1.append(n)
        randomlist2.insert(n)

    print('1:       ', randomlist1)
    print('2:       ', randomlist2)

    randomlist1.sort()
    print('1 sorted:', randomlist1)
    print('1 index:', randomlist1[1])
    print('1 index:', randomlist1[-1])
    randomlist1[-1] = 40
    randomlist1[0] = 40
    print('1 index:', randomlist1[-1])
    print('1 sorted:', randomlist1)
