import board
import digitalio
import random
import time

# debug = True
debug = False

def debug_print(str):
    if not debug:
        return
    print(str) # This will be executed only when debug == True.

class LED2:
    '''
    Class LED2 (version 2)
    Abstract LED with anode and cathode
    '''
    
    initialized_ports = {}
    
    def __init__(self, anode_port, cathode_port):
        if anode_port in LED2.initialized_ports: # Check if the anode_port already has been initialized.
            self.anode = LED2.initialized_ports[anode_port] # Use already initialized instance.
        else: # if not, newly initialize.
            self.anode = digitalio.DigitalInOut(anode_port)
            self.anode.direction = digitalio.Direction.OUTPUT
            LED2.initialized_ports[anode_port] = self.anode # Add to the dictionary.
        if cathode_port in LED2.initialized_ports: # Check if the cathode_port already has been initialized.
            self.cathode = LED2.initialized_ports[cathode_port] # Use already initialized instance.
        else: # if not, newly initialize.
            self.cathode = digitalio.DigitalInOut(cathode_port)
            self.cathode.direction = digitalio.Direction.OUTPUT
            LED2.initialized_ports[cathode_port] = self.cathode # Add to the dictionary.
            
        debug_print(LED2.initialized_ports)
        debug_print(self.anode)
        debug_print(self.cathode)
        
    def on(self):
        self.anode.value = True  # Anode --> High
        self.cathode.value = False # Cathode --> Low
        
    def off(self):
        self.anode.value = False # Anode --> Low
        self.cathode.value = True # Cathode --> High
        
class SWITCH:
    '''
    Class SWITCH
    Abstracts switch input over digital input port
    '''
    def __init__(self, port, polarity=False): # Polarity = True --> Active High
        self.port = digitalio.DigitalInOut(port)
        self.port.direction = digitalio.Direction.INPUT
        self.polarity = polarity
        
    def isPressed(self): # Returns True if SWITCH is pressed
        return not (self.polarity ^ self.port.value)

    def isReleased(self): # Returns True if SWITCH is released
        return not not (self.polarity ^ self.port.value)
    
class Roulette:
    '''
    Class Roulette
    '''
    def __init__(self, leds: list):
        '''
        [ D1, D2, D3, ......., D30 ]
        '''
        self.leds = leds
        self.off()
        
    def off(self, led=None):
        '''
        Turn off a specifed LED.
        If no LED is specified, turn off all LEDs.
        '''
        if led == None:
            for led in self.leds:
                led.off()
        else:
            self.leds[led].off()
            
    def on(self, led=None):
        '''
        Turn on a specifed LED.
        If no LED is specified, turn on all LEDs.
        '''
        if led == None:
            for led in self.leds:
                led.on()
        else:
            self.leds[led].on()
            
    def num_leds(self):
        '''
        Returns how many LEDs in this roulette
        '''
        num_leds = len(self.leds)
        debug_print(f"num_led = {num_leds}")
        return len(self.leds)
            
class Roulette_Game:
    '''
    Class Roulette_Game
    '''
    def __init__(self, roulette: Roulette):
        self.roulette = roulette
        
    def run(self):
        initial_run = random.randint(60,150)
        debug_print(f"Initial run = {initial_run}")
        index = random.randint(0, self.roulette.num_leds()-1)
        debug_print(f"Initial Index = {index}")
        interval = 0.05  # Initial interval = 50 msec
        
        debug_print("----- Initial Run -----")
        # Initial Run
        for run in range(initial_run):
            self.roulette.on(index)
            debug_print(f"Initial run index = {index}")
            time.sleep(interval)
            self.roulette.off(index)
            index += 1
            if index >= self.roulette.num_leds():
                index = 0
        
        debug_print("----- Roulette Run -----")
        # Roulette Run
        iter = random.randint(150, 300)
        debug_print(f"iter = {iter}")
        for run in range(iter):
            self.roulette.on(index)
            debug_print(f"Roulette run index = {index}")
            interval = 0.05 * (0.5/0.05) ** (run / iter) # Interval increases at each run
            time.sleep(interval)
            if run != iter-1:
                self.roulette.off(index)
            index += 1
            if index >= self.roulette.num_leds():
                index = 0
            
def roulette_main():
    switch = SWITCH(board.PB5)
    roulette = Roulette([\
        LED2(board.PB0, board.PA0), LED2(board.PB0, board.PB1), LED2(board.PB0, board.PD5), LED2(board.PB0, board.PD4), LED2(board.PB0, board.PB4),\
        LED2(board.PC8, board.PA0), LED2(board.PC8, board.PB1), LED2(board.PC8, board.PD5), LED2(board.PC8, board.PD4), LED2(board.PC8, board.PB4),\
        LED2(board.PC0, board.PA0), LED2(board.PC0, board.PB1), LED2(board.PC0, board.PD5), LED2(board.PC0, board.PD4), LED2(board.PC0, board.PB4),\
        LED2(board.PC1, board.PA0), LED2(board.PC1, board.PB1), LED2(board.PC1, board.PD5), LED2(board.PC1, board.PD4), LED2(board.PC1, board.PB4),\
        LED2(board.PC2, board.PA0), LED2(board.PC2, board.PB1), LED2(board.PC2, board.PD5), LED2(board.PC2, board.PD4), LED2(board.PC2, board.PB4),\
        LED2(board.PC3, board.PA0), LED2(board.PC3, board.PB1), LED2(board.PC3, board.PD5), LED2(board.PC3, board.PD4), LED2(board.PC3, board.PB4) \
        ])
    
    roulette.off()
    roulette_game = Roulette_Game(roulette)
    
    while True:
        while switch.isReleased():
            pass
        while switch.isPressed():
            roulette.on()
        roulette.off()
        roulette_game.run()
        
if __name__=="__main__":
    roulette_main()