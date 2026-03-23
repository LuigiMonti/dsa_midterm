from ll import LinkedList, Node
from playlist import canciones
from memory_profiler import profile
import os


#@profile
def build_playlist(linked_list, canciones):
    for i, cancion in enumerate(canciones):
        node = Node(data=i+1, song=cancion["song"], artist=cancion["artist"], album=cancion["album"])
        linked_list.insert_at_end(node)

ll = LinkedList()
build_playlist(ll, canciones)

current = ll.start

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show(node):
    clear()
    print("=" * 45)
    print("       🎵  PLAYLIST PLAYER")
    print("=" * 45)
    print(f"  #{node.data:02d}  {node.playlist['song']}")
    print(f"        {node.playlist['artist']}")
    print(f"        {node.playlist['album']}")
    print("=" * 45)
    prev_name = node.prev.playlist['song'] if node.prev else "---"
    next_name = node.next.playlist['song'] if node.next else "---"
    print(f"  ⏮  {prev_name[:25]}")
    print(f"  ⏭  {next_name[:25]}")
    print("=" * 45)
    print("[sh] shuffle ")
    print("  [n] siguiente  [p] anterior  ")
    print("  [s] buscar     [q] salir")
    print("=" * 45)

while True:
    show(current)
    cmd = input("  > ").strip().lower()

    if cmd == 'n':
        result = ll.next_node(current)  
        if result:                       
            current = result             
        else:
            input("  Ya estás en la última canción. Enter para continuar...")

    elif cmd == 'p':
        result = ll.prev_node(current)  
        if result:                       
            current = result             
        else:
            input("  Ya estás en la primera canción. Enter para continuar...")


    elif cmd == 'sh':                                          
        ll.toggle_shuffle(current)                             
        estado = "ON 🔀" if ll.shuffle else "OFF"              
        input(f"  Shuffle {estado}. Enter para continuar...")  

    elif cmd == 's':
        query = input("  Número de canción: ").strip()
        if query.isdigit():
            result = ll.search(int(query))
            if result:
                current = result
            else:
                input("  Canción no encontrada. Enter para continuar...")

    elif cmd == 'q':
        clear()
        print("  Hasta luego 👋")
        break

