import nltk

# Definir la gramática corregida
grammar = nltk.CFG.fromstring("""
    A -> V Assign E
    E -> T | T Operator E
    T -> P | T Term P
    P -> V | '(' E ')'
    V -> l W
    W -> W' | '_'
    W' -> l W' | d W' | '_' l W' | '_' d W' | ''
    Assign -> '='
    Operator -> '+' | '-' | '*' | '/'
    Term -> '*' | '/'
    l -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
    d -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")


# Crear un analizador sintáctico
parser = nltk.RecursiveDescentParser(grammar)

# Definir la cadena de prueba
cadena = "a + b * 3 / c"

# Realizar el análisis sintáctico
words = cadena.split()
trees = list(parser.parse(words))

class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

# Verificar si se encontraron árboles de análisis sintáctico
if trees:
    for tree in trees:
        print(f"{colors.GREEN}La cadena es válida según la gramática.{colors.END}")
else:
    print("La cadena no coincide con la gramática.")
