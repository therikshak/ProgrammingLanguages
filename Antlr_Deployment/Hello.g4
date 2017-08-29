grammar Hello ;
stmt : 'hello' ID ;
ID   : [a-z]+ ;
WS   : [ \t\n\r] -> skip ;