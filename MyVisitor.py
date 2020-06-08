from Skyline import Skyline

from cl.test.SkylineVisitor import SkylineVisitor
from cl.test.SkylineParser import SkylineParser


class MyVisitor(SkylineVisitor):
    def __init__(self, context):
        self.memory = context.user_data

    def visitPrintSkyline(self, ctx):
        value = self.visit(ctx.skyline())
        return value

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.skyline())
        self.memory[name] = value
        return value

    def visitIntersection(self, ctx):
        left = self.visit(ctx.skyline(0))
        right = self.visit(ctx.skyline(1))
        return left.interseccio_skylines(right)

    def visitReplication(self, ctx):
        s = self.visit(ctx.skyline())
        n = ctx.INT().getText()
        return s.replica_skyline(n)

    def visitUnion(self, ctx):
        left = self.visit(ctx.skyline(0))
        right = self.visit(ctx.skyline(1))
        return left.unio_skylines(right)

    def visitDesp(self, ctx):
        s = self.visit(ctx.skyline())
        n = ctx.INT().getText()
        return s.desplacament_skyline(n)

    def visitEdificiSimple(self, ctx):
        s = Skyline()
        s.afegeix_edifici(int(ctx.INT(0).getText()), int(ctx.INT(1).getText()), int(ctx.INT(2).getText()))
        return s

    def visitEdificisCompostos(self, ctx):
        return self.visit(ctx.skyline_sets())

    def visitSkyline_sets(self, ctx):
        s = Skyline()
        aux = self.auxVisitSkyline_sets(ctx, s)
        return s

    # Funcio auxiliar per la creacio de skylines complexos
    def auxVisitSkyline_sets(self, ctx, s):
        if ctx.skyline_sets() is not None:
            s.afegeix_edifici(int(ctx.INT(0).getText()), int(ctx.INT(1).getText()), int(ctx.INT(2).getText()))
            self.auxVisitSkyline_sets(ctx.skyline_sets(), s)
        else:
            s.afegeix_edifici(int(ctx.INT(0).getText()), int(ctx.INT(1).getText()), int(ctx.INT(2).getText()))

    def visitEdificisAleatoris(self, ctx):
        s = Skyline()
        s.random_skyline(int(ctx.INT(0).getText()), int(ctx.INT(1).getText()), int(ctx.INT(2).getText()), int(ctx.INT(3).getText()), int(ctx.INT(4).getText()))
        return s

    def visitParens(self, ctx):
        return self.visit(ctx.skyline())

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            value = Skyline()
            value = self.memory[name]
            return value
        s = Skyline()
        s.lims[0] = 0
        s.lims[1] = 1
        s.altura = 1
        return s  # Si ens pasen un ID que no existeix, retornem un Skyline buit

    def visitInt(self, ctx):
        return ctx.INT().getText()

    def visitReflection(self, ctx):
        s = self.visit(ctx.skyline())
        return s.reflect()
