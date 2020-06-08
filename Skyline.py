import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl

import random


class Skyline:
    def __init__(self):
        self.area = 0
        self.altura = 0
        self.lims = [-1, -1]
        self.skyline = {}

    def afegeix_edifici(self, esquerra, altura, dreta):
        if esquerra < dreta and altura >= 0:
            if self.lims[0] == -1:
                self.lims[0] = esquerra
                self.lims[1] = dreta
            else:
                if esquerra < self.lims[0]:
                    self.lims[0] = esquerra
                if dreta > self.lims[1]:
                    self.lims[1] = dreta
            if altura > self.altura:
                self.altura = altura
            for i in range(esquerra, dreta):
                h_old = self.skyline.get(i)
                if h_old is None:
                    self.skyline[i] = altura
                    self.area += altura
                else:
                    if h_old < altura:
                        self.skyline[i] = altura
                        self.area += altura-h_old

    def interseccio_skylines(s1, s2):
        s1_interseccio_s2 = Skyline()
        for i in s1.skyline.keys():
            altura_s1_i = s1.skyline[i]
            altura_s2_i = s2.skyline.get(i)  # no es segur que hi hagi una entrada al diccionari de s2 per la i
            if altura_s2_i is not None:
                if s1_interseccio_s2.lims[0] == -1:
                    s1_interseccio_s2.lims[0] = i
                    s1_interseccio_s2.lims[1] = i+1
                else:
                    if (i+1) > s1_interseccio_s2.lims[1]:
                        s1_interseccioz_s2.lims[1] = (i+1)
                h = min(altura_s1_i, altura_s2_i)
                s1_interseccio_s2.skyline[i] = h
                s1_interseccio_s2.area += h
                if h > s1_interseccio_s2.altura:
                    s1_interseccio_s2.altura = h
        return s1_interseccio_s2

    def unio_skylines(s1, s2):
        s1_unio_s2 = Skyline()
        for i in s1.skyline.keys():
            if s1_unio_s2.lims[0] == -1:
                s1_unio_s2.lims[0] = i
                s1_unio_s2.lims[1] = i+1
            else:
                if (i+1) > s1_unio_s2.lims[1]:
                    s1_unio_s2.lims[1] = i+1
            altura_s1_i = s1.skyline[i]
            s1_unio_s2.skyline[i] = altura_s1_i
            s1_unio_s2.area += altura_s1_i
            if altura_s1_i > s1_unio_s2.altura:
                s1_unio_s2.altura = altura_s1_i

        for i in s2.skyline.keys():
            if (i+1) > s1_unio_s2.lims[1]:
                s1_unio_s2.lims[1] = i+1
            altura_s2_i = s2.skyline[i]
            altura_s1_i = s1_unio_s2.skyline.get(i)
            if altura_s1_i is not None:
                if altura_s2_i > altura_s1_i:
                    s1_unio_s2.skyline[i] = altura_s2_i
                    s1_unio_s2.area += (altura_s2_i-altura_s1_i)
            else:
                s1_unio_s2.skyline[i] = altura_s2_i
                s1_unio_s2.area += altura_s2_i
            if altura_s2_i > s1_unio_s2.altura:
                s1_unio_s2.altura = altura_s2_i
        return s1_unio_s2

    def desplacament_skyline(s, desp):
        s_desp = Skyline()
        s_desp.lims[0] = s.lims[0]  # Mantenim el lim esq original, per visualitzar el desplacament
        s_desp.lims[1] = s.lims[1] + int(desp)
        s_desp.altura = s.altura
        s_desp.area = s.area
        for i in s.skyline.keys():
            s_desp.skyline[i+int(desp)] = s.skyline[i]
        return s_desp

    def replica_skyline(s, n):
        s_replica = Skyline()
        if n == 1:
            s_replica = s
            return s_replica
        periode = s.lims[1]-s.lims[0]
        s_replica.lims[0] = s.lims[0]
        s_replica.lims[1] = s.lims[1] + periode*(int(n)-1)
        s_replica.altura = s.altura
        s_replica.area = s.area*int(n)
        for i in s.skyline.keys():
            altura_s_i = s.skyline[i]
            for k in range(0, int(n)):
                s_replica.skyline[i+k*periode] = altura_s_i
        return s_replica

    def random_skyline(self, n, h, w, xmin, xmax):
        for i in range(n):
            pos_ini = xmin + random.randint(0, int(xmax-xmin-1))
            amplada = random.randint(1, min(int(xmax-pos_ini), w))
            pos_final = pos_ini + amplada
            altura = random.randint(0, int(h))
            self.afegeix_edifici(pos_ini, altura, pos_final)

    def reflect(self):
        x_min = self.lims[0]
        x_max = self.lims[1]
        s_reflected = Skyline()
        s_reflected.lims[0] = x_min
        s_reflected.lims[1] = x_max
        s_reflected.altura = self.altura
        s_reflected.area = self.area
        for i in self.skyline.keys():
            s_reflected.skyline[x_max-(i-x_min)-1] = self.skyline[i]
        return s_reflected

    def print_skyline(s):
        fitxer = "%d.png" % random.randint(1000000, 9999999)
        fig = plt.figure()
        ax = fig.add_subplot(111, xlim=(int(s.lims[0]), int(s.lims[1])), ylim=(0, int(s.altura)))
        for i in s.skyline.keys():
            r1 = ax.add_patch(patches.Rectangle((i, 0), int(1), int(s.skyline[i])))

        ax.set_aspect('equal')
        ax.set_xlim(int(s.lims[0]), int(s.lims[1]))
        ax.set_ylim(0, s.altura)
        try:
            plt.savefig(fitxer, bbox_inches='tight')
        except (OSError, IOError) as e:
            fitxer = 0
        return fitxer
