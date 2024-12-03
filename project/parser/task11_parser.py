from antlr4 import InputStream, CommonTokenStream, ParserRuleContext, TerminalNode, ParseTreeListener, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener

from project.parser.GQLLexer import GQLLexer
from project.parser.GQLParser import GQLParser


class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.has_errors = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_errors = True


class NodeCountListener(ParseTreeListener):
    def __init__(self):
        self.count = 0

    def enterEveryRule(self, ctx):
        self.count += 1


class TreeToProgramListener(ParseTreeListener):
    def __init__(self) -> None:
        self.result = []

    def visitTerminal(self, node: TerminalNode) -> None:
        self.result.append(node.getText() + " ")

    def getProgram(self) -> str:
        # Собираем результат в одну строку
        return "".join(self.result)


def program_to_tree(program: str) -> tuple[ParserRuleContext, bool]:
    input_stream = InputStream(program.replace("<EOF>", "EOF"))
    error_listener = SyntaxErrorListener()

    lexer = GQLLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = GQLParser(tokens)

    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    tree = parser.prog()

    if error_listener.has_errors:
        return None, False
    return tree, True


def nodes_count(tree: ParserRuleContext) -> int:
    node_listener = NodeCountListener()
    walker = ParseTreeWalker()
    walker.walk(node_listener, tree)
    return node_listener.count


def tree_to_program(tree: ParserRuleContext) -> str:
    listener = TreeToProgramListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.getProgram()
