import pygame
import random
import copy

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
TILE_COLORS = {
    2: (236, 239, 241),
    4: (207, 216, 220),
    8: (176, 190, 197),
    16: (144, 164, 174),
    32: (120, 144, 156),
    64: (96, 125, 139),
    128: (84, 110, 122),
    256: (69, 90, 100),
    512: (55, 71, 79),
    1024: (38, 50, 56),
    2048: (29, 37, 41),
}

# Game settings
BOARD_SIZE = 4
TILE_SIZE = 100
MARGIN = 10
FONT_SIZE = 36

# 2048 게임 클래스 정의
class Game2048:
    # 초기화 메서드
    def __init__(self):
        pygame.init()  # pygame 초기화
        self.screen = pygame.display.set_mode((BOARD_SIZE * (TILE_SIZE + MARGIN) + MARGIN,
                                              BOARD_SIZE * (TILE_SIZE + MARGIN) + MARGIN))  # 게임 화면 생성
        pygame.display.set_caption('2048 Game')  # 게임 창 제목 설정
        self.clock = pygame.time.Clock()  # 게임 속도를 조절하기 위한 clock 객체 생성
        self.running = True  # 게임 진행 여부를 나타내는 플래그
        self.board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]  # 4x4 크기의 2D 리스트로 게임 보드 초기화
        self.spawn_tile()  # 초기에 2개의 타일을 랜덤한 위치에 생성
        self.spawn_tile()

    # 타일을 그리는 메서드
    def draw_tile(self, value, row, col):
        pygame.draw.rect(self.screen, TILE_COLORS.get(value, GRAY),
                         [col * (TILE_SIZE + MARGIN) + MARGIN,
                          row * (TILE_SIZE + MARGIN) + MARGIN,
                          TILE_SIZE, TILE_SIZE])  # 타일의 색상과 위치 지정

        font = pygame.font.Font(None, FONT_SIZE)  # 폰트 생성
        text = font.render(str(value), True, BLACK)  # 타일에 표시될 숫자 생성
        text_rect = text.get_rect(center=(col * (TILE_SIZE + MARGIN) + MARGIN + TILE_SIZE // 2,
                                          row * (TILE_SIZE + MARGIN) + MARGIN + TILE_SIZE // 2))  # 숫자를 타일 가운데로 위치 조정
        self.screen.blit(text, text_rect)  # 화면에 텍스트 그리기

    # 게임 보드 전체를 그리는 메서드
    def draw_board(self):
        self.screen.fill(WHITE)  # 화면을 흰색으로 채우기
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                value = self.board[row][col]
                if value != 0:
                    self.draw_tile(value, row, col)  # 0이 아닌 경우에만 타일을 그리기
        pygame.display.flip()  # 화면 갱신

    # 빈 셀 중 하나에 새로운 타일을 생성하는 메서드
    def spawn_tile(self):
        empty_cells = [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if self.board[i][j] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = 2 if random.random() < 0.9 else 4  # 90%의 확률로 2, 10%의 확률로 4 생성

    # 한 행 또는 열에서 타일을 합치는 메서드
    def merge_tiles(self, row):
        new_row = [val for val in row if val != 0]  # 0이 아닌 값들만 모아 새로운 리스트 생성
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2  # 인접한 같은 값의 타일이 있으면 합치기
                new_row[i + 1] = 0
        new_row = [val for val in new_row if val != 0] + [0] * (BOARD_SIZE - len(new_row))  # 0이 아닌 값들을 합친