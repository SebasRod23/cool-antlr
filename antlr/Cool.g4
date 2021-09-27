grammar Cool;           

program
    : ( klass SEMICOLON ) *
    ;

klass
    : KLASS TYPE ( INHERITS TYPE )? OPEN_K ( feature SEMICOLON )* CLOSE_K
    ;

feature
    : ID OPEN_P (formal (COMMA formal)*)? CLOSE_P COLON TYPE OPEN_K expr CLOSE_K # Method
    | ID COLON TYPE (ASSIGN expr)? # Attribute
    ;

formal: ID COLON TYPE;

expr
    : primary # BASE
    |  ...           #simplecall
    | expr (AT TYPE)? DOT ID OPEN_P (expr(COMMA expr)*)? CLOSE_P # OBJECT_CALL
    | IF expr THEN expr ELSE expr FI # IF_ELSE
    | CASE expr OF (ID COLON TYPE CASEASSIGN expr SEMICOLON)+ ESAC # SWITCH
    | WHILE expr LOOP expr POOL # WHILE
    | LET ID COLON TYPE (ASSIGN expr)? (COMMA ID COLON TYPE (ASSIGN expr)?)* IN expr # LET
    | OPEN_K (expr SEMICOLON)+ CLOSE_K # BLOCK
    |  ...           #at
    |  ...           #neg
    | NEW TYPE expr # NEW_OBJECT
    | ISVOID expr # ISVOID
    | expr MULT expr # MULTIPLICATION
    | expr DIV expr # DIVISION
    | expr ADD expr # ADDITION
    | expr SUBS expr # SUBSTRACTION
    | COMP expr # COMPLEMENT
    | expr LT expr # LESS_THAN
    | expr LE expr # LESS_OR_EQUAL
    | expr EQ expr # Equal
    | NOT expr # Not
    | '(' expr ')'
    | ID # Id
    | INT # Integer
    | STRING # String
    | TRUE  # True
    | FALSE # False
    | ID ASSIGN expr # Assign
    ;
/*

case_stat:
    ...
    ;

let_decl:
    ...
    ;


primary:
    ...Son 6 casos...
    ;
 */
fragment A : [aA] ;
fragment C : [cC] ;
fragment L : [lL] ;
fragment S : [sS] ;
fragment I : [iI] ;
fragment N : [nN] ;
fragment H : [hH] ;
fragment E : [eE] ;
fragment R : [rR] ;
fragment T : [tT] ;
fragment O : [oO] ;
fragment V : [vV] ;
fragment D : [dD] ;
fragment W : [wW] ;
fragment P : [pP] ;
fragment F : [fF] ;


KLASS : C L A S S ;
INHERITS : I N H E R I T S ;
ID : [a-z]* ;
TYPE : [A-Z] [a-z]* ;
ASSIGN : '<-' ;
CASEASSIGN : '=>' ;

DOT : '.' ;
COMMA : ',' ;
COLON : ':' ;
SEMICOLON : ';' ;
OPEN_P : '(' ;
CLOSE_P : ')' ;
OPEN_K : '{' ;
CLOSE_K : '}' ;
AT : '@' ;

IF : I F ;
THEN : T H E N ;
ELSE : E L S E ;
FI : F I ;
WHILE : W H I L E ;
LOOP : L O O P ;
POOL : P O O L ;
CASE : C A S E ;
OF : O F ;
ESAC : E S A C ;

LET : L E T ;
IN : I N ;
NEW : N E W ;
ISVOID : I S V O I D ;
MULT : '*' ;
DIV : '/' ;
ADD : '+' ;
SUBS : '-' ;
COMP : '~' ;
LT : '<' ;
LE : '<=' ;
EQ : '=' ;
NOT : N O T ;
INT : [0-9]+ ;
STRING : '"' (('\\'|'\t'|'\r\n'|'\r'|'\n'|'\\"') | ~('\\'|'\t'|'\r'|'\n'|'"'))* '"' ;
TRUE : 'true' ;
FALSE : 'false' ;

SINGLECOMMENT: '--' ~[\r\n]* -> skip;
MULTICOMMENT: '(*' .*? '*)' -> skip;
WS: [ \n\t\r]+ -> skip;