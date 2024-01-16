### Pygame Pong Clone

This project is a simple implementation of the classic Pong game using Pygame. The primary objectives were to gain insights into how Pygame handles rendering, GUI building, class utilization, and state management.

#### Game Overview
The game features two players represented as white rectangles, each capable of vertical movement using the keys W/S for Player 1 and UP ARROW/DOWN ARROW for Player 2.
The ball exhibits continuous motion on the screen, dynamically responding to collisions with players. Upon colliding. the ball changes its x velocity (vx = -vx). Additionally, if the ball leaves the screen, the opposing player scores a point.
The game continues until one of the players achieves a score greater than a user-defined threshold. Upon reaching this threshold, the game concludes, and the victorious player is declared
