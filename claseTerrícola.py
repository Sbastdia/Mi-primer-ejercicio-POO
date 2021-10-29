from claseGuerrero import Guerrero
from random import randint

class Terricola(Guerrero):
    __totalTerricolasAlive = 0
    __shots_done = [0] * (Guerrero.get_maxTarget() + 1)

    def __init__(self, name):
    Guerrero.__init__(self, name)
    Terricola.__totalTerricolasAlive += 1
# Overrides the method shoot from the parent class!
    def shoot(self):

#  Shoot if the Terricola is alive generating a random number between
# 0 and the __max_target
#  It shoots a number of times equals to the number of shoots that a
# Marciano can hold
#  :returns the number to shoot if the warrior is alive, -1 otherwise

        if(self._vivo):
            shot = generaIntAleatorio(0,Guerrero.get_maxTarget())
        while(Terricola.__shots_done[shot] >=
            Marciano.get_shotsToKillAMarciano()):
            shot = generaIntAleatorio(0,Guerrero.get_maxTarget())
            Terricola.__shots_done[shot] += 1