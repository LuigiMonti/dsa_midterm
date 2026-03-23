from typing import Any, Optional, Iterator


class Node:
    def __init__(self, data: Any, song, album, artist) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None
        self.prev: Optional["Node"] = None
        self.playlist = {"song":song, 
                         "artist":artist,
                         "album": album}


    def __repr__(self) -> str:
        return f"[{self.data}. {self.playlist['song']} - {self.playlist['artist']} ({self.playlist['album']})]"
   

class LinkedList: 
    def __init__(self) -> None:
        self.start: Optional[Node] = None

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(repr(node))
        return '\n'.join(nodes)

    def __iter__(self) -> Iterator[Node]:
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __len__(self) -> int:
        length = 0
        for _ in self:
            length += 1
        return length

    def traverse(self) -> None:
        for node in self:
            print(node.data)

    def insert_at_beginning(self, element: Node) -> None:
        element.next = self.start
        element.prev = None
        if self.start is not None:
            self.start.prev = element
        self.start = element

    def insert_at_end(self, element: Node) -> None:
        if self.start is  None:
            self.start = element
        
        else:
            for current_node in self:
                pass
            current_node.next = element
            element.prev = current_node
            element.next = None

    def insert_after_node(self, element: Node, node_reference: Any) -> None:
    
        target = self.search(node_reference)
        if target is None:
                print(f"Node with data '{node_reference}' not found.")
                return
        element.next = target.next
        element.prev = target
        if target.next is not None:
            target.next.prev = element
        target.next = element

    def delete_node(self, element_data: Any) -> None:
       
        if self.start is None:
            print('Empty linked list..')
            return
        
        if self.start.data == element_data:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
            return
        
        target = self.search(element_data)
        if target is None:
           print(f"Node with data '{element_data}' not found.")
           return
       
        if target.prev is not None:
            target.prev.next = target.next

        if target.next is not None:
            target.next.prev = target.prev
        

        
    def search(self, element_data: Any) -> Optional[Node]:
        for node in self:
            if node.data == element_data:
                return node
        return None