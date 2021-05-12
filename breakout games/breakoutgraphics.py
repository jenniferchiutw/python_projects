"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

These code manage the basic setting of the game, including putting the ball, bricks, paddle into the window,
and find out whether the ball has bumped into the bricks.
"""
from campy.gui.events.timer import pause
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.
score = BRICK_ROWS*BRICK_COLS


class BreakoutGraphics:
    # Constructor
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        self.paddle_width = paddle_width
        self.ball_radius = ball_radius
        self.brick_rows = BRICK_ROWS
        self.brick_cols = BRICK_COLS

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window_width-paddle_width)/2, (self.window_height-paddle_offset))

        # Center a filled ball in the graphical window.
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window_width-ball_radius)/2, (self.window_height-ball_radius)/2 )

        # Default initial velocity for the ball.
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if (random.random() > 0.5):
            self.__dx = -self.__dx

        # Initialize our mouse listeners.
        onmousemoved(self.handle_move)

        # Draw bricks.
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height, x=(brick_width + brick_spacing) * j,
                                    y=brick_offset + (+brick_height + brick_spacing) * i)
                self.brick.filled = True
                if i == 0 or i == 1:
                    self.brick.color = 'red'
                    self.brick.fill_color = 'red'
                    self.window.add(self.brick)
                if i == 2 or i == 3:
                    self.brick.color = 'gold'
                    self.brick.fill_color = 'gold'
                    self.window.add(self.brick)
                if i == 4 or i == 5:
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                    self.window.add(self.brick)
                if i == 6 or i == 7:
                    self.brick.color = 'green'
                    self.brick.fill_color = 'green'
                    self.window.add(self.brick)
                if i == 8 or i == 9:
                    self.brick.color = 'blue'
                    self.brick.fill_color = 'blue'
                    self.window.add(self.brick)

    # To control the paddle to move only in the window
    def handle_move(self, event):
        self.paddle.x = event.x-PADDLE_WIDTH/2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x >= self.window_width - self.paddle_width:
            self.paddle.x = self.window_width - self.paddle_width

    # To let the ball bounce when bumping into things
    def y_bounce(self):
        self.__dy = -self.__dy

    # To find out whether the ball is bumping into things
    def find_ball(self):
        global score
        left_up = self.window.get_object_at(self.ball.x, self.ball.y)
        left_down = self.window.get_object_at(self.ball.x, self.ball.y+self.ball_radius*2)
        right_up = self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y)
        right_down = self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y+self.ball_radius*2)
        # If the left-down and right-down side of the ball is paddle, bounce
        if left_down or right_down is self.paddle:
            self.y_bounce()
        # If the left-up side of the ball is brick, remove the brick and bounce
        if left_up is not None and left_up is not self.paddle:
            self.window.remove(left_up)
            score += 1
            self.y_bounce()
        # If the right-up side of the ball is brick, remove the brick and bounce
        if right_up is not None and left_up is not self.paddle:
            self.window.remove(right_up)
            score += 1
            self.y_bounce()

    # Let the breakout.py file get the velocity of x
    def get_dx(self):
        return self.__dx

    # Let the breakout.py file get the velocity of y
    def get_dy(self):
        return self.__dy



