# CYBERAPOCALYPSE 2021 - CRYPTO PS2

Hace unas semanas se realizó el CTF "CyberApocalypse 2021" organizado por la plataforma Hack The Box. Uno de los problemas que se colocaron en este Capture The Flag fue "crypto_ps2". El nombre viene de criptografía que es la sección a la que pertenece este reto y ps2 proviene de la temática de estos ejercicios que estaban relacionados a consolas de videojuegos.

<img src="https://images-na.ssl-images-amazon.com/images/I/4116HYcMH0L._SX342_.jpg"/>

El reto entregaba el archivo output.txt que pueden encontrarlo en la misma carpeta que este archivo .md. La pista que nos otorgaba el reto es que se usó el cifrado XOR. Como ya es sabido una de las principales propiedad, por no decir la principal, es que la operación XOR puede aplicarse de ida y vuelta. En otras palabras, si a XOR b es c, entonces b XOR c es a y a XOR c es b. Bajo esta propiedad buscaremos encontrar nuestra flag.

<img src="https://i.pcmag.com/imagery/encyclopedia-terms/xor-xor.fit_lim.size_1050x.gif"/>

Lo primero en que tenemos que enfocarnos es en qué deseamos encontrar y cómo reconocer que eso es lo que buscamos. Para el caso de este tipo de retos se busca una flag que tiene una estructura conocida. Para este caso la estructura de flag es la siguiente: "CHTB{fl4g}". Sabiendo esto notamos que buscamos una cadena de caracteres que contenga al menos los caracteres C, H, T, B, { y }.

Revisando el .txt entregado notamos que hay 10000 líneas de texto. Con el fin de no hacer una fuerza bruta muy forzada podemos intentar de muchas formas encontrar los caracteres que se mencionaron en el párrafo anterior. La forma que explicaré en este solucionario es asumiendo que la flag se encuentra en solo una línea en su orden natural, es decir, el primer caracter será C y el segundo H. De esta manera, obtendremos lo siguiente:

Sea c una cadena de texto en hexadecimal que representa el texto cifrado para la flag representada por p y k la llave de tamaño 1 byte, consideramos que:

c<sub>1</sub>c<sub>2</sub> XOR k<sub>1</sub>k<sub>2</sub> = 43 (C en hex.) <==> c<sub>1</sub>c<sub>2</sub> XOR 43 = k<sub>1</sub>k<sub>2</sub>

c<sub>3</sub>c<sub>4</sub> XOR k<sub>1</sub>k<sub>2</sub> = 48 (H en hex.) <==> c<sub>3</sub>c<sub>4</sub> XOR 48 = k<sub>1</sub>k<sub>2</sub>

Entonces:

c<sub>1</sub>c<sub>2</sub> XOR 43 = c<sub>3</sub>c<sub>4</sub> XOR 48

c<sub>1</sub>c<sub>2</sub> XOR 43 XOR 43 = c<sub>3</sub>c<sub>4</sub> XOR 48 XOR 48

c<sub>1</sub>c<sub>2</sub> XOR 0 = c<sub>3</sub>c<sub>4</sub> XOR b

c<sub>1</sub>c<sub>2</sub> = c<sub>3</sub>c<sub>4</sub> XOR b

Con eso resuelto, se hace una fuerza bruta con las 10000 líneas de texto hasta encontrar dicha condición. Sin embargo, eso no garantiza que solo obtendremos un resultado. Así que usaremos la llave generada que para entonces será conocida para desencriptar las opciones de flag. Para esto solo usaré c<sub>5</sub>c<sub>6</sub> para encontrar el caracter "T" que sería el siguiente. Bien, una vez hecho esto encontraremos la línea que corresponde a la flag y la llave. Finalmente, el código fuente de esta solución podrán encontrarlo en esta carpeta como "bruteforcexor.py". Con este ya tendrás tanto la flag encriptada y su llave en hexadecimal, tu único trabajo será desencriptarla. Espero haber sido suficientemente didáctico y que te haya gustado este solucionado. Un saludo.
