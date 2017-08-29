grammar saystuff;

stmt      : hellostmt | byestmt | infostmt ;
infostmt  : HELLOTOK TITLE ID VERB DESCR ;
hellostmt : HELLOTOK TITLE ID ;
byestmt   : BYETOK TITLE ID ENDTOK* ;

HELLOTOK  : 'hi' | 'hello' | 'greetings' | 'hey' ;  
TITLE     : 'mr' | 'ms' | 'doctor' | 'sir' ;
BYETOK    : 'bye' | 'sayanora' ;
ENDTOK    : 'later' ;
VERB      : 'runs' | 'jumps' | 'climbs' | 'walks' ;
DESCR     : 'fast' | 'high' | 'slow' | 'poorly' ;
ID        : [a-x]+ ;
WS        : [ \t\r\n]+ -> skip ;