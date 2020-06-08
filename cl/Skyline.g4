grammar Skyline;

prog: stat+ ;

stat:   skyline                  # printSkyline
    |   ID ':=' skyline          # assign
    ;

skyline:   '(' skyline ')'                                   # parens
    |      '-' skyline                                       # reflection
    |      skyline '*' skyline                               # Intersection
    |      skyline '*' INT                                   # Replication
    |      skyline '+' skyline                               # Union
    |      skyline '+' INT                                   # Desp
    |      '(' INT ',' INT ',' INT ')'                       # EdificiSimple
    |      '[' skyline_sets ']'                              # EdificisCompostos
    |      '{' INT ',' INT ',' INT ',' INT ',' INT '}'       # EdificisAleatoris
    |      ID                                                # id
    ;

skyline_sets: '(' INT ',' INT ',' INT '),' skyline_sets
    |      '(' INT ',' INT ',' INT ')'
    ;

PLUS :   '+' ;           // assigns token name to '+' used above in grammar
ESTRELLA :   '*' ;
ID  :   [a-zA-Z]+[a-zA-Z0-9]* ;      // match identifiers
INT :   [0-9]+ ;         // match integers
WS  :   [ \t]+ -> skip ; // toss out whitespace
