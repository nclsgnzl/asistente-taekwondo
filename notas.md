# asistente-taekwondo

¿Qué es un token y por qué el modelo no "ve" palabras?
¿Qué es el context window?
¿Qué es temperature?
¿Por qué alucina un LLM?
¿Diferencia entre modelo base e instruction-tuned?

Mis respuestas:

el token es la transformación de los datos que introducimos en carácteres que se ven leyendo para formar patrones, y esos patrones hacen que te den una respuesta, es como un codigo binario el cual por cada palabra o letra se transforma en un token para luego buscar un patrón o secuencia que sea similar para luego dar una respuesta.

el context window es el contexto por ventana o el contexto que está dentro de un chat, tiene un límite y ese límite se basa en todo lo que se ha conversado o trabajado en ese contexto, digamoslo así como una memoria a corto plazo, dentro de un contexto.

la temperatura es el nivel en el cual un modelo puede responder de forma creativa o bien de forma certera, si la temperatura se le da un nivel alto puede ser más creativo, pero si no tiene temperatura da respuestas exactas sin adornos o relleno.

alucina un LLM debido a que puede ser por el contexto que tiene con la memoria a corto plazo y luego de ir añadiendo más ideas sobre la misma conversación puede mezclar ideas y formar una respuesta erroneo, como también en que el modelo se basa en un patrón de respuesta donde puede dar la respuesta, pero no la información correcta, ya que tiene a basarse en un factor de recompensa, por ejemplo si yo pregunto X, puede decirme X significa esto erroneamente, pero debe tener un contexto o darle una mejor instrucción para que no alucine y el mismo contexto que tenga dentro de la conversación no se salga de la idea prinicipal.

modelo base es un modelo que responde preguntas a respuestas, pero un modelo ajustado o instruction tuned, es un modelo que tiene la información para responder, pero que a su vez responde de una forma legible para el usuario, tiene ajustes y habilidades para que la respuesta sea acorde a lo que necesite el usuario

Respuestas corregidas:

Buen trabajo en general — captaste la intuición correcta en la mayoría. Te marco dónde afinar, porque estos matices sí importan en una entrevista técnica:

1. Tokens — parcialmente correcto, pero mezclaste dos ideas distintas. El tokenizar es solo el paso de dividir el texto en unidades (palabras, sub-palabras o caracteres) y convertirlas en números — eso es todo, es una transformación mecánica de texto a IDs numéricos. La búsqueda de "patrones para dar una respuesta" es un proceso distinto y posterior (la predicción del modelo). No es como código binario tampoco — es más simple: piensa en un diccionario gigante donde cada fragmento de texto tiene asignado un número, y el modelo trabaja con esos números, no con letras.

2. Context window — bien. La analogía de memoria a corto plazo es correcta y es justo cómo se explica en la industria. Un dato que te falta: se mide en tokens, no en "mensajes" — por eso documentos largos consumen contexto rápido.

3. Temperature — correcto, sin correcciones. Buena síntesis.

4. Alucinaciones — aquí hay una confusión importante que quiero que te quede clara. Mencionaste "factor de recompensa" — eso es un concepto de cómo se entrena el modelo (RLHF), no la causa directa de la alucinación en el momento de responder. La causa real y más simple: el modelo genera texto prediciendo la palabra estadísticamente más probable, no consultando una base de datos de "verdad". Si nunca aprendió el dato real, igual va a generar algo fluido y con apariencia correcta, porque su trabajo es "sonar coherente", no "saber". No es que "mezcle ideas de la conversación" principalmente — puede pasar eso también, pero la raíz de fondo es que no tiene un mecanismo interno para distinguir "sé esto con certeza" de "esto suena plausible".

5. Base vs instruction-tuned — la intuición está bien encaminada, pero vaga. Más preciso: un modelo base solo continúa texto siguiendo patrones de su entrenamiento (le das "El cielo es" y completa "...azul", sin necesariamente entender que le estás haciendo una pregunta). Un modelo instruction-tuned (como Claude) fue entrenado específicamente con ejemplos de instrucción→respuesta útil y con feedback humano (RLHF) para seguir instrucciones, ser útil y evitar respuestas dañinas — no es solo "legibilidad", es un entrenamiento adicional con propósito específico.
