import pygame
import sys

pygame.init()   

from screen import*
from constans import*
from color import*
from object import*
from function import show , circle , cross

status = [None] * 9  # وضعیت خانه‌ها
turn = 'O'           # نوبت بازیکن

def check_winner(status):
    win_patterns = [
        [0,1,2], [3,4,5], [6,7,8],  # ردیف‌ها
        [0,3,6], [1,4,7], [2,5,8],  # ستون‌ها
        [0,4,8], [2,4,6]            # قطرها
    ]
    for pattern in win_patterns:
        a, b, c = pattern
        if status[a] and status[a] == status[b] == status[c]:
            return status[a]
    if all(status):
        return "Draw"
    return None

game_over = False
winner = None

while True:
    screen.fill(purple)
    show()

    for i in range(9):
        if status[i] == 'O':
            circle(i)
        elif status[i] == 'X':
            cross(i)

    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for sq in range(len(sq_list)):
                    if sq_list[sq].collidepoint(pos):
                        if not status[sq]:
                            status[sq] = turn
                            turn = 'X' if turn == 'O' else 'O'
                            winner = check_winner(status)
                            if winner:
                                game_over = True
    else:
        # نمایش پیام برنده یا مساوی
        font = pygame.font.SysFont(None, 60)
        if winner == "Draw":
            text = font.render("Draw!", True, (black))
        else:
            text = font.render(f"{winner} Wins!", True, (black))
        rect = text.get_rect(center=(200, 200))
        screen.blit(text, rect)
        # با کلیک دوباره بازی ریست شود
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                status = [None]*9
                turn = 'O'
                game_over = False
                winner = None

    pygame.display.update()


