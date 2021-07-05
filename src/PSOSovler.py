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
    def solver(self):
        X = np.zeros((self.num, self.dim))
        V = np.zeros((self.num, self.dim))
        p_best = np.zeros((self.num, self.dim), dtype=float)
        g_best = np.zeros((1, self.dim), dtype=float)
        p_bestfit = np.zeros(self.num)
        g_bestfit = -1e15

        for i in range(self.num):
            X[i] = np.random.uniform(0, 5, [1, self.dim])
            V[i] = np.random.uniform(0, 5, [1, self.dim])
            p_best[i] = X[i]
            p_bestfit[i] = self.kp.cost(X[i])
            if p_bestfit[i] > g_bestfit:
                g_bestfit = p_bestfit[i]
                g_best = X[i]
        fitness = []

        for _ in range(self.max_iter):
            for i in range(self.num):
                temp = self.kp.cost(X[i])
                if temp > p_bestfit[i]:
                    p_bestfit[i] = temp
                    p_best[i] = X[i]
                    if p_bestfit[i] > g_bestfit:
                        g_best = X[i]
                        g_bestfit = p_bestfit[i]

            for i in range(self.num):
                V[i] = self.w * V[i] + self.c1 * self.r1 * (p_best[i] - X[i]) + self.c2 * self.r2 * (g_best - X[i])
                X[i] = X[i] + V[i]

            fitness.append(g_bestfit)

        print(g_best, g_bestfit)
