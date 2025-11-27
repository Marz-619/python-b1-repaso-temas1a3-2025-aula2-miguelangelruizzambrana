"""El objetivo general del ejercicio es crear una serie de funciones que nos permitan realizar operaciones 
sobre un texto.

Para este ejercicio, no se debe usar la función split de Python. En vez de ello, deberás  usar las 
siguientes funciones auxiliares que serán de gran ayuda al resolver el ejercicio. Asimismo, se pueden 
elegir crear nuevas funciones adicionales. A continuación, presentaremos una descripción de estos métodos:

* is_newline(character): Es una función que detecta el final de una oración. Deberás suponer que las frases 
están separadas por "\n" (nueva línea). Si el carácter es este símbolo, devolverá True.

* is_space(character): Es una función que detecta si un carácter es un espacio en blanco. Si el carácter es 
este símbolo, devolverá True.

* remove_punctuation_marks(cad): Una función que elimina los signos de puntuación de una palabra o un texto. 
Este método devuelve como resultado una cadena de caracteres sin signos de puntuación.

Las funciones descritas en el apartado anterior forman parte del módulo denominado 'text_manager.py', por lo tanto, 
es preciso importar estas en el módulo 'ejb1_x1_main.py', el cual es el módulo principal en el que desarrollaremos 
nuestra solución. 
En este ejercicio utilizaremos  la variable "TEXT" de tipo cadena de caracteres(definida en el módulo text_manager.py), 
la cual será empleada en cada una de las siguientes funciones como parámetro. Los métodos que se solicita 
desarrollar son:

* find_largest_word(text): Un método que permite detectar la palabra más larga en un texto. Este método debe 
devolver como resultado una cadena de caracteres correspondiente a la palabra más larga. Al evaluar la palabra
no debe contener signos de puntuación. 

* is_palindrome_word(word): Es una función recursiva que nos permitirá detectar si una palabra es palíndromo. 
Un palíndromo es una palabra que se lee igual en un sentido que en otro. Por ejemplo las siguientes palabras son 
palíndromos: Ata; Aviva; Azuza; Apa; Afromorfa. Para el ejercicio, el texto se encuentra en lengua inglesa, 
por lo que no se requiere realizar ningún tipo de acción en relación con tildes o acentos. Al evaluar la palabra 
no debe contener signos de puntuación. El valor que devuelve es de tipo booleano. Si es un palíndromo devolverá 
"True", y en el caso contrario "False". 

* count_palindrome_words(text): Se trata de una función que nos permitirá enumerar las apariciones de palíndromos 
en el texto, por lo tanto, esta retorna un número entero. Para esto debemos hacer uso de la anterior 
función is_palindrome_word(word).

* find_size_largest_sentence(text, filter): Se trata de una función que permite encontrar el tamaño de la oración 
más larga cuyo valor de filtro esté en esa sentencia. Si no existe una oración que coincida con el filtro deberá 
lanzar una excepción del tipo ValueError. El valor a retornar es un número entero que representa la longitud de 
la cadena en cuestión. 
Por ejemplo: si se invoca a la función con los parámetros text = "Hola, Pepe.\n¿Cómo estás, amigo?", el parámetro
filter = "a", este debe devolver 19, ya que en la segunda oración "¿Cómo estás, amigo?", se encuentra incluido 
el valor pasado como filtro y la oración tiene una longitud de la cadena de texto más larga. 
"""
# Add your imports here
from util_package import text_manager 
from util_package.text_manager import TEXT
from util_package.text_manager import is_newline
from util_package.text_manager import is_space 
from util_package.text_manager import remove_punctuation_marks

