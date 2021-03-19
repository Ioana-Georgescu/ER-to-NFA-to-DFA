# Generated from Regex.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
	with StringIO() as buf:
		buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
		buf.write("%\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
		buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\7\6\32\n\6\f")
		buf.write("\6\16\6\35\13\6\3\7\6\7 \n\7\r\7\16\7!\3\7\3\7\2\2\b\3")
		buf.write("\3\5\4\7\5\t\6\13\7\r\b\3\2\4\3\2c|\4\2\13\f\"\"\2&\2")
		buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
		buf.write("\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5\21\3\2\2\2\7\23\3\2")
		buf.write("\2\2\t\25\3\2\2\2\13\27\3\2\2\2\r\37\3\2\2\2\17\20\t\2")
		buf.write("\2\2\20\4\3\2\2\2\21\22\7*\2\2\22\6\3\2\2\2\23\24\7+\2")
		buf.write("\2\24\b\3\2\2\2\25\26\7~\2\2\26\n\3\2\2\2\27\33\7,\2\2")
		buf.write("\30\32\7,\2\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2")
		buf.write("\2\33\34\3\2\2\2\34\f\3\2\2\2\35\33\3\2\2\2\36 \t\3\2")
		buf.write("\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"#\3")
		buf.write("\2\2\2#$\b\7\2\2$\16\3\2\2\2\5\2\33!\3\b\2\2")
		return buf.getvalue()


class RegexLexer(Lexer):

	atn = ATNDeserializer().deserialize(serializedATN())

	decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

	SYMBOL = 1
	OPEN = 2
	CLOSE = 3
	REUNION = 4
	KLEENE = 5
	WHITESPACE = 6

	channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

	modeNames = [ "DEFAULT_MODE" ]

	literalNames = [ "<INVALID>",
			"'('", "')'", "'|'" ]

	symbolicNames = [ "<INVALID>",
			"SYMBOL", "OPEN", "CLOSE", "REUNION", "KLEENE", "WHITESPACE" ]

	ruleNames = [ "SYMBOL", "OPEN", "CLOSE", "REUNION", "KLEENE", "WHITESPACE" ]

	grammarFileName = "Regex.g4"

	def __init__(self, input=None, output:TextIO = sys.stdout):
		super().__init__(input, output)
		self.checkVersion("4.7.2")
		self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
		self._actions = None
		self._predicates = None


