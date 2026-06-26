class NoMusica :

    def __init__(self, data) :

        self.data = data
        self.next = None

class Playlist :

    def __init__(self) :

        self.head = None
        self.size = 0

    def __str__(self) :
        
        current = self.head
        musics = []

        while current is not None :
            musics.append(current.data)
            current = current.next

        return ' -> '.join(musics)
    
    def __iter__(self) :

        current = self.head

        while current is not None :
            yield current.data
            current = current.next

    def __len__(self) :
        return self.size

    def add(self, song) :
            
        new = NoMusica(song)

        if self.head is not None :

            new.next = self.head
        
        self.head = new
        self.size += 1
                

musicas = Playlist()
musicas.add('Deixe-me ir')
musicas.add('Yellow')
musicas.add('Photograph')

print(musicas)
print(len(musicas))

for musica in musicas :
    print(musica)