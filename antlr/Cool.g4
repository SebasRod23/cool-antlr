grammar Cool;           

program
    : ( klass ';' ) *
    ;

// Esta regla está mal, solo es para poder generar un parser y probar
klass
    : KLASS
    ;

/*
 * Aquí comenzaría el léxico
 */


fragment A : [aA] ;
fragment C : [cC] ;
fragment L : [lL] ;
fragment S : [sS] ;

KLASS : C L A S S ;

