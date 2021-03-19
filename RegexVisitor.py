# Generated from Regex.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
	from .RegexParser import RegexParser
else:
	from RegexParser import RegexParser

# This class defines a complete generic visitor for a parse tree produced by RegexParser.

class RegexVisitor(ParseTreeVisitor):

	# Visit a parse tree produced by RegexParser#regex.
	def visitRegex(self, ctx:RegexParser.RegexContext):
		return self.visitChildren(ctx)


	# Visit a parse tree produced by RegexParser#concat_regex.
	def visitConcat_regex(self, ctx:RegexParser.Concat_regexContext):
		return self.visitChildren(ctx)


	# Visit a parse tree produced by RegexParser#kleene_regex.
	def visitKleene_regex(self, ctx:RegexParser.Kleene_regexContext):
		return self.visitChildren(ctx)


	# Visit a parse tree produced by RegexParser#atom.
	def visitAtom(self, ctx:RegexParser.AtomContext):
		return self.visitChildren(ctx)


	# Visit a parse tree produced by RegexParser#symbol.
	def visitSymbol(self, ctx:RegexParser.SymbolContext):
		return self.visitChildren(ctx)


	# Visit a parse tree produced by RegexParser#inner_regex.
	def visitInner_regex(self, ctx:RegexParser.Inner_regexContext):
		return self.visitChildren(ctx)



del RegexParser