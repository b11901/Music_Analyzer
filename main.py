import pygame
import easygui
from mutagen.mp3 import MP3
from buttons import *
import music
import analyzer

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Monospace',20)

#Defining screen parameters
screen_height = 600
screen_width = 900
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Music-Analyzer')

#Initialize all the buttons
btn_play = Play(screen,screen_width/2,screen_height-60,30)
btn_pause = Pause(screen,screen_width/2,screen_height-60,30)
btn_next = Next(screen,screen_width/2+60,screen_height-60,30)
btn_previous = Previous(screen,screen_width/2-60,screen_height-60,30)
btn_add = Add(screen,screen_width-60,screen_height-60,30)
#btn_volume = Circle(screen,700,300,35)

#Initialize the play bar
play_bar = Bar(screen,screen_width,screen_height)
play_bar_full = BarPlayed(screen,screen_width,screen_height)

#Initialize the beats
first_circle = Circle(screen,int(screen_width/2),200,20,width=0,color=(255,0,0))
second_circle = Circle(screen,int(screen_width/2),200,60,width=0,color=(0,255,0))
third_circle = Circle(screen,int(screen_width/2),200,80,width=0,color=(0,0,255))

audio = MP3('songs/second.mp3')
audio_length = audio.info.length


#Control Variables
paused = False
song_index = 0
files = ""
newSong = 1
played = 0
togglePlayaPause = 1
a = 0
b = 1024

pygame.mixer.music.load("songs/first.mp3")
#Game Loop
done = False
while not done:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    btn_next.draw()
    btn_previous.draw()
    btn_add.draw()

    if btn_add.click():
        files = easygui.fileopenbox(title="Select Music Files",filetypes="*.mp3",multiple=True)
        song_index = 0
        pygame.mixer.music.load(files[song_index])
        audio = MP3(files[song_index])
        audio_length  = audio.info.length

    #Display the name of the song
    try:
        song_name = files[song_index]
        song_name = ntpath.basename(song_name)
        song_name = song_name.split('.')
        song_name = song_name[0]
        ts_song_name = font.render(song_name, False, (255, 255, 255))
        screen.blit(ts_song_name,(400,400))
    except:
        pass

    if played:
        r1,r2,r3= analyzer.analyze("hello",newSong,a,b)
        if not paused:
            a = a+1024
            b = b+1024

    try:
        #Initialize the beats
        first_circle = Circle(screen,int(screen_width/2),200,r3,width=0,color=(242, 135, 48))
        second_circle = Circle(screen,int(screen_width/2),200,r2,width=0,color=(232, 20, 20))
        third_circle = Circle(screen,int(screen_width/2),200,r1,width=0,color=(255,255,255))

        print(r1,r2,r3)

        first_circle.draw()
        second_circle.draw()
        third_circle.draw()
    except NameError:
        pass

    if togglePlayaPause == 1:
        if btn_play.click():
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.play()

                played = 1
                togglePlayaPause = togglePlayaPause ^ 1
                pygame.time.wait(250)
                print("clicked")
                a = 0
                b = 1024
                paused = False

    else:        
        if btn_pause.click():
            pygame.mixer.music.pause()
            print("paused")

            paused = True
            newSong = 0
            played = 0
            togglePlayaPause = togglePlayaPause ^ 1
            pygame.time.wait(250)

    if togglePlayaPause == 1:
        btn_play.draw()
    else:
        btn_pause.draw()


    if btn_next.click() and song_index < len(files):
        song_index += 1
        print("Next:")
        print(song_index)
        pygame.mixer.music.load(files[song_index])
        pygame.mixer.music.play()
        audio = MP3(files[song_index])
        audio_length  = audio.info.length
        pause = False
        played = 1
        a = 0
        b = 1024
        pygame.time.wait(250)



    if btn_previous.click() and song_index > 0:
        song_index -= 1
        print("Prev:")
        print(song_index)
        pygame.mixer.music.load(files[song_index])
        pygame.mixer.music.play()
        audio = MP3(files[song_index])
        audio_length  = audio.info.length
        pause = False
        played = 1
        a = 0
        b = 1024
        pygame.time.wait(250)
    
   


    play_bar.draw()
    dx = int( int(pygame.mixer.music.get_pos()/1000) / audio_length * (screen_width-150) )
    play_bar_full.draw(dx)


    pygame.display.flip()
    pygame.display.update()
