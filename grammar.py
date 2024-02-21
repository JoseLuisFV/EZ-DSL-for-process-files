grammar = """

start: expr

expr: operation

operation:  [extract | generate | locate] "from" filename

extract: "extract" action props? 
generate: "generate" action props? 
locate: "locate" action props? 

action: "'" ALPHABET "'"

props: "PROPS" "{" prop+ "}"

prop:  ALPHANUMERIC ":"  "'" ALPHANUMERIC "'"  ","
filename: ALPHANUMERIC

ALPHABET: /[a-zA-Z]+/
ALPHANUMERIC: /[a-zA-Z0-9_\-.]+/


%import common.WS
%ignore WS
%ignore /\s+/
"""