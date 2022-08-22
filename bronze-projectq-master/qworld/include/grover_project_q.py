# Import all required objects and methods
from projectq import MainEngine
from projectq.ops import H,X,Measure,All, C, NOT, Barrier
from projectq.backends import CircuitDrawerMatplotlib, Simulator
from projectq.setups.default import get_engine_list

def giant_oracle(eng,qubit):
    
    number = 18
    
    if(number%2 == 0):
        X | qubit[0]
    if(number%4 < 2):
        X | qubit[1]
    if(number%8 < 4):
        X | qubit[2]
    if(number%16 < 8):
        X | qubit[3]
    if(number%32 < 16):
        X | qubit[4]
    if(number%64 < 32):
        X | qubit[5]
    if(number%128 < 64):
        X | qubit[6]
    if(number%256 < 128):
        X | qubit[7]
    if(number%512 < 256):
        X | qubit[8]
    if(number < 512):
        X | qubit[9]
        
    C(NOT,2) | (qubit[0], qubit[1], qubit[18])
    C(NOT,2) | (qubit[2], qubit[3], qubit[11])
    C(NOT,2) | (qubit[4], qubit[5], qubit[12])
    C(NOT,2) | (qubit[6], qubit[7], qubit[13])
    C(NOT,2) | (qubit[8], qubit[9], qubit[14])
    
    C(NOT,2) | (qubit[18], qubit[11], qubit[15])
    C(NOT,2) | (qubit[12], qubit[13], qubit[16])
    
    C(NOT,2) | (qubit[15], qubit[16], qubit[17])
    C(NOT,2) | (qubit[14], qubit[17], qubit[10])
    C(NOT,2) | (qubit[15], qubit[16], qubit[17])
    
    C(NOT,2) | (qubit[12], qubit[13], qubit[16])
    C(NOT,2) | (qubit[18], qubit[11], qubit[15])
    
    C(NOT,2) | (qubit[8], qubit[9], qubit[14])
    C(NOT,2) | (qubit[6], qubit[7], qubit[13])
    C(NOT,2) | (qubit[4], qubit[5], qubit[12])
    C(NOT,2) | (qubit[2], qubit[3], qubit[11]) 
    C(NOT,2) | (qubit[0], qubit[1], qubit[18])
    
    if(number%2 == 0):
        X | qubit[0]
    if(number%4 < 2):
        X | qubit[1]
    if(number%8 < 4):
        X | qubit[2]
    if(number%16 < 8):
        X | qubit[3]
    if(number%32 < 16):
        X | qubit[4]
    if(number%64 < 32):
        X | qubit[5]
    if(number%128 < 64):
        X | qubit[6]
    if(number%256 < 128):
        X | qubit[7]
    if(number%512 < 256):
        X | qubit[8]
    if(number < 512):
        X | qubit[9]
        

def giant_oracle2(eng,qubit):
    
    numbers=[12,45]
    
    for number in numbers:
        if(number%2 == 0):
            X | qubit[0]
        if(number%4 < 2):
            X | qubit[1]
        if(number%8 < 4):
            X | qubit[2]
        if(number%16 < 8):
            X | qubit[3]
        if(number%32 < 16):
            X | qubit[4]
        if(number%64 < 32):
            X | qubit[5]
        if(number%128 < 64):
            X | qubit[6]
        if(number%256 < 128):
            X | qubit[7]
        if(number%512 < 256):
            X | qubit[8]
        if(number < 512):
            X | qubit[9]

        C(NOT,2) | (qubit[0], qubit[1], qubit[18])
        C(NOT,2) | (qubit[2], qubit[3], qubit[11])
        C(NOT,2) | (qubit[4], qubit[5], qubit[12])
        C(NOT,2) | (qubit[6], qubit[7], qubit[13])
        C(NOT,2) | (qubit[8], qubit[9], qubit[14])
        
        C(NOT,2) | (qubit[18], qubit[11], qubit[15])
        C(NOT,2) | (qubit[12], qubit[13], qubit[16])

        C(NOT,2) | (qubit[15], qubit[16], qubit[17])
        C(NOT,2) | (qubit[14], qubit[17], qubit[10])
        C(NOT,2) | (qubit[15], qubit[16], qubit[17])

        C(NOT,2) | (qubit[12], qubit[13], qubit[16])
        C(NOT,2) | (qubit[18], qubit[11], qubit[15])

        C(NOT,2) | (qubit[8], qubit[9], qubit[14])
        C(NOT,2) | (qubit[6], qubit[7], qubit[13])
        C(NOT,2) | (qubit[4], qubit[5], qubit[12])
        C(NOT,2) | (qubit[2], qubit[3], qubit[11]) 
        C(NOT,2) | (qubit[0], qubit[1], qubit[18])

        if(number%2 == 0):
            X | qubit[0]
        if(number%4 < 2):
            X | qubit[1]
        if(number%8 < 4):
            X | qubit[2]
        if(number%16 < 8):
            X | qubit[3]
        if(number%32 < 16):
            X | qubit[4]
        if(number%64 < 32):
            X | qubit[5]
        if(number%128 < 64):
            X | qubit[6]
        if(number%256 < 128):
            X | qubit[7]
        if(number%512 < 256):
            X | qubit[8]
        if(number < 512):
            X | qubit[9]
            
def giant_diffusion(eng,qubit):
    
    for i in range(10):
        H | qubit[i]
        X | qubit[i]

    C(NOT,2) | (qubit[0], qubit[1], qubit[18])
    C(NOT,2) | (qubit[2], qubit[3], qubit[11])
    C(NOT,2) | (qubit[4], qubit[5], qubit[12])
    C(NOT,2) | (qubit[6], qubit[7], qubit[13])
    C(NOT,2) | (qubit[8], qubit[9], qubit[14])

    C(NOT,2) | (qubit[18], qubit[11], qubit[15])
    C(NOT,2) | (qubit[12], qubit[13], qubit[16])

    C(NOT,2) | (qubit[15], qubit[16], qubit[17])
    C(NOT,2) | (qubit[14], qubit[17], qubit[10])
    C(NOT,2) | (qubit[15], qubit[16], qubit[17])

    C(NOT,2) | (qubit[12], qubit[13], qubit[16])
    C(NOT,2) | (qubit[18], qubit[11], qubit[15])

    C(NOT,2) | (qubit[8], qubit[9], qubit[14])
    C(NOT,2) | (qubit[6], qubit[7], qubit[13])
    C(NOT,2) | (qubit[4], qubit[5], qubit[12])
    C(NOT,2) | (qubit[2], qubit[3], qubit[11]) 
    C(NOT,2) | (qubit[0], qubit[1], qubit[18])

    for i in range(10):
        X | qubit[i]
        H | qubit[i]
    
    X | qubit[10]
    
def Uf(eng,qubit):
    C(NOT,2) | (qubit[0], qubit[1], qubit[2])

def Uf_8(eng,qubit):
    X | qubit[2]
    C(NOT,2) | (qubit[2], qubit[1], qubit[4])
    C(NOT,2) | (qubit[4], qubit[0], qubit[3])
    C(NOT,2) | (qubit[2], qubit[1], qubit[4])
    X | qubit[2]

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    