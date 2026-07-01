class NoMusic :

    def __init__(self, name) :

        self.name = name
        self.next = None

class Playlist :

    def __init__(self) :

        self.head = None
        self.size = 0

    def __len__(self) :

        return self.size
    
    def __iter__(self) :

        begin = self.head

        while begin is not None :
            yield begin.name
            begin = begin.next
    
    def inserir(self, nome_musica) :

        node = NoMusic(nome_musica)

        if self.head is None :

            self.head = node
        
        else :
            node.next = self.head
            self.head = node
            
        self.size += 1
    

minha_playlist = Playlist()

minha_playlist.inserir("Bohemian Rhapsody")
minha_playlist.inserir("Stairway to Heaven")
minha_playlist.inserir("Hotel California")

print(f"Total de músicas: {len(minha_playlist)}")

for musica in minha_playlist:
    print(f"Tocando agora: {musica}")




