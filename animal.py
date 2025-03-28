class Animal:
    def __init__(self, nome, especie, som):
        self.nome = nome
        self.especie = especie
        self.som = som

    def __str__(self):
        return f"{self.nome} ({self.especie})"

def iniciar_jogo():
    animais = [
        Animal("Leão", "Felino", "Rugido"),
        Animal("Cachorro", "Canino", "Latido"),
        Animal("Gato", "Felino", "Miado"),
        Animal("Elefante", "Mamífero", "Barrito"),
        Animal("Pato", "Ave", "Quack")
    ]
    
    animal_escolhido = random.choice(animais)
    
    print("Adivinhe o animal!")
    tentativa = Animal(input("Nome: "), input("Espécie: "), input("Som: "))
    
    if (tentativa.nome.lower() == animal_escolhido.nome.lower() and
        tentativa.especie.lower() == animal_escolhido.especie.lower() and
        tentativa.som.lower() == animal_escolhido.som.lower()):
        print("Parabéns! Você acertou!")
    else:
        print(f"Errado! Era {animal_escolhido} que faz '{animal_escolhido.som}'.")

if __name__ == "__main__":
    iniciar_jogo()
