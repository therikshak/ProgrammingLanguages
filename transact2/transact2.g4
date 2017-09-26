grammar transact2 ;

transaction : (deposit | withdraw)+ BYE ;
deposit     : ID DEPOSIT NUM
			  {System.out.println("Hey " +$ID.getText() + ", saving money eh?"); } ;
withdraw    : ID WITHDRAW NUM
			  {System.out.println($ID.getText() + " need some cash?"); } ;

DEPOSIT   : 'dep' ;
WITHDRAW  : 'withdraw' ;
BYE       : 'bye' | 'solong' | 'seeya' | 'later' | 'adios' ;
NUM       : DIGIT+ ;
DIGIT     : [0-9] ;
ID        : [a-z]+ | [A-Z] DIGIT DIGIT DIGIT ;
WS        : [ \r\n\t]+ -> skip ;