# What is pstone?

ToDo: Fix Me

## Prerequisite

* Python 3.3 or higher

## Install

```
pyvenv /PATH/TO/pstone
source /PATH/TO/pstone/bin/activate
```

## Memo

```
primary   : "(" expr ")" | NUMBER | IDENTIFIER | STRING
factor    : "-" primary | primary
expr      : factor { OP factor }
block     : "{" [ statement ] {(";" | EOL) [ statement ]} "}"
simple    : expr
statement : "if" expr block [ "else" block ]
          | "while" expr block
          | simple
program   : [ statement ] (";" | EOL)
```
