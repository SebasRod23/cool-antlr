grammar Cool;           

program
    : ( klass SEMICOLON ) *
    ;

klass
    : KLASS TYPE ( INHERITS TYPE )? OPEN_K ( feature SEMICOLON )* CLOSE_K
    ;

feature
    : ID OPEN_P (formal (COMMA formal)*)? CLOSE_P COLON TYPE OPEN_K expr CLOSE_K # METHOD
    | ID COLON TYPE (ASSIGN expr)? # ATTRIBUTE
    ;

formal: ID COLON TYPE;

expr
    : primary # BASE // base
    | expr (TYPE)? DOT simplecall # OBJECT_CALL // objectcall
    | IF expr THEN expr ELSE expr FI # IF_ELSE // if
    | CASE expr OF (case_stat)+ ESAC # SWITCH // case
    | WHILE expr LOOP expr POOL # WHILE // while
    | LET ID COLON TYPE (ASSIGN expr)? (let_decl)* IN expr # LET // let
    | OPEN_K (expr SEMICOLON)+ CLOSE_K # BLOCK // block
    | expr (AT TYPE)? DOT simplecall #AT //at
    | NEW TYPE expr # NEW_OBJECT // new
    | ISVOID expr # ISVOID // isvoid
    | expr MULT expr # MULTIPLICATION // mult
    | expr DIV expr # DIVISION // div
    | expr ADD expr # ADDITION // plus
    | expr SUBS expr # SUBSTRACTION // less
    | COMP expr # COMPLEMENT // neg
    | expr LT expr # LESS_THAN // lt
    | expr LE expr # LESS_OR_EQUAL // le
    | expr EQ expr # EQUAL // eq
    | NOT expr # NOT // not 
    | ID ASSIGN expr # ASSIGN // assign
    ;

simplecall
    : ID OPEN_P (expr(COMMA expr)*)? CLOSE_P # SIMPLE_CALL
    ;

case_stat
    : ID COLON TYPE CASEASSIGN expr SEMICOLON # CASE_STAT
    ;

let_decl
    : COMMA ID COLON TYPE (ASSIGN expr)? # LET_DECL
    ;

primary
    : OPEN_P expr CLOSE_P # PARENTHESIS 
    | ID # ID
    | INT # INTEGER
    | STRING # STRING
    | TRUE  # TRUE
    | FALSE # FALSE
    ;

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
ID : [a-z]+ ;
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