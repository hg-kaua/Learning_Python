class Block:
    
    def __init__(self, arr):
        self.arr = arr
        self.width = arr[0]
        self.length = arr[1]
        self.heigth= arr[2]
        
    def get_width(self):
        return self.width
    
    def get_length(self):
        return self.length
    
    def get_height(self):
        return self.heigth
    
    def get_volume(self):
        return self.width*self.heigth*self.length
    
    def get_surface_area(self):
        w, l, h = self.dimensions
        return 2 * (w * l + l * h + w * h)
        