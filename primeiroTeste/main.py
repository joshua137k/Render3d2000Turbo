import pygame
from Jmath import *
import numpy as np

# Initialize Pygame
pygame.init()

# Constants

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Parâmetros da câmera


# Create a Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("3D Projection with Pygame")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK=(0,0,0)
lst=[WHITE,RED,BLUE,WHITE,RED,BLUE,WHITE]






class Projection(base):
    def __init__(self):
        self.position = [0,0,-40]
        self.rotation = [0,0,0]
        self.camera_speed = 0.1
        self.camera_rot_speed = 0.001
        self.clip_distance = 10  # Distância de corte
        self.FOV = 314


    def projection(self, pos):
        pos = np.array(pos) - self.position
        pos = self.rotY(pos)
        pos = self.rotZ(pos)
        pos = self.rotX(pos)

        if np.linalg.norm(self.position - pos) > 500:
            return None
        if pos[2] <0:
            return None
        elif pos[2] == 0:
            pos[2] = 1e-5  # Prevent division by zero

        scale_factor = self.FOV / pos[2]
        x = pos[0] * scale_factor + SCREEN_WIDTH // 2
        y = pos[1] * scale_factor + SCREEN_HEIGHT // 2
        return (round(x), round(y))


    def draw_entities(self, entities):
            faces = []
            face_distances = []

            for entity in entities:
                for idx,face in enumerate(entity.faces):
                    face_vertices = [self.projection(entity.transform(entity.vertices[i])) for i in face]
                    if None not in face_vertices:
                        # Calcula a distância média da face
                        face_center = np.mean([entity.transform(entity.vertices[i]) for i in face], axis=0)
                        distance = np.linalg.norm(face_center - np.array(self.position))
                        faces.append((face_vertices, entity.face_colors[idx]))
                        face_distances.append((distance, len(faces)-1))

            # Ordena as faces pela distância (as mais próximas primeiro)
            face_distances.sort(key=lambda x: -x[0])

            # Desenha as faces na ordem de proximidade
            for _, face_idx in face_distances:
                pygame.draw.polygon(screen, faces[face_idx][1], faces[face_idx][0])
proj=Projection()


def main():
    #
    
    cubes=[Cube([i*4,-30,j*4],[0,0,0]) for i in range(5) for j in range(5)]
    cubes.append(Tetrahedron([10,-20,10],[0,0,0]))
    running = True
    print("ok")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            proj.position[0] -= proj.camera_speed
        if keys[pygame.K_RIGHT]:
            proj.position[0] += proj.camera_speed
        if keys[pygame.K_UP]:
            proj.position[1] += proj.camera_speed
        if keys[pygame.K_DOWN]:
            proj.position[1] -= proj.camera_speed
        if keys[pygame.K_w]:
            proj.position[2] += proj.camera_speed
        if keys[pygame.K_s]:
            proj.position[2] -= proj.camera_speed
        if keys[pygame.K_a]:
             proj.rotation[1]+= proj.camera_rot_speed
        if keys[pygame.K_d]:
             proj.rotation[1]-= proj.camera_rot_speed

        screen.fill((20, 100,100))  # Clear the screen

        proj.draw_entities(cubes)
        cubes[len(cubes)-1].rotation[1]+=0.01

        pygame.display.flip()  # Update the display



    pygame.quit()


if __name__ == "__main__":
    main()
