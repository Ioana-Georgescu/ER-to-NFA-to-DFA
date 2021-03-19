# Generated from Regex.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
	with StringIO() as buf:
		buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
		buf.write(",\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
		buf.write("\3\2\3\2\3\2\3\2\5\2\24\n\2\3\3\3\3\3\3\3\3\5\3\32\n\3")
		buf.write("\3\4\3\4\3\4\3\4\5\4 \n\4\3\5\3\5\5\5$\n\5\3\6\3\6\3\7")
		buf.write("\3\7\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2)\2\23\3\2\2\2")
		buf.write("\4\31\3\2\2\2\6\37\3\2\2\2\b#\3\2\2\2\n%\3\2\2\2\f\'\3")
		buf.write("\2\2\2\16\24\5\4\3\2\17\20\5\4\3\2\20\21\7\6\2\2\21\22")
		buf.write("\5\2\2\2\22\24\3\2\2\2\23\16\3\2\2\2\23\17\3\2\2\2\24")
		buf.write("\3\3\2\2\2\25\32\5\6\4\2\26\27\5\6\4\2\27\30\5\4\3\2\30")
		buf.write("\32\3\2\2\2\31\25\3\2\2\2\31\26\3\2\2\2\32\5\3\2\2\2\33")
		buf.write(" \5\b\5\2\34\35\5\b\5\2\35\36\7\7\2\2\36 \3\2\2\2\37\33")
		buf.write("\3\2\2\2\37\34\3\2\2\2 \7\3\2\2\2!$\5\n\6\2\"$\5\f\7\2")
		buf.write("#!\3\2\2\2#\"\3\2\2\2$\t\3\2\2\2%&\7\3\2\2&\13\3\2\2\2")
		buf.write("\'(\7\4\2\2()\5\2\2\2)*\7\5\2\2*\r\3\2\2\2\6\23\31\37")
		buf.write("#")
		return buf.getvalue()


class RegexParser ( Parser ):

	grammarFileName = "Regex.g4"

	atn = ATNDeserializer().deserialize(serializedATN())

	decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

	sharedContextCache = PredictionContextCache()

	literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "'|'" ]

	symbolicNames = [ "<INVALID>", "SYMBOL", "OPEN", "CLOSE", "REUNION", 
					  "KLEENE", "WHITESPACE" ]

	RULE_regex = 0
	RULE_concat_regex = 1
	RULE_kleene_regex = 2
	RULE_atom = 3
	RULE_symbol = 4
	RULE_inner_regex = 5

	ruleNames =  [ "regex", "concat_regex", "kleene_regex", "atom", "symbol", 
				   "inner_regex" ]

	EOF = Token.EOF
	SYMBOL=1
	OPEN=2
	CLOSE=3
	REUNION=4
	KLEENE=5
	WHITESPACE=6

	def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
		super().__init__(input, output)
		self.checkVersion("4.7.2")
		self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
		self._predicates = None



	class RegexContext(ParserRuleContext):

		def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
			super().__init__(parent, invokingState)
			self.parser = parser

		def concat_regex(self):
			return self.getTypedRuleContext(RegexParser.Concat_regexContext,0)


		def REUNION(self):
			return self.getToken(RegexParser.REUNION, 0)

		def regex(self):
			return self.getTypedRuleContext(RegexParser.RegexContext,0)


		def getRuleIndex(self):
			return RegexParser.RULE_regex

		def accept(self, visitor:ParseTreeVisitor):
			if hasattr( visitor, "visitRegex" ):
				return visitor.visitRegex(self)
			else:
				return visitor.visitChildren(self)




	def regex(self):

		localctx = RegexParser.RegexContext(self, self._ctx, self.state)
		self.enterRule(localctx, 0, self.RULE_regex)
		try:
			self.state = 17
			self._errHandler.sync(self)
			la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
			if la_ == 1:
				self.enterOuterAlt(localctx, 1)
				self.state = 12
				self.concat_regex()
				pass

			elif la_ == 2:
				self.enterOuterAlt(localctx, 2)
				self.state = 13
				self.concat_regex()
				self.state = 14
				self.match(RegexParser.REUNION)
				self.state = 15
				self.regex()
				pass


		except RecognitionException as re:
			localctx.exception = re
			self._errHandler.reportError(self, re)
			self._errHandler.recover(self, re)
		finally:
			self.exitRule()
		return localctx

	class Concat_regexContext(ParserRuleContext):

		def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
			super().__init__(parent, invokingState)
			self.parser = parser

		def kleene_regex(self):
			return self.getTypedRuleContext(RegexParser.Kleene_regexContext,0)


		def concat_regex(self):
			return self.getTypedRuleContext(RegexParser.Concat_regexContext,0)


		def getRuleIndex(self):
			return RegexParser.RULE_concat_regex

		def accept(self, visitor:ParseTreeVisitor):
			if hasattr( visitor, "visitConcat_regex" ):
				return visitor.visitConcat_regex(self)
			else:
				return visitor.visitChildren(self)




	def concat_regex(self):

		localctx = RegexParser.Concat_regexContext(self, self._ctx, self.state)
		self.enterRule(localctx, 2, self.RULE_concat_regex)
		try:
			self.state = 23
			self._errHandler.sync(self)
			la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
			if la_ == 1:
				self.enterOuterAlt(localctx, 1)
				self.state = 19
				self.kleene_regex()
				pass

			elif la_ == 2:
				self.enterOuterAlt(localctx, 2)
				self.state = 20
				self.kleene_regex()
				self.state = 21
				self.concat_regex()
				pass


		except RecognitionException as re:
			localctx.exception = re
			self._errHandler.reportError(self, re)
			self._errHandler.recover(self, re)
		finally:
			self.exitRule()
		return localctx

	class Kleene_regexContext(ParserRuleContext):

		def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
			super().__init__(parent, invokingState)
			self.parser = parser

		def atom(self):
			return self.getTypedRuleContext(RegexParser.AtomContext,0)


		def KLEENE(self):
			return self.getToken(RegexParser.KLEENE, 0)

		def getRuleIndex(self):
			return RegexParser.RULE_kleene_regex

		def accept(self, visitor:ParseTreeVisitor):
			if hasattr( visitor, "visitKleene_regex" ):
				return visitor.visitKleene_regex(self)
			else:
				return visitor.visitChildren(self)




	def kleene_regex(self):

		localctx = RegexParser.Kleene_regexContext(self, self._ctx, self.state)
		self.enterRule(localctx, 4, self.RULE_kleene_regex)
		try:
			self.state = 29
			self._errHandler.sync(self)
			la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
			if la_ == 1:
				self.enterOuterAlt(localctx, 1)
				self.state = 25
				self.atom()
				pass

			elif la_ == 2:
				self.enterOuterAlt(localctx, 2)
				self.state = 26
				self.atom()
				self.state = 27
				self.match(RegexParser.KLEENE)
				pass


		except RecognitionException as re:
			localctx.exception = re
			self._errHandler.reportError(self, re)
			self._errHandler.recover(self, re)
		finally:
			self.exitRule()
		return localctx

	class AtomContext(ParserRuleContext):

		def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
			super().__init__(parent, invokingState)
			self.parser = parser

		def symbol(self):
			return self.getTypedRuleContext(RegexParser.SymbolContext,0)


		def inner_regex(self):
			return self.getTypedRuleContext(RegexParser.Inner_regexContext,0)


		def getRuleIndex(self):
			return RegexParser.RULE_atom

		def accept(self, visitor:ParseTreeVisitor):
			if hasattr( visitor, "visitAtom" ):
				return visitor.visitAtom(self)
			else:
				return visitor.visitChildren(self)




	def atom(self):

		localctx = RegexParser.AtomContext(self, self._ctx, self.state)
		self.enterRule(localctx, 6, self.RULE_atom)
		try:
			self.state = 33
			self._errHandler.sync(self)
			token = self._input.LA(1)
			if token in [RegexParser.SYMBOL]:
				self.enterOuterAlt(localctx, 1)
				self.state = 31
				self.symbol()
				pass
			elif token in [RegexParser.OPEN]:
				self.enterOuterAlt(localctx, 2)
				self.state = 32
				self.inner_regex()
				pass
			else:
				raise NoViableAltException(self)

		except RecognitionException as re:
			localctx.exception = re
			self._errHandler.reportError(self, re)
			self._errHandler.recover(self, re)
		finally:
			self.exitRule()
		return localctx

	class SymbolContext(ParserRuleContext):

		def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
			super().__init__(parent, invokingState)
			self.parser = parser

		def SYMBOL(self):
			return self.getToken(RegexParser.SYMBOL, 0)

		def getRuleIndex(self):
			return RegexParser.RULE_symbol

		def accept(self, visitor:ParseTreeVisitor):
			if hasattr( visitor, "visitSymbol" ):
				return visitor.visitSymbol(self)
			else:
				return visitor.visitChildren(self)




	def symbol(self):

		localctx = RegexParser.SymbolContext(self, self._ctx, self.state)
		self.enterRule(localctx, 8, self.RULE_symbol)
		try:
			self.enterOuterAlt(localctx, 1)
			self.state = 35
			self.match(RegexParser.SYMBOL)
		except RecognitionException as re:
			localctx.exception = re
			self._errHandler.reportError(self, re)
			self._errHandler.recover(self, re)
		finally:
			self.exitRule()
		return localctx

	class Inner_regexContext(ParserRuleContext):

		def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
			super().__init__(parent, invokingState)
			self.parser = parser

		def OPEN(self):
			return self.getToken(RegexParser.OPEN, 0)

		def regex(self):
			return self.getTypedRuleContext(RegexParser.RegexContext,0)


		def CLOSE(self):
			return self.getToken(RegexParser.CLOSE, 0)

		def getRuleIndex(self):
			return RegexParser.RULE_inner_regex

		def accept(self, visitor:ParseTreeVisitor):
			if hasattr( visitor, "visitInner_regex" ):
				return visitor.visitInner_regex(self)
			else:
				return visitor.visitChildren(self)




	def inner_regex(self):

		localctx = RegexParser.Inner_regexContext(self, self._ctx, self.state)
		self.enterRule(localctx, 10, self.RULE_inner_regex)
		try:
			self.enterOuterAlt(localctx, 1)
			self.state = 37
			self.match(RegexParser.OPEN)
			self.state = 38
			self.regex()
			self.state = 39
			self.match(RegexParser.CLOSE)
		except RecognitionException as re:
			localctx.exception = re
			self._errHandler.reportError(self, re)
			self._errHandler.recover(self, re)
		finally:
			self.exitRule()
		return localctx





