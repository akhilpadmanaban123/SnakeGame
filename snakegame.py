
import pygame as py
import time
import random # for food


''' For the screen'''
py.init()  # initialises all of the pygame modules
displayy=py.display.set_mode((400,300))  # for creating a surface, it takes a tuple or list as a parameter
py.display.update() #updates the screen
py.display.set_caption("SNAKE GAME ")


'''For hitting boundary'''
display_width=400
display_height=300




'''colours'''
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
yellow=(255,255,102)



clock=py.time.Clock()
snake_block=10


'''score'''
def your_score(score):
    v=py.font.SysFont("comicsansms",15).render("Your Score :"+str(score),True, yellow)
    displayy.blit(v,[0,0])


'''length of snake'''
def our_snake(snake_block,snake_list):
    for i in snake_list:
        py.draw.rect(displayy,black,[i[0],i[1],snake_block,snake_block])

def message(msg, color):
    mesg=py.font.SysFont(None,50).render(msg,True,color)
    displayy.blit(mesg,[display_width/6,display_height/3])


#---------------------------------------------------------------------
def gameLoop():
    game_over=False
    game_close=False

    snakespeed = 10
    score=0

    x1 = display_width / 2
    y1 = display_height / 2

    ''''game coordinates'''
    x1_change, y1_change = 0, 0  # for updating the changed variables of the x and y coordinates


    snake_List=[]
    Length_of_snake=1
    '''for food'''
    foodx=round(random.randrange(0,display_width-snake_block)/10.0)*10.0
    foody=round(random.randrange(0,display_height-snake_block)/10.0)*10.0




    while not game_over:

        while game_close==True:
            displayy.fill(blue)
            message("You Lose! Press Q to quit or C to play again...")
            your_score(Length_of_snake-1)
            py.display.update()

            for i in py.event.get():
                    if i.type==py.KEYDOWN:
                        if i.key==py.K_q:
                            game_over=True
                            game_close=True
                        if i.key==py.K_c:
                            gameLoop()

        for i in py.event.get():
            '''When Pressed X button, it will quit'''
            if i.type==py.QUIT:
                game_over=True
            if i.type==py.KEYDOWN:
                if i.key==py.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                elif i.key==py.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif i.key==py.K_UP:
                    x1_change=0
                    y1_change=-snake_block
                elif i.key==py.K_DOWN:
                    x1_change=0
                    y1_change=snake_block

        if x1>=display_width or x1<0 or y1>display_height or y1<0:
                 game_over=True
        x1+=x1_change
        y1+=y1_change
        displayy.fill(blue)

        ''''snake length increasing'''
        py.draw.rect(displayy,green,[foodx,foody,snake_block,snake_block])
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if(len(snake_List)>Length_of_snake):
            del snake_List[0]

        for x in snake_List[:-1]:
            if x==snake_head:
                game_close=True
        our_snake(snake_block,snake_List)
        your_score(Length_of_snake-1)
        py.display.update()

        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0,display_width-snake_block)/10.0)*10.0
            foody=round(random.randrange(0,display_height-snake_block)/10.0)*10.0
            Length_of_snake+=1
            score+=1
            if score%5==0:
                snakespeed+=5
                ''' Increase speed'''
        clock.tick(snakespeed) #speed of snake


    py.quit()  # used to uninitialize everything
    quit()

#-----------------------------------------------------------
gameLoop()
