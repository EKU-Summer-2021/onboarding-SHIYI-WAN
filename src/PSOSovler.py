import numpy as np
from src.KP import KP


class PSOSolver:
    def __init__(self, w, c1, c2, r1, r2, num, dim, max_iter, kpdataset, kpmax_weight, kpafa):
        self.w = w  # inertia factor
        self.c1 = c1  # self-cognition factor
        self.c2 = c2  # social cognitive factor
        self.r1 = r1  # self-cognition learning rate
        self.r2 = r2  # Social cognitive learning rate
        self.num = num  # number of particles
        self.dim = dim  # search dimension
        self.max_iter = max_iter  # Maximum number of iterations
        self.kp = KP(dataset=kpdataset, max_weight=kpmax_weight, afa=kpafa)
