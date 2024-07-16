l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
dim = l*a
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(l, a, dim))
print("Para pintar essa parede você precisará de {}l de tinta.".format(dim/2))