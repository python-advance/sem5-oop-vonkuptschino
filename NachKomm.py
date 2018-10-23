class Autor(object):
	def __init__(self, Name):
		self.Name = Name
		

class Nachricht(object):

    def __init__(self, Autor, Zeitmark, Inhalt):
        self.Autor = Autor
        self.Zeitmark = Zeitmark
        self.Inhalt = Inhalt
 
class Kommentar(Nachricht):
    def _machenPublik(self, istPublik):
        self._istPublik = true

G = Autor("Gera")
post = Nachricht(G, "heute", "lala")

print(G.Name, post.Autor.Name)