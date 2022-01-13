import sys
sys.path.append('./zadanie2')
from src.Planets import Planets

def before_scenario(context, scenario):
    context.Planets = Planets()

def after_scenario(context, scenario):
    context.Planets = None
