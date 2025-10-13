from __future__ import annotations
import copy
import random
import sys

import pokemon
from play import *


pokemon1 = pokemon.Bulbasaur()
pokemon2 = pokemon.PikaChu()
all_pokemon = [pokemon1,pokemon2]
play = Play(all_pokemon)
play.run()
