import pygame
pygame.init()

#set color with rgb
white,black,red = (255,255,255),(0,0,0),(255,0,0)

#set display
gameDisplay = pygame.display.set_mode((800,600))

#caption
pygame.display.set_caption("ChessBoard")

#beginning of logic
gameExit = False

lead_x = 20
lead_y = 20

#draw a rectangle
# gameDisplay.fill(white)
# pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,20,20])
# pygame.display.update()

#For loop for chessboard 
#Size of squares
size = 60

#board length, must be even
boardLength = 8
gameDisplay.fill(white)

cnt = 0
for i in range(1,boardLength+1):
    for z in range(1,boardLength+1):
        #check if current loop value is even
        if cnt % 2 == 0:
            pygame.draw.rect(gameDisplay, white,[size*z,size*i,size,size])
        else:
            pygame.draw.rect(gameDisplay, black, [size*z,size*i,size,size])
        cnt +=1
    #since theres an even number of squares go back one value
    cnt-=1
#Add a nice boarder
pygame.draw.rect(gameDisplay,black,[size,size,boardLength*size,boardLength*size],1)

pygame.display.update()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True


#quit from pygame & python
# pygame.quit()
# quit()