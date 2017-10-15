grammar banking2 ;

transaction 	: (deposit | withdraw )+  ;
deposit		: ID  DEPOSIT  expr  ;
withdraw	: ID  WITHDRAW expr  ;

expr 
    :   expr MUL expr 		#MUL
    |	expr DIV expr		#DIV
    |	expr ADD expr		#ADD
    |	expr SUB expr		#SUB                                                                            
    |   NUM    			#NUM                          
    |   ID  			#ID     
    |   '(' e=expr ')'          #PARENS
    ;


//LEXER RULES  --------------------------
MUL :   '*' ; 
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;


DEPOSIT 	: 'dep' ;
WITHDRAW 	: 'withdraw' ;
NUM		: DIGIT+ ;
DIGIT		: [0-9]  ;
ID		: [a-z]+ ;
WS		: [ \n\r\t]+ -> skip ;