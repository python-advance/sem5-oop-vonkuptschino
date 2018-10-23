class Autor(object):
	def __init__(self, Name):
		self.Name = Name
		
class Nachricht(object):

    def __init__(self, Autor, Zeitmark, Inhalt):
        self.Autor = Autor
        self.Zeitmark = Zeitmark
        self.Inhalt = Inhalt

    def druckenAutor(self):
    	print(f'Autor: {self.Autor.Name}')

    def druckerInhalt(self):
    	print(f'Inhalt: {self.Inhalt}')

class Kommentar(Nachricht):

	def __init__(self):
		self._istPublik = 1

	istPublik = property()

	@istPublik.getter
	def istPublik(self):
		return self._istPublik

	@istPublik.setter
	def istPublik(self, value):
	    self._istPublik = value

G = Autor("Gera")
post = Nachricht(G, "heute", "lala")

print(G.Name, post.Autor.Name)
post.druckenAutor()
post.druckerInhalt()