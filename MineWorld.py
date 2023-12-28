import numpy as np

def generate_minecraft_world(size):
    # Inicializando o mundo com zeros
    world = np.zeros(size, dtype=bool)

    # Parâmetros para o ruído Perlin
    scale = 0.1  # Quanto menor, mais 'liso' será o terreno
    threshold = 0.5  # Limiar para decidir se um bloco é sólido ou vazio

    # Gerando o mundo
    for x in range(size[0]):
        for y in range(size[1]):
            for z in range(size[2]):
                # Calculando um valor de ruído Perlin simples
                noise_value = np.sin(x * scale) * np.cos(y * scale) * np.sin(z * scale)
                # Se o valor de ruído for maior que o limiar, marcamos como um bloco sólido
                world[x, y, z] = noise_value > threshold

    # Retornando as coordenadas dos blocos sólidos
    solid_blocks = np.argwhere(world)
    return solid_blocks

# Gerando um mini mundo Minecraft de 20x20x20
minecraft_world = generate_minecraft_world((20, 20, 20))
f=open("cords.txt","w")
for i in minecraft_world:
	f.write(f"({i[0]},{i[1]},{i[2]}),")
f.close()