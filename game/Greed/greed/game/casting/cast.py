import random

class Cast:
    """A collection of actors.

    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._actors = {}
        self._path = ""
        self._artifact = ""
        self._Point = ""
        self._Color = ""
        
    def add_actor(self, group, actor):
        """Adds an actor to the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to add.
        """
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        """Gets the actors in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The actors in the group.
        """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_all_actors(self):
        """Gets all of the actors in the cast.
        
        Returns:
            List: All of the actors in the cast.
        """
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_first_actor(self, group):
        """Gets the first actor in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first actor in the group.
        """
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result

    def remove_actor(self, group, actor):
        """Removes an actor from the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to remove.
        """
        if group in self._actors:
            self._actors[group].remove(actor)
    
    def create_artifact(self, path, Point, Artifact,Color):
        self._path = path
        self._Point = Point
        self._artifact = Artifact
        self._Color = Color
            # create the artifacts
        self.generate()
        
    def generate(self):

        COLS = 60
        ROWS = 120
        DEFAULT_ARTIFACTS = 10

        CELL_SIZE = 15
        FONT_SIZE = 15

        for n in range(DEFAULT_ARTIFACTS):
            # objects = [94, 79, 124]
            object = chr(79)

            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS / 8)
            position = self._Point(x, y)
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = self._Color(r, g, b)
            
            artifact = self._artifact()
            artifact.set_life(3)
            artifact.set_text(object)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)

            self.add_actor("artifacts", artifact)

        def shoot(self, x_position, y_position, character="alien"):
            COLS = 60
            ROWS = 120


            CELL_SIZE = 15
            FONT_SIZE = 15

            objects = 94 if character == "ship" else 124
            object = chr(objects)

            x = x_position
            y = y_position

            origin_position = self._Point(x,y)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = self._Color(r, g, b)
                
            artifact = self._artifact()
            artifact.set_text(object)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(origin_position)

        if object == chr(94):
            self.add_actor("rockets", artifact)
        elif object == chr(124):
            self.add_actor("lasers", artifact) 
            if object == chr(94):
                self.add_actor("rockets", artifact)
            elif object == chr(124):
                self.add_actor("lasers", artifact)
            else:
                artifact.set_life(3)
                self.add_actor("artifacts", artifact)