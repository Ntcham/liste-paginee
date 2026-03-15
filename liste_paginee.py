class Page:
    
    def __init__(self, taille):
        # tableau pour stocker les éléments
        self.elements = [None] * taille
        # tableau pour savoir si une case est utilisée
        self.occupe = [False] * taille
        #  le pointeur vers la page suivante
        self.suivant = None
        
class ListePaginee:
    
    def __init__(self, taille_page):
        # taille d'une page
        self.taille_page = taille_page
        # première page
        self.premiere = None
        # nombre d'éléments
        self.nbr_elements = 0
        # nombre de pages
        self.nbr_pages = 0  
          
    def add(self, valeur):
        # si la liste est vide on crée la première page
        if self.premiere is None:
           self.premiere = Page(self.taille_page)
           self.nbr_pages += 1

        # on commence par la première page
        page = self.premiere

        # parcourir les pages
        while page is not None:

            # regarder toutes les cases de la page
            for i in range(self.taille_page):

                # si la case est libre
                if not page.occupe[i]:

                     # ajouter la valeur
                     page.elements[i] = valeur
                     page.occupe[i] = True

                     # mettre à jour le nombre d'éléments
                     self.nbr_elements += 1

                     return

            # passer à la page suivante
            if page.suivant is None:
               break

            page = page.suivant

        # si toutes les pages sont pleines on crée une nouvelle page
        nouvelle_page = Page(self.taille_page)
        self.nbr_pages += 1

         # relier la nouvelle page
        page.suivant = nouvelle_page

        # ajouter la valeur dans la première case
        nouvelle_page.elements[0] = valeur
        nouvelle_page.occupe[0] = True

        self.nbr_elements += 1 
        
    def search(self, valeur):
    
        resultats = []
        page = self.premiere
        numero_page = 1

        while page is not None:

            for i in range(self.taille_page):

                if page.occupe[i] and page.elements[i] == valeur:
                    resultats.append((numero_page, i))
            page = page.suivant
            numero_page += 1

        return resultats      
        
    def remove(self, numero_page, position):
    
        page = self.premiere
        compteur = 1
        # il faut trouver la bonne page
        while page is not None and compteur <numero_page:
            page = page.suivant
            compteur += 1

        if page is not None and page.occupe[position]:

            page.elements[position] = None
            page.occupe[position] = False

            self.nbr_elements -= 1  
    def compact(self):
    
        valeurs = []

        page = self.premiere

        # récupérer tous les éléments
        while page is not None:
            for i in range(self.taille_page):
                if page.occupe[i]:
                    valeurs.append(page.elements[i])

            page = page.suivant

        # réinitialiser la liste
        self.premiere = None
        self.nbr_elements = 0
        self.nbr_pages = 0

        # réinsérer les éléments
        for v in valeurs:
            self.add(v)     
    
    def elements(self):
        return self.nbr_elements      
    def pages(self):
        return self.nbr_pages       
if __name__ == "__main__":
    
    liste = ListePaginee(2)

    liste.add(10)
    liste.add(20)
    liste.add(30)
    liste.add(40)
    liste.add(50)
    
    print("Voici la liste créée:") 
    print(liste.pages())   
    print(liste.elements())
    print(liste.search(10))  
    liste.remove(1,0)
    liste.compact()
    print(liste.pages())
    print(liste.elements())