def find_largest_word(text):
    longest_word = "" #Inicializamos la palabra más larga que se devolverá
    aux_word = "" #Inicializamos variable auxiliar para realizar la comparación de las palabras
    for letra in text: #Recorremos el texto completo
        if (is_space(letra)==False and is_newline(letra)==False):
            # Indica que el caracter es una letra o signo de puntuación y no un espacio ó salto de linea
            aux_word = aux_word+letra #Añadimos la letra a la palabra a evaluar
        else: #Indica que ya hemos llegado a un espacio o salto de linea, osea que la palabra está completa
            aux_word = remove_punctuation_marks(aux_word) #Eliminamos simbolos
            if (len(aux_word)>len(longest_word)): #La nueva palabra es la más grande por ahora del texto
                longest_word = aux_word
            aux_word = "" #Reseteamos palabra para una nueva iteración
    # Si la frase no termina en espacio o en newline no se evalúa la última palabra
    # Se añade el check para la última palabra
    aux_word = remove_punctuation_marks(aux_word) #Eliminamos simbolos
    if (len(aux_word)>len(longest_word)): 
        longest_word = aux_word

    return longest_word



def is_palindrome_word(word):
    word = word.lower() # Convertimos todo a minúsculas para que no haya problemas de comparación 
    if len(word)<1: # La palabra sólo tiene 1 caracter, es palindromo
        return True
    if word[0] != word[len(word)-1]: # Evalúa si el primer y útimo caracter son iguales
        return False
    
    return is_palindrome_word(word[1:len(word)-1]) # Volvemos a iterar acortando la cadena   
    


def count_palindrome_words(text):
    cnt_palindromes = 0 # Incializamos a 0 el contador de palabras palídroma
    palabra = "" # Variable auxiliar para almacenar las palabras del texto
    for letra in text: # Recorremos el texto completo
        if (is_space(letra)==False and is_newline(letra)==False): 
            palabra = palabra + letra # Indica que el caracter es una letra o signo de puntuación y no un espacio ó salto de linea
        else: #Indica que ya hemos llegado a un espacio o salto de linea, osea que la palabra está completa
            palabra = remove_punctuation_marks(palabra) #Eliminamos los signos de puntuación
            if (len(palabra)>0 and is_palindrome_word(palabra)==True): 
                # Revisamos que la palabra sea palindromo y que no sea una palabra vacía
                # Pues puede darse el caso que tras eliminar simbolos, se quede la palabra vacía
                # Como puede ser con el &, y lo cuente como palíndromo
                cnt_palindromes += 1
            palabra = "" # Reseteamos la palabra para una nueva palabra a crear
    # Si la frase no termina en espacio o en newline no se evalúa la última palabra
    # Se añade el check para la última palabra
    palabra = remove_punctuation_marks(palabra) # Eliminamos primero signos de puntuación
    if (len(palabra)>0 and is_palindrome_word(palabra)==True): 
        cnt_palindromes += 1
    
    return cnt_palindromes


def find_size_largest_sentence(text, filter):
    longest_sentence = "" # Inicializamos la frase más larga con el filter incluido
    aux_sentence = "" # Inicializamos cadena auxiliar
    for palabra in text: # Recorremos el texto completo
        if (is_newline(palabra)==False): # Mientras no haya salto de linea es una misma frase
            aux_sentence += palabra
        else: # He llegado al fin de una línea, evalúo esa frase
            if ((filter in aux_sentence)): #El filtro está dentro de mi frase
                if (len(aux_sentence)>len(longest_sentence)): 
                    # La nueva cadena con filter es más grande que la anterior
                    longest_sentence = aux_sentence
            aux_sentence = "" # Reseteo la frase auxiliar
    print(longest_sentence)
    if (len(longest_sentence)==0): # Ninguna frase contiene el filtro, lanzo error
        raise ValueError(f"Longitud de la cadena en cuestión:  {len(filter)}")
    return len(longest_sentence)


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
#print("La palabra mas larga es:", find_largest_word(TEXT))
#print("'aa' es un palíndromo su resultado es:", is_palindrome_word("aa"))
#print("'abx' no un palíndromo su resultado es:", is_palindrome_word("abx"))
#print("'a' es un palíndromo su resultado es:", is_palindrome_word("a"))
#print("'Ababa' es palíndromo su resultado es:", is_palindrome_word("Ababa"))
#print("El número de palabras identificadas como palíndromos es:", count_palindrome_words("civic, radar, level, rotor, kayak, madam, and refer."))
#print("El tamaño de la oración más larga con el filtro='a', es :", find_size_largest_sentence(TEXT, "melon"))
