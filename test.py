import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

benchy_path = "/Users/johnhoeksema/stls/_3DBenchy.stl"

your_mesh = mesh.Mesh.from_file(benchy_path, mode='binary')
