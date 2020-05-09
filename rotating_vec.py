import pygame
from vector_class import vector
import math

class rotvec():
    def __init__(self,screen,centre,amplitude,frequency,far_end_draw = False,offset = 0,time = 0):
        self.screen = screen
        self.centre = centre
        self.amplitude = amplitude
        self.frequency = frequency
        self.time = time
        self.points_coll = []
        self.far_end = None
        self.far_end_draw = far_end_draw
        self.offset = offset

    def angle(self):
        calc_angle = self.time * 2* math.pi* self.frequency
        if calc_angle >=2*math.pi:
            self.time = (calc_angle-2*math.pi)/(2*math.pi*self.frequency)
        return math.degrees(calc_angle)+self.offset

    def draw_me(self):
        self.far_end = self.centre.protrude(self.amplitude,self.angle())
        pygame.draw.line(self.screen,(255,0,0),(self.centre.x,self.centre.y),(self.far_end.x,self.far_end.y),2)
        pygame.draw.circle(self.screen,(0,0,0),(int(self.centre.x),int(self.centre.y)),5)
        if self.far_end_draw:
            self.points_coll.append(self.far_end)
            for i in range(2,len(self.points_coll)):
                pygame.draw.line(self.screen,(0,255,0),(self.points_coll[i-1].x,self.points_coll[i-1].y),(self.points_coll[i].x,self.points_coll[i].y),2)
        
    def update_me(self):
        self.time+=1
    
    
class epicycles():
    def __init__(self,centre,screen,amplitudes):
        self.centre = centre
        self.screen = screen
        self.amplitudes = amplitudes
        self.rotvecs = []
        self.size = len(amplitudes)

    def assign_params(self):
        for i in range(self.size):
            draw = True if i==0 else False
            if not isinstance(self.amplitudes[i],complex):
                temp = rotvec(self.screen,self.centre,self.amplitudes[i]/self.size,i/self.size,far_end_draw = draw)
            else:
                temp_vec = vector(self.amplitudes[i].real,self.amplitudes[i].imag)
                temp = rotvec(self.screen,self.centre,temp_vec.magnitude()/self.size,i/self.size,far_end_draw = draw,offset = temp_vec.argument())
            self.rotvecs.append(temp)

    def draw_them_all(self):
        self.rotvecs[1].draw_me()
        self.rotvecs[1].update_me()
        for i in range(2,self.size):
            self.rotvecs[i].centre = self.rotvecs[i-1].far_end
            self.rotvecs[i].draw_me()
            self.rotvecs[i].update_me()
        self.rotvecs[0].centre = self.rotvecs[self.size-1].far_end
        self.rotvecs[0].draw_me()
        self.rotvecs[0].update_me()
        
