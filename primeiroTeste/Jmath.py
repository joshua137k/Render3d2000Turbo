import numpy as np
import math



def cross_product(edge1, edge2):
    return np.cross(edge1, edge2)

class base:

    def rotZ(self, pos):
        x = pos[0] * math.cos(self.rotation[2]) - pos[1] * math.sin(self.rotation[2])
        y = pos[1] * math.cos(self.rotation[2]) + pos[0] * math.sin(self.rotation[2])
        return np.array([x, y, pos[2]])

    def rotX(self, pos):
        y = pos[1] * math.cos(self.rotation[0]) - pos[2] * math.sin(self.rotation[0])
        z = pos[2] * math.cos(self.rotation[0]) + pos[1] * math.sin(self.rotation[0])
        return np.array([pos[0], y, z])

    def rotY(self, pos):
        x = pos[0] * math.cos(self.rotation[1]) + pos[2] * math.sin(self.rotation[1])
        z = pos[2] * math.cos(self.rotation[1]) - pos[0] * math.sin(self.rotation[1])
        return np.array([x, pos[1], z])

    def transform(self, vertex):
        pos = np.array(vertex) * 2
        pos = self.rotY(pos)
        pos = self.rotZ(pos)
        pos = self.rotX(pos)
        pos -= self.position
        return pos



class entity(base):
    def __init__(self,position,rotation):
        self.position = position
        self.rotation = rotation
        self.vertices=[]
        self.edges=[]
        self.faces = []
        self.face_colors = []





class Quad(entity):
    def __init__(self,position=[0,0,0],rotation=[0,0,0]):
        super().__init__(position,rotation)
        self.vertices = [[-1, 1, 0],
                         [1, 1, 0],
                         [1, -1, 0],
                         [-1, -1, 0]]
        self.edges = [(0, 1), (1, 2), (2, 3), (3, 0)]

        self.faces = [
            (0, 1, 2, 3)
        ]

    

class Tetrahedron(entity):
    def __init__(self, position=[0, 0, 0], rotation=[0, 0, 0]):
        super().__init__( position, rotation)
        # Definindo os vértices do Tetraedro
        self.vertices = [
            [1, 1, 1],
            [-1, -1, 1],
            [-1, 1, -1],
            [1, -1, -1]
        ]
        # Definindo as arestas do Tetraedro
        self.edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        # Definindo as faces do Tetraedro
        self.faces = [
            (0, 1, 2),
            (0, 1, 3),
            (0, 2, 3),
            (1, 2, 3)
        ]
        self.face_colors = [
            (255, 0, 0),    # Vermelho
            (0, 255, 0),    # Verde
            (0, 0, 255),    # Azul
            (255, 255, 0),  # Amarelo
        ]



class Cube(entity):
    def __init__(self,position=[0,0,0],rotation=[0,0,0]):
        super().__init__(position,rotation)
        self.vertices = [
            (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
            (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
        ]
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]
        self.faces = [
            (0, 1, 2, 3), (4, 5, 6, 7), (0, 3, 7, 4),
            (1, 2, 6, 5), (0, 1, 5, 4), (3, 2, 6, 7)
        ]
        self.face_colors = [
            (255, 0, 0),    # Vermelho
            (0, 255, 0),    # Verde
            (0, 0, 255),    # Azul
            (255, 255, 0),  # Amarelo
            (255, 165, 0),  # Laranja
            (255, 20, 147)  # Rosa
        ]

    
