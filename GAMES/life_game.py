import pygame
import sys

# Konfigurace
CELL_SIZE = 20
GRID_WIDTH = 40
GRID_HEIGHT = 30
PANEL_HEIGHT = 80
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT + PANEL_HEIGHT
FPS = 10

# Barvy
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)
BLUE = (0, 150, 255)
RED = (200, 50, 50)
DARK_GRAY = (40, 40, 40)


class Button:
    def __init__(self, name, x, y, width=80, color=GRAY):
        self.name = name
        self.rect = pygame.Rect(x, y, width, 30)
        self.color = color

    def draw(self, screen, font, active=False):
        pygame.draw.rect(screen, BLUE if active else self.color, self.rect)
        text = font.render(self.name.capitalize(), True, WHITE)
        screen.blit(text, (self.rect.x + 10, self.rect.y + 5))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]

    def toggle_cell(self, x, y):
        self.cells[y][x] = 1 - self.cells[y][x]

    def clear(self):
        self.cells = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def draw(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                color = GREEN if self.cells[y][x] else BLACK
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, DARK_GRAY, rect, 1)

    def update(self):
        new = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                if self.cells[y][x] == 1 and neighbors in (2, 3):
                    new[y][x] = 1
                elif self.cells[y][x] == 0 and neighbors == 3:
                    new[y][x] = 1
        self.cells = new

    def count_neighbors(self, x, y):
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    count += self.cells[ny][nx]
        return count

    def place_pattern(self, pattern, x, y):
        for dx, dy in pattern:
            gx, gy = x + dx, y + dy
            if 0 <= gx < self.width and 0 <= gy < self.height:
                self.cells[gy][gx] = 1


class PatternManager:
    def __init__(self):
        self.patterns = {
            "block": [(0, 0), (1, 0), (0, 1), (1, 1)],
            "blinker": [(0, 0), (1, 0), (2, 0)],
            "glider": [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)],
        }
        self.selected = "glider"

    def get_selected_pattern(self):
        return self.patterns[self.selected]

    def select(self, name):
        if name in self.patterns:
            self.selected = name


class GameOfLife:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Hra života - OOP verze")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)

        self.grid = Grid(GRID_WIDTH, GRID_HEIGHT)
        self.patterns = PatternManager()
        self.simulating = False
        self.buttons = self.create_buttons()

    def create_buttons(self):
        buttons = []
        x = 10
        for pattern in self.patterns.patterns:
            buttons.append(Button(pattern, x, CELL_SIZE * GRID_HEIGHT + 10))
            x += 90
        buttons.append(Button("start", x, CELL_SIZE * GRID_HEIGHT + 10, color=GREEN))
        x += 90
        buttons.append(Button("stop", x, CELL_SIZE * GRID_HEIGHT + 10, color=RED))
        x += 90
        buttons.append(Button("clear", x, CELL_SIZE * GRID_HEIGHT + 10, color=GRAY))
        return buttons

    def run(self):
        running = True
        while running:
            self.screen.fill(BLACK)
            self.grid.draw(self.screen)
            self.draw_ui()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if my < CELL_SIZE * GRID_HEIGHT:
                        gx, gy = mx // CELL_SIZE, my // CELL_SIZE
                        if event.button == 1:
                            self.grid.toggle_cell(gx, gy)
                        elif event.button == 3:
                            self.grid.place_pattern(self.patterns.get_selected_pattern(), gx, gy)
                    else:
                        for btn in self.buttons:
                            if btn.is_clicked((mx, my)):
                                self.handle_button(btn.name)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.simulating = not self.simulating
                    elif event.key == pygame.K_c:
                        self.grid.clear()

            if self.simulating:
                self.grid.update()

            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def handle_button(self, name):
        if name in self.patterns.patterns:
            self.patterns.select(name)
        elif name == "start":
            self.simulating = True
        elif name == "stop":
            self.simulating = False
        elif name == "clear":
            self.grid.clear()

    def draw_ui(self):
        for btn in self.buttons:
            active = btn.name == self.patterns.selected if btn.name in self.patterns.patterns else False
            btn.draw(self.screen, self.font, active=active)


if __name__ == "__main__":
    game = GameOfLife()
    game.run()