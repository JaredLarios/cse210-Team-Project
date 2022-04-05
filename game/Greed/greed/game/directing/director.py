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
        self._points = 0
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
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)

        
        artifacts = cast.get_actors("artifacts")
        for arts in artifacts:
            velocity = self._art.falling()
            arts.set_velocity(velocity)

        bullets = cast.get_actors("bullets")
        for bullet in bullets:
            velocity = self._art.falling()
            bullet.set_velocity(velocity)
        
        
    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        bullets = cast.get_actors("bullets")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x)

        self._art.move_up(max_x, bullets)
        self._art.move_down(max_x, artifacts)
        
        for artifact in artifacts:
            
            if robot.get_position().equals(artifact.get_position()) or artifact.get_position().greater(max_y):
                cast.remove_actor("artifacts", artifact)
                if robot.get_position().equals(artifact.get_position()) :
                    self._points += 1 if artifact.get_text() == '*' else -1
                    print(self._points)

        if len(artifacts) < 10:
            cast.generate()
        banner.set_text(f'Score: {self._points}')
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()