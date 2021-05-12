"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

When the ball bounce the brick, the brick will disappear.
Each game only has three lives.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved


FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3

# BRICK_ROWS = 10        # Number of rows of bricks.
# BRICK_COLS = 10        # Number of columns of bricks.
graphics = BreakoutGraphics()
dx = graphics.get_dx()
dy = graphics.get_dy()
count = 0
score = 0


def main():
    onmouseclicked(handle_click)


def handle_click(event):
    """
    The animation that will happen after clicking the mouse.
    The ball will start to move.
    """
    global dy, dx, NUM_LIVES, count
    if count < NUM_LIVES:
        while True:
            graphics.find_ball()
            dy = graphics.get_dy()
            graphics.ball.move(dx, dy)
            # When the ball bump into left and right window, it will bounce
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window_width - graphics.ball_radius*2:
                dx = -dx
            # When the ball bump into the top of the window, it will bounce
            if graphics.ball.y <= 0:
                graphics.y_bounce()
            # When the ball bump into the bottom of the window, it will lose one life and add the ball back to the window
            if graphics.ball.y >= graphics.window_height - graphics.ball_radius*2:
                count += 1
                graphics.window.add(graphics.ball, (graphics.window_width-graphics.ball_radius)/2,
                                    (graphics.window_height-graphics.ball_radius)/2)
            # When the bricks are all gone or the player has lose three times, the game will break
            if score == graphics.brick_rows*graphics.brick_cols or count == NUM_LIVES:
                break
            pause(FRAME_RATE)


if __name__ == '__main__':
    main()
