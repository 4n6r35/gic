import nltk

# Definir la gramática para la estructura condicional
grammar = nltk.CFG.fromstring("""
    A -> 'V' ' ' '(' C ')' ' ' P  ' ' 'S'  ' ' P  ' ' 'V'
    C -> S  ' '  O  ' ' S
    O -> '>' | '>''=' | '<' | '<''=' | '=' | '=''=' | '~''='
    P -> Q PP
    PP -> '+' Q PP | '-' Q PP |
    Q -> S QQ
    QQ -> '*' S QQ | '/' S QQ |
    S -> V | K
    V -> l T
    T -> l T | d T | '_' l T | '_' d T | '_' |
    K -> E | E '.' E
    E -> d E | d
    l -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
    d -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")

# Crear un analizador sintáctico
parser = nltk.RecursiveDescentParser(grammar)

# Definir una cadena de prueba
# cadena = "V (y_5b_ = y_y6) 1+b-5/3*0.5-5+10 S var_66/b6 V"
# cadena = "I (y_5b > y_y6) 1+b-5/3 L nzgn_66/b6 D"

cadena= "a + b * 3 / c"

# Realizar el análisis sintáctico
word = list(cadena)
trees = list(parser.parse(word))

class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'


# Verificar si se encontraron árboles de análisis sintáctico
if trees:
    for tree in trees:
        # tree.pretty_print()
        print(f"{colors.GREEN}La cadena es válida según la gramática.{colors.END}")
else:
    print(f"{colors.RED}La variable no coincide con la gramática. {colors.END}")
