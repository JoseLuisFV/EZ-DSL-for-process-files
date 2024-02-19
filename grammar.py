grammar = """

start: expr

expr: operation

operation:  [extract | generate | locate] props? "from" filename props?

extract: "extract" action
generate: "generate" action
locate: "locate" action

action: "'" ALPHABET "'"

props: "PROPS" "{" prop+ "}"

prop:  ALPHANUMERIC ":"  "'" ALPHANUMERIC "'"  ","
filename: ALPHANUMERIC

ALPHABET: /[a-zA-Z]+/
ALPHANUMERIC: /[a-zA-Z0-9_\-.]+/


%import common.WS
%ignore WS
"""