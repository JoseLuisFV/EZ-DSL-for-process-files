from lark import Lark
from grammar import grammar
from evaluator import Evaluador
       
parser = Lark(grammar, parser='lalr', transformer=Evaluador())


def evaluate(expression):
  try:
    result = parser.parse(expression)
    return result
  except Exception as e:
    return f"Error: {e}"
  

print(evaluate("generate 'copy' PROPS" +"{" + "format: 'audio', startwith: 'pe'," + "}" + "  from archivo.txt"))