from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream

from project.interpreter.visitor import MyVisitor
from project.typeinference.infer import GLTypesInferencer
from project.parser.GQLLexer import GQLLexer
from project.parser.GQLParser import GQLParser


def typing_program(program: str) -> bool:
    lexer = GQLLexer(InputStream(program))
    stream = CommonTokenStream(lexer)
    parser = GQLParser(stream)

    tree = parser.prog()

    types_visitor = GLTypesInferencer()

    try:
        types_visitor.visit(tree)
        return True
    except Exception:
        return False


def exec_program(program: str) -> dict[str, set[tuple]]:
    lexer = GQLLexer(InputStream(program))
    stream = CommonTokenStream(lexer)
    parser = GQLParser(stream)

    tree = parser.prog()

    runner_visitor = MyVisitor()

    try:
        runner_visitor.visit(tree)
        return runner_visitor.query
    except Exception:
        return {}
