import time


def build_playlist(linked_list, canciones):
    for i, cancion in enumerate(canciones):
        node = Node(
            data=i + 1,
            song=cancion["song"],
            artist=cancion["artist"],
            album=cancion["album"]
        )
        linked_list.insert_at_end(node)

if __name__ == "__main__":
    from ll import LinkedList, Node
    from playlist import canciones

    ll = LinkedList()

    inicio = time.perf_counter()
    build_playlist(ll, canciones)
    fin = time.perf_counter()

    print(f"Tiempo de inserción: {fin - inicio:.6f} segundos")


