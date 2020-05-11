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

    def draw_polygon(self,points_coll):
        for i in range(1,len(points_coll)):
                pygame.draw.line(self.screen,(0,255,0),(points_coll[i-1].x,points_coll[i-1].y),(points_coll[i].x,points_coll[i].y),2)
    
    def draw_me(self):
        self.far_end = self.centre.protrude(self.amplitude,self.angle())
        pygame.draw.line(self.screen,(255,0,0),(self.centre.x,self.centre.y),(self.far_end.x,self.far_end.y),2)
        if self.amplitude > 1:
            pygame.draw.circle(self.screen,(0,0,255),(int(self.centre.x),int(self.centre.y)),int(self.amplitude),1)
        if self.far_end_draw:
            self.points_coll.append(self.far_end)
            self.draw_polygon(self.points_coll)
        
    def update_me(self):
        self.time+=1
    
    
class epicycles():
    def __init__(self,centre,screen,all_amplitudes):
        self.centre = centre
        self.screen = screen
        self.current_assign = 0
        self.all_amplitudes = all_amplitudes
        self.amplitudes = self.all_amplitudes[self.current_assign]
        self.rotvecs = []
        self.size = len(self.amplitudes)
        self.amp_count = len(all_amplitudes)
        self.archived = []
        
    def assign_params(self):
        for i in range(self.size):
            draw = True if i==0 else False
            temp_vec = vector(self.amplitudes[i].real,self.amplitudes[i].imag)
            temp = rotvec(self.screen,self.centre,temp_vec.magnitude()/self.size,i/self.size,far_end_draw = draw,offset = temp_vec.argument())
            self.rotvecs.append(temp)
        self.rotvecs.reverse()

    def draw_them_all(self):
        for i in range(0,self.size):
            if i>0:
                self.rotvecs[i].centre = self.rotvecs[i-1].far_end
            self.rotvecs[i].draw_me()
            self.rotvecs[i].update_me()
            
        for item in self.archived:
            self.rotvecs[-1].draw_polygon(item)
        if len(self.rotvecs[-1].points_coll) == self.size+5:#To close contours smoothly +1 would have been enough
            self.archived.append(self.rotvecs[-1].points_coll)
            self.current_assign +=1
            if self.current_assign == self.amp_count:
                self.current_assign = 0
            self.amplitudes = self.all_amplitudes[self.current_assign]
            self.size = len(self.amplitudes)
            self.rotvecs = []
            self.assign_params()
            self.draw_them_all()
        
