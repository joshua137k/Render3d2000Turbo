from const import *
import pywavefront




class Cube:
	vertices = [
			[-1, -1, -1],
			[1, -1, -1],
			[1, 1, -1],
			[-1, 1, -1],
			[-1, -1, 1],
			[1, -1, 1],
			[1, 1, 1],
			[-1, 1, 1]
			]

	edges = [
			(0, 1),
			(1, 2),
			(2, 3),
			(3, 0),
			(4, 5),
			(5, 6),
			(6, 7),
			(7, 4),
			(0, 4),
			(1, 5),
			(2, 6),
			(3, 7)
			]

	faces = [
			(0, 1, 2, 3),  # Fundo
			(4, 7, 6, 5),  # Topo
			(0, 4, 5, 1),  # Lateral esquerda
			(2, 6, 7, 3),  # Lateral direita
			(0, 3, 7, 4),  # Frente
			(1, 5, 6, 2)   # Atrás
	]	
	colors = ORANGE,GRAY,GREEN,YELLOW,RED,BLUE
	def __init__(self,pos=(0,0,0),rot=(0,0,0)):
		self.pos=list(pos)
		self.rot=list(rot)
		self.verts=[]
		self.update()


	def update(self):
		x, y, z = self.pos
		rx, ry, rz = self.rot

		self.verts = [self._rotate_point((X, Y, Z), rx, ry, rz) for X, Y, Z in self.vertices]
		self.verts = [(x*2 + X, y*2 + Y, z*2 + Z) for X, Y, Z in self.verts]


	def _rotate_point(self, point, rx, ry, rz):
		point = rotateX(point, rx)
		point = rotateY(point, ry)
		point = rotateZ(point, rz)
		return point

	
	def get_verts(self,cam_pos,cam_rot):
		vert_list=[]; screen_coords=[]
		for x,y,z in self.verts:
			
			x-=cam_pos[0]
			y-=cam_pos[1]
			z-=cam_pos[2]
			

			x,z = rotate2d((x,z),cam_rot[1])
			y,z = rotate2d((y,z),cam_rot[0])
			vert_list+=[(x,y,z)]

			f = 200/z
			x,y = x*f,y*f
			screen_coords+=[(cx+int(x),cy+int(y))]
		return vert_list,screen_coords


class Tetrahedron:
	vertices = [
		[1, 1, 1],
		[-1, -1, 1],
		[-1, 1, -1],
		[1, -1, -1]
	]
	# Definindo as arestas do Tetraedro

	edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
	# Definindo as faces do Tetraedro
	faces = [
		(0, 1, 2),
		(0, 1, 3),
		(0, 2, 3),
		(1, 2, 3)
	]
	colors = [
		(255, 0, 0),    # Vermelho
		(0, 255, 0),    # Verde
		(0, 0, 255),    # Azul
		(255, 255, 0),  # Amarelo
	]

	def __init__(self, pos=(0, 0, 0),rot=(0,0,0)):
		self.pos=list(pos)
		self.rot=list(rot)
		self.verts=[]
		self.update()



	def update(self):
		x, y, z = self.pos
		rx, ry, rz = self.rot

		self.verts = [self._rotate_point((X, Y, Z), rx, ry, rz) for X, Y, Z in self.vertices]
		self.verts = [(x + X, y + Y, z + Z) for X, Y, Z in self.verts]

	def _rotate_point(self, point, rx, ry, rz):
		point = rotateX(point, rx)
		point = rotateY(point, ry)
		point = rotateZ(point, rz)
		return point

	def get_verts(self,cam_pos,cam_rot):
		vert_list=[]; screen_coords=[]
		for x,y,z in self.verts:
			x-=cam_pos[0]
			y-=cam_pos[1]
			z-=cam_pos[2]

			x,z = rotate2d((x,z),cam_rot[1])
			y,z = rotate2d((y,z),cam_rot[0])
			vert_list+=[(x,y,z)]

			f = 200/z
			x,y = x*f,y*f
			screen_coords+=[(cx+int(x),cy+int(y))]
		return vert_list,screen_coords


        # Definindo os vértices do Tetraedro


class Model3D:
	def __init__(self, file_path,pos,rot):
		self.vertices, self.faces = self.load_obj(file_path)
		self.pos=list(pos)
		self.rot=list(rot)
		self.colors=[WHITE for i in self.faces]
		self.verts=[]
		self.update()

	def load_obj(self,caminho_arquivo):
	    vertices = []
	    faces = []
	    with open(caminho_arquivo, 'r') as arquivo:
	        for linha in arquivo:
	            partes = linha.strip().split()
	            if partes:
	                if partes[0] == 'v':
	                    vertices.append([float(partes[1]), float(partes[2]), float(partes[3])])
	                elif partes[0] == 'f':
	                    # Extrai os índices dos vértices que formam a face
	                    # Nota: Os índices no arquivo .obj começam em 1, mas em Python começam em 0
	                    indice_vertices = [int(parte.split('/')[0]) - 1 for parte in partes[1:]]
	                    faces.append(indice_vertices)
	    return vertices, faces


		

	def update(self):
		x, y, z = self.pos
		rx, ry, rz = self.rot

		self.verts = [self._rotate_point((X, Y, Z), rx, ry, rz) for X, Y, Z in self.vertices]
		self.verts = [(x*2 + X, y*2 + Y, z*2 + Z) for X, Y, Z in self.verts]

	def _rotate_point(self, point, rx, ry, rz):
		point = rotateX(point, rx)
		point = rotateY(point, ry)
		point = rotateZ(point, rz)
		return point



	def get_verts(self,cam_pos,cam_rot):
		vert_list=[]; screen_coords=[]
		for x,y,z in self.verts:
			
			x-=cam_pos[0]
			y-=cam_pos[1]
			z-=cam_pos[2]
			

			x,z = rotate2d((x,z),cam_rot[1])
			y,z = rotate2d((y,z),cam_rot[0])
			vert_list+=[(x,y,z)]

			f = 200/z
			x,y = x*f,y*f
			screen_coords+=[(cx+int(x),cy+int(y))]
		return vert_list,screen_coords
