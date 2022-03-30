class Square:
    '''
    С помощью класса создаются квадраты карты.
    
    Результат команды `square_X = Square(3,2)` на схеме ниже:
        w i d t h
        1 2 3 4 5
        _ _ _ _ _
    h 1|* * * * *
    e 2|* * * * *
    i 3|* X * * *
    g 4|* * * * *
    h 5|* * * * *
    t 6|* * * * *

    '''

    def __init__(self, HEIGHT, WIDTH):
        self.__id = "".join(["h", str(HEIGHT), "w", str(WIDTH)])
        self.__height = HEIGHT
        self.__width = WIDTH
        self.__is_captured = False
        self.__neighbors = [] # список объектов класса Square

    def get_id(self):
        return self.__id

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_status(self):
        return self.__is_captured

    def set_status(self, capture_status):
        self.__is_captured = capture_status

    def get_neighbors(self, free_only=False):
        if free_only:
            free_neighbors = []
            for i in self.__neighbors:
                is_free = i.get_status() is False
                if is_free:
                    free_neighbors.append(i)
            return free_neighbors
        return self.__neighbors

    def set_neighbors(self, neighbors_list):
        '''
        Получает на вход список объектов класса Squares
        '''
        self.__neighbors = neighbors_list


class CampaignMap:

    def __init__(self, MAP_HEIGHT=1, MAP_WIDTH=1):

        def define_neighbors_ids(map_used, square_used):
        
            def get_neighbor_id(height, width):
                return "".join(["h", str(height), "w", str(width)])
        
            neighbors_list = []
        
            # в этом блоке проверяем наличие квадратов-соседей сверху и снизу
            height_min = 1
            height_max = map_used.height
            # т.к. ходим вверх и вниз, фиксируем значение по горизонтали 
            top_neighbor_width = bottom_neighbor_width = square_used.get_width()
            top_neighbor_height = square_used.get_height() - 1
            if top_neighbor_height >= height_min:
                top_neighbor_id = get_neighbor_id(top_neighbor_height, 
                                                  top_neighbor_width)
                neighbors_list.append(top_neighbor_id)
            bottom_neighbor_height = square_used.get_height() + 1
            if bottom_neighbor_height <= height_max:
                bottom_neighbor_id = get_neighbor_id(bottom_neighbor_height, 
                                                     bottom_neighbor_width)
                neighbors_list.append(bottom_neighbor_id)
        
            # в этом блоке проверяем наличие квадратов-соседей слева и справа
            width_min = 1
            width_max = map_used.width
            # т.к. ходим влево и вправо, фиксируем значение по вертикали
            left_neighbor_height = right_neighbor_height = square_used.get_height()
            left_neighbor_width = square_used.get_width() - 1
            if left_neighbor_width >= width_min:
                left_neighbor_id = get_neighbor_id(left_neighbor_height, 
                                                  left_neighbor_width)
                neighbors_list.append(left_neighbor_id)
            right_neighbor_width = square_used.get_width() + 1
            if right_neighbor_width <= width_max:
                right_neighbor_id = get_neighbor_id(right_neighbor_height, 
                                                  right_neighbor_width)
                neighbors_list.append(right_neighbor_id)
        
            return neighbors_list # список строковых констант

        def update_neighbors(map_used, square_used, map_grid_template):
            neighbors_ids = define_neighbors_ids(map_used, square_used)
            neighbors = []
            for i in neighbors_ids:
                new_neighbor = map_grid_template[i]
                neighbors.append(new_neighbor)
            square_used.set_neighbors(neighbors)

        def create_grid(map_used):
            grid_template = {}
            for height in range(1, map_used.height+1):
                for width in range(1, map_used.width+1):
                    new_square = Square(height, width)
                    grid_template[new_square.get_id()] = new_square
            # обновить список соседей у каждого квадрата на карте
            for square_id in grid_template:
                square = grid_template[square_id]
                update_neighbors(map_used, square, grid_template)
            return grid_template
                    

        self.height = MAP_HEIGHT
        self.width = MAP_WIDTH
        self.__grid = create_grid(self) # словарь для обращения к квадратам по id

    def access_square(self, square_id):
        return self.__grid[square_id]

    def get_squares_ids(self):
        '''for testing'''
        return set(self.grid.keys())

    def get_square_neighbors_ids(self, square_id):
        '''for testing'''
        square = self.grid[square_id]
        neighbors = square.get_neighbors()
        ids = set()
        for neighbor in neighbors:
            ids.add(neighbor.get_id())
        return ids
