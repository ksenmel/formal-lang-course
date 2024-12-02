from antlr4 import InputStream, CommonTokenStream, ParserRuleContext, TerminalNode
from antlr4.error.ErrorListener import ErrorListener

from project.parser.GQLLexer import GQLLexer
from project.parser.GQLParser import GQLParser


class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.has_errors = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_errors = True


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


def tree_to_program(tree: ParserRuleContext) -> str:
    return "".join(
        child.getText() + " "
        if isinstance(child, TerminalNode)
        else tree_to_program(child)
        for child in tree.children
    )
