grammar tarzan2;

sentence: statement+  ;

statement : PERSON  VERB   phrase?    #PEOPLEFACT
	|   PLACE   ADJECTIVE 	      #PLACEFACT
	|   QUERY   PERSON 	      #PERSONQUERY
	|   QUERY   PLACE	      #PLACEQUERY
	;

phrase   : CONJ  PLACE ;



PERSON 	  :  'tarzan' | 'jane' | 'cheeta' ;
VERB      :  'run' | 'jump' | 'play' | 'swim' ;
PLACE     :  'river' | 'tree' | 'jungle' | 'swamp' ;
CONJ      :  'in' | 'by' | 'at' ;
QUERY     :  'what about'     ;
ADJECTIVE :  'pretty' | 'well' | 'bad' ;
WS        :   [ \r\n\t]+ -> skip ; // toss out whitespace