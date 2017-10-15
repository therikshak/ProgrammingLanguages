grammar triplegen;

phrase : word+ ;

word: L1 L2 L3 ;

L1: [bcdfgmnpr] ;
L2: [aeiou] ;
L3: [dgnprstwxyz] ;
WS: [ \t\n\r]+ -> skip ; 