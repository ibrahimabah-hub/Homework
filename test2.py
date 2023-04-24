def check(same, tokens):
  global curToken
  if(curToken==same):
    if(len(tokens)>1):
      tokens=tokens[1:]
      curToken=tokens[0]
      return True
    else:
      curToken=None
      return True

def stmtList(tokens):
  if(curToken==None):
    return False
  stmt(tokens)
  while(curToken==';'):
    check(';', tokens)
    stmt(tokens)
    
def tokenize(tokens):
  global curToken
  curToken = newList[0]
  stmtList(tokens)
  return curToken==None
  
def stmt(tokens):
  if(curToken==None):
    return False
  elif(curToken=='if'):
    ifStmt(tokens)
  elif(curToken=='while'):
    whileLoop(tokens)
  elif(curToken=='{'):
    block(tokens)
  elif(curToken=='int' or curToken=='String' or curToken=='float' or curToken=='boolean' or curToken=='char'):
    declare(tokens)
  else:
    expr(tokens)
    
def declare(tokens):
  if(curToken==None):
    return False
  elif(curToken=='int' or curToken=='String' or curToken=='float' or curToken=='boolean' or curToken=='char'):
    check(curToken, tokens)
    check(curToken, tokens)
    while(curToken==','):
      check(',', tokens)
      check(curToken, tokens)

def whileLoop(tokens):
  if(curToken==None):
    return False
  else:
    check('while', tokens)
    check('(', tokens)
    boolExpr(tokens)
    check(')', tokens)
    if(curToken=='{'):
      block(tokens)
    else:
      stmt(tokens)
      check(';', tokens)

def ifStmt(tokens):
  if(curToken==None):
    return False
  else:
    check('if', tokens)
    check('(', tokens)
    boolExpr(tokens)
    check(')', tokens)
    if(curToken=='{'):
      block(tokens)
    else:
      stmt(tokens)
      check(';', tokens)
    if(curToken=='else'):
      check('else')
      if(curToken=='{'):
        block(tokens)
      else:
        stmt(tokens)
        check(';', tokens)

def block(tokens):
  if(curToken==None):
    return False
  check('{', tokens)
  stmtList(tokens)
  check('}', tokens)

def expr(tokens):
  if(curToken==None):
    return False
  term(tokens)
  while(curToken=='+' or curToken=='-'):
    if(curToken=='+'):
      check('+', tokens)
    else:
      check('-', tokens)
    term(tokens)

def term(tokens):
  if(curToken==None):
    return False
  fact(tokens)
  while(curToken=='*' or curToken=='/' or curToken=='%'):
    if(curToken=='*'):
      check('*', tokens)
    elif(curToken=='%'):
      check('%', tokens)
    else:
      check('/', tokens)
    fact(tokens)

def fact(tokens):
  global curToken
  if(curToken==None):
    return False
  if(curToken=='('):
    check('(')
    expr(tokens)
    check(')')
  else:
    if(len(tokens)>1):
      tokens=tokens[1:]
      curToken=tokens[0]
    else:
      curToken=None

def boolExpr(tokens):
  if(curToken==None):
    return False
  bterm(tokens)
  while(curToken=='>' or curToken=='<' or curToken=='>=' or curToken=='<='):
    if(curToken=='>'):
      check('>', tokens)
    elif(curToken=='<'):
      check('<', tokens)
    elif(curToken=='>='):
      check('>=', tokens)
    else:
      check('<=', tokens)
    bterm(tokens)

def bterm(tokens):
  if(curToken==None):
    return False
  band(tokens)
  while(curToken=='==' or curToken=='!='):
    if(curToken=='=='):
      check('==', tokens)
    else:
      check('!=', tokens)
    band(tokens)

def band(tokens):
  if(curToken==None):
    return False
  bor(tokens)
  while(curToken=='&&'):
    check('&&', tokens)
    bor(tokens)

def bor(tokens):
  if(curToken==None):
    return False
  expr(tokens)
  while(curToken=='||'):
    check('||', tokens)
    expr(tokens)

newList=['Hello', ';']
if(tokenize(newList)):
  print('correct')
else:
  print('incorrect')