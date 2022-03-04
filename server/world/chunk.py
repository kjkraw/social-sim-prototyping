class Chunk:
    x_dim = 64  # North-south
    y_dim = 64  # East-west
    z_dim = 64  # Elevation
    horizontal_size = x_dim * y_dim
    chunk_size = horizontal_size * z_dim

    @classmethod
    def empty_chunk(cls):
        return [0 for _ in range(cls.chunk_size)]

    @classmethod
    def get_voxel_idx(cls, x, y, z):
        return x + y + z * cls.horizontal_size

    @classmethod
    def get_local_coords(cls, g_x, g_y, z):
        return g_x % cls.x_dim, g_y % cls.y_dim, z

    def __init__(self):
        self.voxels = self.empty_chunk()

    def get_voxel(self, x, y, z):
        return self.voxels[self.get_voxel_idx(x, y, z)]

    def set_voxel(self, x, y, z, voxel):
        self.voxels[self.get_voxel_idx(x, y, z)] = voxel
