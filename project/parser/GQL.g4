grammar GQL;

prog : stmt* ;

stmt: declare
    | bind
    | add
    | remove;

declare : LET var IS GRAPH ;

bind : LET var EQUAL expr ;

remove : REMOVE (VERTEX | EDGE | VERTICES) expr FROM var ;

add : ADD (VERTEX | EDGE) expr TO var ;

expr : num | char | var | edge_expr | set_expr | regexp | select ;

set_expr : L_SQ_BR expr (COMMA expr)* R_SQ_BR ;

edge_expr : L_BR expr COMMA expr COMMA expr R_BR ;

regexp: char
        | var
        | L_BR regexp R_BR
        | regexp CIRCUMFLEX range
        | regexp DOT regexp
        | regexp PIPE regexp
        | regexp AMPERSAND regexp;

range : L_SQ_BR num ELLIPSIS num? R_SQ_BR ;

select : v_filter? v_filter? RETURN var (COMMA var)? WHERE var REACHABLE FROM var IN var BY expr ;

v_filter : FOR var IN expr ;

num: NUM ;
char: CHAR;
var: VAR ;

LET:            'let' ;
IS:             'is' ;
GRAPH:          'graph' ;
REMOVE:         'remove' ;
WHERE:          'where' ;
REACHABLE:      'reachable' ;
RETURN:         'return' ;
BY:             'by' ;
VERTEX:         'vertex' ;
EDGE:           'edge' ;
VERTICES:       'vertices' ;
FROM:           'from' ;
ADD:            'add' ;
TO:             'to' ;
FOR:            'for' ;
IN:             'in' ;

EQUAL:          '=' ;
L_SQ_BR:        '[' ;
L_BR:           '(' ;
R_SQ_BR:        ']' ;
R_BR:           ')' ;
COMMA:          ',' ;
CIRCUMFLEX:     '^' ;
DOT:            '.' ;
AMPERSAND:      '&' ;
ELLIPSIS:       '..' ;
PIPE:           '|' ;

VAR : [a-zA-Z] [a-zA-Z0-9]* ;
NUM : [0-9]+ ;
CHAR : '"' [a-z] '"' | '\'' [a-z] '\'' ;

WS : [ \t\r\n]+ -> skip ;