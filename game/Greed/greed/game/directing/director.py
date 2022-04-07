class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service, artifact, path, point, color):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._art = artifact
        self._lives = 0
        self._level = 0
        self._path = path
        self._point = point
        self._color = color
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the ship.
        
        Args:
            cast (Cast): The cast of actors.
        """
        ship = cast.get_first_actor("ships")
        velocity = self._keyboard_service.get_direction()
        ship.set_velocity(velocity)

        
        artifacts = cast.get_actors("artifacts")
        for arts in artifacts:
            velocity = self._art.falling()
            arts.set_velocity(velocity)

        rockets = cast.get_actors("rockets")
        for rocket in rockets:
            velocity = self._art.falling()
            rocket.set_velocity(velocity)

        lasers = cast.get_actors("lasers")
        for laser in lasers:
            velocity = self._art.falling()
            laser.set_velocity(velocity)
        
        
    def _do_updates(self, cast):
        """Updates the ship's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        ship = cast.get_first_actor("ships")
        artifacts = cast.get_actors("artifacts")
        rockets = cast.get_actors("rockets")
        lasers = cast.get_actors("lasers")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        ship.move_next(max_x)

        self._art.move_up(max_x, rockets)
        self._art.move_down(max_x, lasers)
        self._lives = ship.get_life()
        
        for laser in lasers:  
            if ship.get_position().equals(laser.get_position()) or laser.get_position().greater(max_y):
                cast.remove_actor("lasers", laser)
                if ship.get_position().equals(laser.get_position()) :
                    self._lives -= 1
                    ship.set_life(self._lives)
                    print(ship.get_life())
        
        for rocket in rockets:
            for artifact in artifacts:  
                if artifact.get_position().equals(rocket.get_position()):
                    cast.remove_actor("rockets", rocket)
                    if artifact.get_position().equals(rocket.get_position() or laser.get_position().greater(-max_y)) :
                        alien_life = artifact.get_life() 
                        alien_life -= 1
                        artifact.set_life(alien_life)
                        print(f"Alien Life: {artifact.get_life()}")
                    
                    if artifact.get_life() <= 0:
                        cast.remove_actor("artifacts", artifact)

        if len(lasers) < 5:
            cast.generate()

        banner.set_text(f'Lives: {self._lives}  Level: {self._level}')
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()