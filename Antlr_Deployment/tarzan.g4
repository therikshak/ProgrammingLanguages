grammar tarzan ;
stmt: noun verb mod;
noun: 'tarzan' | 'jane' ;
verb: 'run' | 'jump' ;
mod: 'slowly' | 'high' | 'fast' ; 

WS:   [ \t\n\r]+ -> skip ;