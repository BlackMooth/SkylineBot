# Generated from Skyline.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#prog.
    def visitProg(self, ctx:SkylineParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#printSkyline.
    def visitPrintSkyline(self, ctx:SkylineParser.PrintSkylineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#assign.
    def visitAssign(self, ctx:SkylineParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#Intersection.
    def visitIntersection(self, ctx:SkylineParser.IntersectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#parens.
    def visitParens(self, ctx:SkylineParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#EdificiSimple.
    def visitEdificiSimple(self, ctx:SkylineParser.EdificiSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#reflection.
    def visitReflection(self, ctx:SkylineParser.ReflectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#EdificisAleatoris.
    def visitEdificisAleatoris(self, ctx:SkylineParser.EdificisAleatorisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#Replication.
    def visitReplication(self, ctx:SkylineParser.ReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#EdificisCompostos.
    def visitEdificisCompostos(self, ctx:SkylineParser.EdificisCompostosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#id.
    def visitId(self, ctx:SkylineParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#Union.
    def visitUnion(self, ctx:SkylineParser.UnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#Desp.
    def visitDesp(self, ctx:SkylineParser.DespContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skyline_sets.
    def visitSkyline_sets(self, ctx:SkylineParser.Skyline_setsContext):
        return self.visitChildren(ctx)



del SkylineParser