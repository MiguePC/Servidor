class Pratos:

    def __init__(self, nome, peso, ingredientes, preco, likes):
            self._nome = nome.title()
            self.peso = peso
            self.ingredientes = ingredientes.title()
            self._preco = preco
            self._likes = 0
        
    @property
    def nome (self):
        return self._nome

    @nome.setter
    def nome (self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def preco (self):
        return self._preco

    @nome.setter
    def nome (self, novo_preco):
        self._preco = novo_preco.title()

    @property
    def likes (self):
        return self._likes

    def dar_like (self):
        self._likes += 1

    def __str__(self):
        return (f'Prato Principal:{self._nome} tem {self.peso},'
        f' Ingredientes: {self.ingredientes}' '- Custa R${self._preco}'
        f' e teve um total de {self._likes} avaliações')

class Entradas(Pratos):
    def __init__(self, nome, peso, ingredientes, preco, likes, pessoas):
        super().__init__(nome, peso, ingredientes, preco, likes)
        self.pessoas = pessoas
    
    def __str__(self):
        return (f'Entrada: {self._nome}, Peso: {self.peso}, Ingredientes:' 
f'{self.ingredientes}, Preço R$ {self._preco}'
f' - Quantidade de avaliações {self._likes},' 
f'Serve {brusqueta.pessoas} pessoas')

class PratoPrincipal(Pratos):
    def __init__(self, nome, peso, ingredientes, preco, likes):
        super().__init__(nome, peso, ingredientes, preco, likes)

class Cardapio():
    def __init__(self, tipo, nome_pratos):
        self.tipo = tipo
        self._pratos = nome_pratos
    
    def __getitem__(self, item):
        return self._pratos[item]

    @property
    def listagem(self):
        return self._pratos
    
    def __len__(self):
        return len (self._pratos)

        #Elementos do Cardápio

#Entradas
brusqueta = Entradas('brusqueta marguerita', '125g', 
'pão italiano, tomate em cubos, mangericão e parmesão', '18,25', 'likes', '3')
caprese = Entradas('Salada Caprese', '150g', 'Rúcula, Mussarela de Bufala,'
' Tomate e Pesto', '23,50', '7', '2')
focaccia = Entradas ('Focaccias', '145g', 
'Farinha de Trigo, Ovos, Azeite de oliva e Temperos', '16,50', '3', '3')

#Pratos Principaos
lasanha = PratoPrincipal('lasanha bolonhesa', '650g', 
'massa, molhos bolonhesa, queijo mussarela', '45,30' , '')
gnocchi = PratoPrincipal ('Gnocchi Frito com Bisteca', '435g', 
'Gnocchi de Batata, Bisteca de Porco e Tempro Verde', '37,45', '')
risoto = PratoPrincipal ('Risoto de Parmesão com Mignon', '380g', 
'Arroz Arbório, Parmesão, Mignon em Cubos, Caldo e Temperos', '23', '')

brusqueta.dar_like()
brusqueta.dar_like()
caprese.dar_like()
focaccia.dar_like()
focaccia.dar_like()
focaccia.dar_like()
lasanha.dar_like()
lasanha.dar_like()
lasanha.dar_like()
lasanha.dar_like()
lasanha.dar_like()
gnocchi.dar_like()
risoto.dar_like()

lista_cardapio = [brusqueta, caprese, focaccia, lasanha, gnocchi, risoto]
cardapio_pratos = Cardapio ('Opções de entradas e prato principal', lista_cardapio)

print (f'Temos {len (cardapio_pratos)} opções no menu de hoje')

for Pratos in cardapio_pratos:
    print (Pratos)
