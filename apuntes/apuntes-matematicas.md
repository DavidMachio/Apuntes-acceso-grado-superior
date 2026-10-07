[CABECERA DE ETIQUETAS — no imprimir]
Etiquetas de bloque: PORTADA, INICIO SECCIÓN / FIN SECCIÓN, EJEMPLO, MÉTODO ALTERNATIVO, FÓRMULA DESTACADA, TABLA, LISTA, LISTA NUMERADA, LEYENDA (abren y cierran con [/...]).
Etiquetas de línea: ANTETÍTULO, TÍTULO DOCUMENTO, SUBTÍTULO DOCUMENTO, TEXTO INTRODUCTORIO, TÍTULO APARTADO, SUBTÍTULO, TEXTO, NOTA, DESTACADO, FÓRMULA, IMAGEN, DIAGRAMA.
Fórmulas en LaTeX: la línea [FÓRMULA] es fórmula en bloque; $...$ dentro de un texto es fórmula en línea. "EJ." y "R." son rótulos de ejemplo y de respuesta. Imágenes en la carpeta imagenes/.
[/CABECERA DE ETIQUETAS]

[PORTADA]

[ANTETÍTULO] Apuntes transcritos

[TÍTULO DOCUMENTO] Matemáticas aplicadas

[SUBTÍTULO DOCUMENTO] Porcentajes · Cantidades iniciales y finales · Variaciones · Interés simple y compuesto · Proporcionalidad · Tablas y gráficas

[TEXTO INTRODUCTORIO] Transcripción de 31 fotografías (archivador y cuaderno, septiembre–octubre 2026), con los ejercicios repetidos unificados en su tema. Los títulos subrayados aparecen como encabezados, las fórmulas resaltadas en amarillo van en recuadro y las gráficas se han redibujado a partir de los datos de los apuntes.

[LEYENDA]
- EJ.: Ejemplo o ejercicio
- Fórmula: Fórmula resaltada en los apuntes
- Cómo lo haría yo: Método alternativo anotado
[/LEYENDA]

[SUBTÍTULO] Contenido

[LISTA NUMERADA]
1. Porcentajes: IVA, IRPF, inflación, comisiones y tasas
2. Cálculo de cantidades iniciales y finales
3. Porcentaje que representa una cantidad de un total
4. Variación absoluta y porcentual
5. Interés simple
6. Interés compuesto
7. Proporcionalidad y regla de tres
8. Despejar incógnitas
9. Tablas de datos y frecuencias
10. Representaciones gráficas
[/LISTA NUMERADA]

[/PORTADA]

[INICIO SECCIÓN]

[TÍTULO APARTADO] 1. Porcentajes

[FÓRMULA] 300\text{ €}\cdot\frac{80}{100}=240\text{ €}

[NOTA] Se anulan los %.

[SUBTÍTULO] IVA (Impuesto sobre el Valor Añadido)

[FÓRMULA] 21\% = \frac{21}{100}=0{,}21

[EJEMPLO]
EJ. Precio sin IVA: 200 €.

[FÓRMULA] 200\cdot 0{,}21 = 42\text{ € de IVA}\qquad\text{Precio con IVA}=200+42=242\text{ €}

o bien $200\cdot 1{,}21 = 242\text{ €}$
[/EJEMPLO]

[FÓRMULA DESTACADA]
\text{Precio con IVA}=\text{Precio sin IVA}\times 1{,}21
[/FÓRMULA DESTACADA]

[EJEMPLO]
EJ. Por qué se multiplica por 1,21:

[FÓRMULA] 200+(200\cdot0{,}21)=200\,[1+(1\cdot0{,}21)]=200\cdot1{,}21
[/EJEMPLO]

[TEXTO] El precio con IVA es la cantidad final y el precio sin IVA la cantidad inicial:

[FÓRMULA DESTACADA]
\text{Precio sin IVA}=\frac{\text{Precio con IVA}}{1{,}21}\qquad \text{Precio con IVA}=\text{Precio sin IVA}\left(1+\frac{\text{IVA}}{100}\right)
[/FÓRMULA DESTACADA]

[EJEMPLO]
EJ. Precio sin IVA 300 € → $300\cdot1{,}21=363\text{ € con IVA}$
[/EJEMPLO]

[EJEMPLO]
EJ. Precio con IVA 363 € → $\frac{363}{1{,}21}=300\text{ € sin IVA}$
[/EJEMPLO]

[EJEMPLO]
EJ. Precio total con IVA (21 %) de: gafas 160 € (1 ud.), gafas de sol 210 € (1 ud.), funda 10 € (2 uds.).

[FÓRMULA] 160+210+20=390\text{ €}

[FÓRMULA] \text{Precio sin IVA}=\frac{390}{1{,}21}=322{,}31\text{ €}\qquad \text{IVA}=390-322{,}31=67{,}69\text{ €}

[FÓRMULA] \text{IVA}=\text{Precio sin IVA}\cdot0{,}21=322{,}31\cdot0{,}21=67{,}68\simeq67{,}69\text{ €}
[/EJEMPLO]

[SUBTÍTULO] IRPF (Impuesto sobre la Renta de las Personas Físicas)

[TEXTO] En la nómina = retención. Salario bruto 3.000 €, retención 15 %:

[FÓRMULA] 3000\cdot\frac{15}{100}=450\text{ €}

[TEXTO] Cotización a la Seguridad Social 10 %:

[FÓRMULA] 3000\cdot\frac{10}{100}=300\text{ €}\qquad 450+300=750\qquad 3000-750=2250\text{ € netos}

[FÓRMULA DESTACADA]
\text{Neto}=\text{Bruto}-\text{Retención}-\text{Cotización}
[/FÓRMULA DESTACADA]

[EJEMPLO]
EJ. Calcular el sueldo neto si el salario bruto son 2.000 €, retención IRPF 12 % y cotización 6 % de Seguridad Social.

[FÓRMULA] 2000\left(1-\frac{12}{100}\right)=2000\cdot0{,}88=1760\qquad 2000\left(1-\frac{6}{100}\right)=2000\cdot0{,}94=1880

[FÓRMULA] 240+120=360\text{ €}\qquad 2000-360=1640\text{ €}

[MÉTODO ALTERNATIVO]
Cómo lo haría yo:

[FÓRMULA] 2000\cdot\frac{18}{100}=360\text{ €}\;\Rightarrow\;2000-360=1640\text{ €}
[/MÉTODO ALTERNATIVO]

R. Sueldo neto: 1.640 €.
[/EJEMPLO]

[SUBTÍTULO] Inflación

[EJEMPLO]
Precio 600 €, inflación 2 %: $600\cdot\frac{2}{100}=12\text{ € de subida}$ R. 612 € nuevo precio.
[/EJEMPLO]

[SUBTÍTULO] Comisión

[EJEMPLO]
EJ. Venta de casa 200.000 €, comisión inmobiliaria 5 %.

[FÓRMULA] 200000\cdot\frac{5}{100}=10000\text{ € para la inmobiliaria}\qquad 200000\cdot\frac{95}{100}=190000\text{ € para el vendedor}
[/EJEMPLO]

[EJEMPLO]
EJ. Si un representante cobra una comisión del 9 % a su representado sobre una cantidad de 15.000 €, ¿qué cantidad obtiene cada uno?

[FÓRMULA] 15000\left(1-\frac{9}{100}\right)=15000\cdot0{,}91=13650\qquad 15000-13650=1350

R. 1.350 € para el representante y 13.650 € para el famoso.

[MÉTODO ALTERNATIVO]
Cómo lo haría yo:

[FÓRMULA] 15000\cdot\frac{9}{100}=1350\text{ € para el representante}\qquad 15000-1350=13650\text{ €}
[/MÉTODO ALTERNATIVO]
[/EJEMPLO]

[SUBTÍTULO] Tasas (para un organismo público)

[LISTA]
- Basura – tasa fija.
- IBI – porcentaje.
[/LISTA]

[EJEMPLO]
EJ. 8 % de ITP (Impuesto de Transmisiones Patrimoniales). Casa valorada en 150.000 €. $150000\cdot\frac{8}{100}=12000\text{ €}\;+\;150000\text{ €}$ R. Total: 162.000 €.
[/EJEMPLO]

[FIN SECCIÓN]

[INICIO SECCIÓN]

[TÍTULO APARTADO] 2. Cálculo de cantidades iniciales y finales

[TEXTO] Cantidad inicial = $C_i$ · Cantidad final = $C_f$ · Porcentaje = $p\,\%$

[FÓRMULA DESTACADA] Si aumenta
C_f=C_i\left(1+\frac{p}{100}\right)\qquad C_i=\frac{C_f}{1+\frac{p}{100}}
[/FÓRMULA DESTACADA]

[FÓRMULA DESTACADA] Si disminuye
C_f=C_i\left(1-\frac{p}{100}\right)\qquad C_i=\frac{C_f}{1-\frac{p}{100}}
[/FÓRMULA DESTACADA]

[EJEMPLO]
EJ. 5.000 € en acciones suben un 4 %.

[FÓRMULA] 5000\left(1+\frac{4}{100}\right)=5000\cdot1{,}04=5200\text{ €}=C_f
[/EJEMPLO]

[EJEMPLO]
EJ. Un pantalón costaba 60 € y está rebajado un 5 %. ¿Cuánto valdría?

[FÓRMULA] 60\left(1-\frac{5}{100}\right)=60\cdot0{,}95=57\text{ €}=C_f
[/EJEMPLO]

[EJEMPLO]
EJ. Al inicio de la jornada bursátil una acción vale 500 €. Si baja un 6 %, ¿cuál será el nuevo precio?

[FÓRMULA] 500\left(1-\frac{6}{100}\right)=500\,(1-0{,}06)=500\cdot0{,}94=470\text{ €}
[/EJEMPLO]

[EJEMPLO]
EJ. Un producto de 100 € sube un 15 %. ¿Precio final?

[FÓRMULA] 15\%\text{ de }100=15\;\Rightarrow\;100+15=115 \qquad C_f=100\left(1+\frac{15}{100}\right)=100\cdot1{,}15=115\text{ €}

Si baja un 15 %:

[FÓRMULA] 100-15=85 \qquad C_f=100\left(1-\frac{15}{100}\right)=100\cdot0{,}85=85\text{ €}\quad(1-0{,}15=0{,}85)
[/EJEMPLO]

[EJEMPLO]
EJ. Un producto que ahora vale 100 € ha subido un 15 %. ¿Cuál era su precio anterior?

[FÓRMULA] C_i=\frac{100}{1+\frac{15}{100}}=\frac{100}{1{,}15}=86{,}96\text{ €}

Si hubiera bajado un 15 %:

[FÓRMULA] C_i=\frac{100}{1-0{,}15}=\frac{100}{0{,}85}=117{,}65\text{ €}
[/EJEMPLO]

[EJEMPLO]
Otros:

[FÓRMULA] 100\left(1+\frac{10}{100}\right)=100\cdot1{,}1=110 \qquad 100\left(1-\frac{10}{100}\right)=100\cdot0{,}9=90
[/EJEMPLO]

[SUBTÍTULO] Aumentos y disminuciones encadenados

[EJEMPLO]
EJ. Un producto de 200 € aumenta un 40 % y después disminuye un 40 %.

[FÓRMULA] 200\left(1+\frac{40}{100}\right)=280\text{ €}\qquad 280\left(1-\frac{40}{100}\right)=168\text{ €}

[FÓRMULA] 200\left(1+\frac{40}{100}\right)\left(1-\frac{40}{100}\right)=200\cdot1{,}40\cdot0{,}60=168\text{ € precio final}
[/EJEMPLO]

[EJEMPLO]
EJ. Después de aplicarle un descuento del 20 % una chaqueta cuesta 72 €. ¿Cuál era su precio antes del descuento? (el descuento disminuye; buscamos $C_i$)

[FÓRMULA] C_i=\frac{C_f}{1-\frac{p}{100}}=\frac{72}{1-\frac{20}{100}}=\frac{72}{0{,}8}=90\text{ € precio inicial}
[/EJEMPLO]

[EJEMPLO]
EJ. El precio del kilo de tomates subió un 10 %, luego un 12 %, después un 11 % y finalmente un 15 %. Si actualmente vale 2,5 €/kg, ¿cuánto valía antes de las subidas? ¿Con qué se relacionan estas subidas? → Inflación.

[FÓRMULA] C_1=\frac{2{,}5}{1{,}15}=2{,}17\quad C_2=\frac{2{,}17}{1{,}11}=1{,}95\quad C_3=\frac{1{,}95}{1{,}12}=1{,}74\quad C_4=\frac{1{,}74}{1{,}10}=1{,}58\text{ €}

2ª forma: $C_i=2{,}5\div1{,}15\div1{,}11\div1{,}12\div1{,}10=1{,}5896$

3ª forma:

[FÓRMULA] C_i=\frac{2{,}5}{1{,}15\cdot1{,}11\cdot1{,}12\cdot1{,}10}=\frac{2{,}5}{1{,}572648}=1{,}5897
[/EJEMPLO]

[EJEMPLO]
EJ. Un perfume primero subió (suma) un 10 % y luego se rebajó (resta) un 10 %. Ahora cuesta 80 €. ¿Cuánto valía al inicio? (división)

[FÓRMULA] C_1=\frac{80}{1-\frac{10}{100}}=\frac{80}{0{,}90}=88{,}88\text{ €}\qquad C_2=\frac{88{,}88}{1+\frac{10}{100}}=\frac{88{,}88}{1{,}1}=80{,}8\text{ €}

Comprobación: $80{,}8\cdot1{,}10\cdot0{,}9=79{,}992\simeq80$
[/EJEMPLO]

[EJEMPLO]
EJ. Una acción subió un 20 %, luego un 30 % y finalmente un 25 %. Si vale actualmente 195 €, ¿cuánto valía antes?

[FÓRMULA] C_1=\frac{195}{1{,}25}=156\qquad C_2=\frac{156}{1{,}30}=120\qquad C_3=\frac{120}{1{,}20}=100\text{ €}

[FÓRMULA] C_i=\frac{195}{1{,}25\cdot1{,}30\cdot1{,}20}=\frac{195}{1{,}95}=100\text{ €}
[/EJEMPLO]

[EJEMPLO]
EJ. Un juguete subió un 25 % en Navidad y en la cuesta de enero se rebajó un 5 %. En enero cuesta 95 €. ¿Cuánto costaba antes de Navidad?

[FÓRMULA] C_1=\frac{95}{1-0{,}05}=\frac{95}{0{,}95}=100\qquad C_2=\frac{100}{1+0{,}25}=\frac{100}{1{,}25}=80\text{ €}

[FÓRMULA] C_i=\frac{95}{0{,}95\cdot1{,}25}=80\text{ €}
[/EJEMPLO]

[SUBTÍTULO] Tabla resumen

[TABLA]
|  | Aumenta | Disminuye |
|---|---|---|
| Tengo $C_i$ y calculo $C_f$ | $C_f=C_i\left(1+\frac{p}{100}\right)$ | $C_f=C_i\left(1-\frac{p}{100}\right)$ |
| Tengo $C_f$ y calculo $C_i$ | $C_i=\dfrac{C_f}{1+\frac{p}{100}}$ | $C_i=\dfrac{C_f}{1-\frac{p}{100}}$ |
[/TABLA]

[FIN SECCIÓN]

[INICIO SECCIÓN]

[TÍTULO APARTADO] 3. Porcentaje que representa una cantidad de un total

[TEXTO] Porcentaje ($p$) · Cantidad ($c$) · Total ($t$)

[FÓRMULA DESTACADA]
p=\frac{c}{t}\times100
[/FÓRMULA DESTACADA]

[EJEMPLO]
EJ. Estudiamos 10 h y 4 h son de matemáticas. ¿Qué porcentaje dedicamos a matemáticas? $p=\frac{4}{10}\times100=40\%$
[/EJEMPLO]

[EJEMPLO]
EJ. En una biblioteca hay 800 libros, de los cuales 200 son de matemáticas. ¿Qué porcentaje corresponde a matemáticas?

[FÓRMULA] p=\frac{200}{800}\times100=0{,}25\times100=25\%\qquad\text{o bien}\qquad\frac{200}{800}=\frac{x}{100}\Rightarrow x=\frac{200\times100}{800}

R. El 25 % de los libros corresponde a matemáticas.
[/EJEMPLO]

[EJEMPLO]
EJ. Un cesto con 15 manzanas; tomamos 3. $p=\frac{3}{15}\times100=20\%$
[/EJEMPLO]

[EJEMPLO]
EJ. En una bolsa hay 250 bolas y el 20 % son rojas. ¿Cuántas bolas rojas hay? $250\cdot\frac{20}{100}=250\cdot0{,}2=50\text{ bolas rojas}$
[/EJEMPLO]

[EJEMPLO]
EJ. En un frutero hay 36 frutas y 6 son plátanos. ¿Porcentaje de plátanos? $p=\frac{6}{36}\times100=16{,}67\%$
[/EJEMPLO]

[EJEMPLO]
EJ. El 15 % de las frutas de un almacén son plátanos y hay 120 unidades. ¿Cuántas frutas hay?

[FÓRMULA] \frac{120}{15}=\frac{x}{100}\Rightarrow x=\frac{120\cdot100}{15}=\frac{12000}{15}=800

Con la fórmula:

[FÓRMULA] 15=\frac{120}{T}\cdot100\Rightarrow 15\,T=120\cdot100\Rightarrow T=\frac{120\cdot100}{15}=800

(C = cantidad, T = total)
[/EJEMPLO]

[FIN SECCIÓN]

[INICIO SECCIÓN]

[TÍTULO APARTADO] 4. Variación absoluta y porcentual

[TEXTO] $C_i$ = cantidad inicial · $C_f$ = cantidad final

[FÓRMULA DESTACADA] Variación absoluta
V_A=C_f-C_i
[/FÓRMULA DESTACADA]

[FÓRMULA DESTACADA] Variación porcentual
V_P=\frac{C_f-C_i}{C_i}\times100=\frac{V_A}{C_i}\times100
[/FÓRMULA DESTACADA]

[EJEMPLO]
EJ. Al comenzar el mes teníamos 7.000 € en el banco; a mitad de mes tenemos 6.200 €.

[FÓRMULA] V_A=6200-7000=-800\text{ €}\qquad V_P=\frac{-800}{7000}\times100=-11{,}43\%
[/EJEMPLO]

[EJEMPLO]
EJ. Calcular la variación porcentual entre cada dos años consecutivos de los ahorros de una persona.

[TABLA]
| Año | Ahorros (€) |
|---|---|
| 2024 | 2.500 |
| 2025 | 2.000 |
| 2026 | 4.000 |
[/TABLA]

[FÓRMULA] \frac{2000-2500}{2500}\times100=\frac{-500}{2500}\times100=-20\%\qquad \frac{4000-2000}{2000}\times100=100\%
[/EJEMPLO]

[EJEMPLO]
EJ. Un trabajador autónomo ha ganado 2.000 € un mes y 1.800 € el siguiente.

[FÓRMULA] V_A=1800-2000=-200\text{ € (menos que el mes anterior)}\qquad V_P=\frac{1800-2000}{2000}\times100=-10\%
[/EJEMPLO]

[EJEMPLO]
EJ. Camiones descargados: 100.000 (2019) y 125.000 (2025).

[FÓRMULA] V_A=125000-100000=25000\qquad V_P=\frac{125000-100000}{100000}\cdot100=25\%
[/EJEMPLO]

[EJEMPLO]
EJ. Variaciones absoluta y porcentual entre 1995 y 1980 (gráfica del apartado 10).

[FÓRMULA] V_A=1750-1500=250\qquad V_P=\frac{1750-1500}{1500}\cdot100=\frac{250}{1500}\cdot100=16{,}67\%
[/EJEMPLO]

[FIN SECCIÓN]

[INICIO SECCIÓN]

[TÍTULO APARTADO] 5. Interés simple

[TEXTO] El interés es el mismo en cada periodo porque no se acumula. Datos: capital inicial ($C_i$ o $C_0$), tasa de interés anual ($t$), años.

[FÓRMULA DESTACADA] ¡Importante!
\text{Interés}=C_i\cdot\text{tasa}\cdot\text{años}\qquad C_f=C_i+\text{Interés}
[/FÓRMULA DESTACADA]

[EJEMPLO]
EJ.

[FÓRMULA] C_0=5000\text{ €},\; t=3\%,\;4\text{ años}:\quad 5000\cdot\frac{3}{100}=150\;\Rightarrow\;150\cdot4=600\text{ €}
[/EJEMPLO]

[SUBTÍTULO] ¡Ojo! Unidades de tiempo

[TEXTO] Si el interés es anual y tenemos seis meses: $\text{años}=\frac{6}{12}=0{,}5$

[TEXTO] ¿Qué incógnita podríamos despejar?

[FÓRMULA DESTACADA] Capital inicial
C_i=\frac{\text{Interés}}{\text{tasa}\cdot\text{años}}
C_i=C_f-\text{Interés}
[/FÓRMULA DESTACADA]

[FÓRMULA DESTACADA] Tasa
\frac{\text{Interés}}{C_i}=\text{tasa}\cdot\text{años}
\text{tasa}=\frac{\text{Interés}}{C_i\cdot\text{años}}
[/FÓRMULA DESTACADA]

[FÓRMULA DESTACADA] Años
\frac{\text{Interés}}{C_i}=\text{tasa}\cdot\text{años}
\text{años}=\frac{\text{Interés}}{C_i\cdot\text{tasa}}
[/FÓRMULA DESTACADA]

[EJEMPLO]
EJ. Una renta a interés simple ha generado 500 € de interés; inicialmente había 6.000 € y la tasa era del 1 %. ¿Cuántos años hemos necesitado?

[FÓRMULA] \text{años}=\frac{500}{6000\cdot0{,}01}=8{,}\overline{3}\;\Rightarrow\;8\text{ años y }12\cdot0{,}\overline{3}=4\text{ meses}

Comprobación: $6000\cdot0{,}01=60\qquad 60\cdot8{,}\overline{3}\simeq500$
[/EJEMPLO]

[EJEMPLO]
EJ. A interés simple invertimos 2.500 € y hemos obtenido 3.200 €. ¿Qué interés ha generado?

[FÓRMULA] \text{Interés}=C_f-C_i=3200-2500=700\text{ €}\qquad p=\frac{700}{2500}\cdot100=28\%

Hemos mantenido la inversión 7 años. ¿A qué tasa ha rentado?

[FÓRMULA] \text{tasa}=\frac{\text{Interés}}{C_i\cdot\text{años}}=\frac{700}{2500\cdot7}=0{,}04\;\Rightarrow\;0{,}04\cdot100=4\%
[/EJEMPLO]

[EJEMPLO]
EJ. Un interés simple a 18 meses y con un tipo anual del 2 % ha dado un interés de 200 €. ¿Cuál es el capital final?

[FÓRMULA] I=200\quad C_i=x\quad p=2\%\;(0{,}02)\quad t=\frac{18}{12}=1{,}5\text{ años}

[FÓRMULA] I=C_i\cdot p\cdot t\;\Rightarrow\;200=C_i\cdot0{,}02\cdot1{,}5=C_i\cdot0{,}03\;\Rightarrow\;C_i=\frac{200}{0{,}03}\simeq6666{,}67

[FÓRMULA] C_f=C_i+I=6666{,}67+200=6866{,}67\text{ €}
[/EJEMPLO]

[FIN SECCIÓN]

[INICIO SECCIÓN]

[TÍTULO APARTADO] 6. Interés compuesto

[TEXTO] Intereses acumulativos: se reinvierten y vuelven a generar beneficio.

[FÓRMULA DESTACADA]
C_f=C_i\,(1+\text{tasa})^{\text{años}}\qquad \text{Interés acumulado}=C_f-C_i
\text{Despejar } C_i=\frac{C_f}{(1+\text{tasa})^{\text{años}}}\qquad C_i=C_f-\text{Interés acumulado}\qquad \text{tasa}=\frac{\text{porcentaje}}{100}
[/FÓRMULA DESTACADA]

[EJEMPLO]
EJ. Invertimos 1.000 € al 5 % anual durante 3 años.

[FÓRMULA] 1^{\text{er}}\text{ año}: 1000\cdot1{,}05=1050\quad 2^{\text{o}}: 1050\cdot1{,}05=1102{,}5\quad 3^{\text{er}}: 1102{,}5\cdot1{,}05=1157{,}625

Con la fórmula:

[FÓRMULA] 1000\left(1+\frac{5}{100}\right)^3=1000\cdot1{,}05^3=1157{,}62\text{ €}
[/EJEMPLO]

[EJEMPLO]
EJ. Invertimos 2.000 € al 4 % anual durante dos años. $2000\cdot1{,}04^2=2163{,}2\text{ €}$
[/EJEMPLO]

[EJEMPLO]
EJ. Invertimos 5.000 € al 3 % anual durante 2 años. $5000\cdot1{,}03^2=5304{,}5\text{ €}$
[/EJEMPLO]

[EJEMPLO]
EJ. Invertimos 4.000 € al 5 % durante 2 años. $4000\cdot1{,}05^2=4410\text{ €}$
[/EJEMPLO]

[EJEMPLO]
EJ. Una empresa tenía 2.500 clientes; durante un año aumentaron un 12 % y al año siguiente un 8 %. ¿Cuántos clientes tiene finalmente?

[FÓRMULA] 2500\cdot\frac{12}{100}=300\qquad 2800\cdot\frac{8}{100}=224

R. 300 clientes el primer año y 224 el segundo: $300+224=524$ → $2500+524=3024$ clientes en total.
[/EJEMPLO]

[EJEMPLO]
EJ. Una acción bursátil se ha incrementado un 5 % los 3 últimos años. Si inicialmente valía 120 €, ¿cuál es su valor actual?

[FÓRMULA] 120\left(1+\frac{5}{100}\right)^3=120\cdot1{,}05^3=138{,}915\text{ €}

Se incrementó 18,915 € en los últimos 3 años.
[/EJEMPLO]

[EJEMPLO]
EJ. Si la inflación de un producto de estética es del 5 % un año y del 4 % el siguiente, ¿qué precio se puede esperar si inicialmente valía 30 €?

[FÓRMULA] C_f=C_i\left(1+\frac{p_1}{100}\right)\left(1+\frac{p_2}{100}\right)=30\cdot1{,}05\cdot1{,}04\qquad 30\cdot1{,}05=31{,}50\qquad 31{,}50\cdot1{,}04=32{,}76\text{ €}
[/EJEMPLO]

[EJEMPLO]
EJ. Metemos en una cuenta de ahorro una cantidad que, tras 4 años y 6 meses al 2 %, genera un capital final de 8.700 €. ¿Cuál ha sido el interés acumulado?

[FÓRMULA] C_i=\frac{8700}{\left(1+\frac{2}{100}\right)^{4{,}5}}=\frac{8700}{1{,}02^{4{,}5}}=\frac{8700}{1{,}0932}=7958{,}28\qquad \text{Interés}=8700-7958{,}28=741{,}72\text{ €}
[/EJEMPLO]

[EJEMPLO]
EJ. Metemos en una cuenta de ahorro un capital que, tras 2 años y 3 meses con una tasa anual del 1,5 %, genera 7.200 €. ¿Cuál ha sido el interés acumulado?

[FÓRMULA] C_i=\frac{7200}{\left(1+\frac{1{,}5}{100}\right)^{2{,}25}}=\frac{7200}{1{,}015^{2{,}25}}

[FÓRMULA] C_i=\frac{7200}{1{,}0341}=6962{,}77\qquad \text{Interés}=7200-6962{,}77=237{,}23\text{ €}
[/EJEMPLO]

[FIN SECCIÓN]

[INICIO SECCIÓN]

[TÍTULO APARTADO] 7. Proporcionalidad

[SUBTÍTULO] Proporcionalidad numérica

[FÓRMULA] \frac{3}{5}=\frac{6}{10}=\frac{9}{15}\;\Rightarrow\;3\cdot15=5\cdot9=45\qquad \frac{3}{5}=\frac{6}{10}\;\Rightarrow\;3\cdot10=5\cdot6=30

[SUBTÍTULO] Regla de 3

[DIAGRAMA] regla-de-tres.svg — Regla de 3 en cruz: 4/7 = 8/x; multiplica 7 × 8 y divide entre 4

[TEXTO] Multiplica en cruz los que se conocen (7 × 8) y divide entre el que queda (4):

[FÓRMULA] \frac{4}{7}=\frac{8}{x}\;\Rightarrow\;x=\frac{7\times8}{4}=\frac{56}{4}=14\qquad 4x=7\times8\Rightarrow x=14

[EJEMPLO]
EJ. Si 3 azucarillos tienen 21 gramos de azúcar, ¿cuántos gramos tienen 5 azucarillos?

[FÓRMULA] \frac{3}{21}=\frac{5}{x}\;\Rightarrow\;x=\frac{21\times5}{3}=35\text{ g}
[/EJEMPLO]

[SUBTÍTULO] Proporcionalidad directa

[TEXTO] Si una variable aumenta, la otra también. Se divide: el cociente es constante.

[TABLA]
| Libros a imprimir | 1 | 2 | 3 | 4 | 10 |
|---|---|---|---|---|---|
| Folios necesarios | 300 | 600 | 900 | 1200 | 3000 |
[/TABLA]

[FÓRMULA] \frac{300}{1}=\frac{600}{2}=\frac{900}{3}=\frac{1200}{4}=\frac{3000}{10}=300

[NOTA] 300 es el ratio (constante) de proporcionalidad.

[FÓRMULA DESTACADA]
\text{Directa: } k=\frac{y}{x}\qquad\text{Inversa: } k=x\cdot y
[/FÓRMULA DESTACADA]

[SUBTÍTULO] Proporcionalidad inversa (indirecta)

[TEXTO] Si una variable aumenta, la otra disminuye. Se multiplica: el producto es constante.

[TABLA]
| Nº de trabajadores | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Horas de trabajo necesarias | 60 | 30 | 20 | 15 | 12 | 10 |
[/TABLA]

[FÓRMULA] 1\times60=2\times30=3\times20=4\times15=5\times12=6\times10=60

[NOTA] 60 es el ratio de proporcionalidad.

[IMAGEN] imagenes/proporcionalidad.png — Gráfica generada: la directa es una recta; la inversa, una curva que baja.

[EJEMPLO]
EJ. Distancia recorrida a velocidad constante (directa → dividir).

[TABLA]
| Tiempo (h) | 1 | 2 | 4 | 8 | 20 |
|---|---|---|---|---|---|
| Distancia (km) | 80 | 160 | 320 | 640 | 1600 |
[/TABLA]

[FÓRMULA] \frac{640}{8}=80\text{ (ratio o relación)}\qquad \frac{1}{80}=\frac{2}{160}=\frac{4}{320}=\frac{8}{640}=\frac{20}{1600}
[/EJEMPLO]

[EJEMPLO]
EJ. Distancia recorrida a una velocidad:

[TABLA]
| Tiempo (h) | 1 | 2 | 4 | 8 | 20 |
|---|---|---|---|---|---|
| Distancia (km) | 80 | 100 | 320 | 640 | 1600 |
[/TABLA]

[FÓRMULA] \frac{80}{1}=\frac{320}{4}=\frac{640}{8}=\frac{1600}{20}=80\qquad\frac{100}{2}=50

[DESTACADO] $80\neq50\Rightarrow$ NO es constante.
[/EJEMPLO]

[EJEMPLO]
EJ. Velocidad y tiempo en un mismo trayecto (inversa → multiplicar).

[TABLA]
| Velocidad (km/h) | 20 | 40 | 60 | 80 | 120 |
|---|---|---|---|---|---|
| Tiempo (h) | 12 | 6 | 4 | 3 | 2 |
[/TABLA]

[FÓRMULA] 80\cdot3=240\quad 20x=240\Rightarrow x=12\quad 40x=240\Rightarrow x=6\quad 60x=240\Rightarrow x=4\quad 120x=240\Rightarrow x=2

[FÓRMULA] 20\cdot12=40\cdot6=60\cdot4=80\cdot3=120\cdot2=240
[/EJEMPLO]

[EJEMPLO]
EJ. Directa: km recorridos y gasolina gastada (litros).

[TABLA]
| Km recorridos | 50 | 100 | 200 | 400 | 600 |
|---|---|---|---|---|---|
| Gasolina (l) | 2,5 | 5 | 10 | 20 | 30 |
[/TABLA]

[FÓRMULA] \frac{200}{10}=20=\frac{400}{20}=\frac{50}{2{,}5}

Inversa: tiempo y velocidad.

[TABLA]
| Tiempo | 4 | 2 | 1 |
|---|---|---|---|
| Velocidad | 60 | 120 | 240 |
[/TABLA]

[FÓRMULA] 4\cdot60=2\cdot120=1\cdot240
[/EJEMPLO]

[EJEMPLO]
EJ. ¿Es la siguiente una proporcionalidad inversa?

[TABLA]
| 2 | 4 | 8 | 10 |
|---|---|---|---|
| 100 | 50 | 10 | 2 |
[/TABLA]

[FÓRMULA] 2\times100=200\quad 4\times50=200\quad 8\times10=80\quad 10\times2=20

[DESTACADO] $200\neq80\neq20$ → no se mantiene la constante: NO es proporción inversa.
[/EJEMPLO]

[EJEMPLO]
EJ. Dos personas recogen la mesa de una fiesta en 30 minutos. ¿Cuánto tardarían si fueran 5?

[FÓRMULA] 2\cdot30=5\cdot x\;\Rightarrow\;x=\frac{2\cdot30}{5}=\frac{60}{5}=12\text{ min}
[/EJEMPLO]

[EJEMPLO]
EJ. Si un saco de arroz pesa 45 kg y en cada kilo se devuelven 5 gramos de arroz en mal estado, ¿cuántos gramos en mal estado habrá en 3 sacos?

[FÓRMULA] 45\cdot3=135\text{ kg en total}\qquad 135\cdot5=675\text{ g en mal estado}
[/EJEMPLO]

[FIN SECCIÓN]

[INICIO SECCIÓN]

[TÍTULO APARTADO] 8. Despejar incógnitas

[EJEMPLO]
Despejar la $V$ de $E=V\cdot t\;\Rightarrow\;V=\frac{E}{t}$

Despejar $V$ de $I=\frac{V}{R}\;\Rightarrow\;V=I\cdot R$
[/EJEMPLO]

[EJEMPLO]
Despejar la $x$ de $3x+1=4$:

[FÓRMULA] 3x=4-1\;\Rightarrow\;3x=3\;\Rightarrow\;x=\frac{3}{3}=1
[/EJEMPLO]

[FIN SECCIÓN]

[INICIO SECCIÓN]

[TÍTULO APARTADO] 9. Tablas de datos numéricos y frecuencias

[TEXTO] Elementos: filas, columnas y celdas; título, encabezado y detalle; unidades.

[EJEMPLO]
EJ. Tabla del gasto medio en los hogares españoles (€/mes).

[TABLA]
|  | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|
| Vivienda | 600 | 620 | 660 | 750 |
| Alimentación | 250 | 300 | 310 | 315 |
| Otros | 100 | 110 | 115 | 120 |
[/TABLA]
[/EJEMPLO]

[EJEMPLO]
EJ. Datos meteorológicos en distintas localidades.

[TABLA]
|  | Temperatura (°C) | Probabilidad de lluvia (%) | Viento (km/h) |
|---|---|---|---|
| Illescas | 36 | 0 % | 10 |
| Toledo | 34 | 2 % | 12 |
| Madrid | 32 | 5 % | 20 |
[/TABLA]
[/EJEMPLO]

[FÓRMULA DESTACADA]
\text{Frecuencia absoluta (FA)}=\text{nº de apariciones}\qquad \text{Frecuencia relativa (FR)}=\frac{FA}{\text{nº total de datos}}\qquad P=FR\times100\qquad \textstyle\sum fr_i=1
[/FÓRMULA DESTACADA]

[EJEMPLO]
EJ. Calificaciones en una clase de 20 alumnos: 4, 6, 7, 5, 8, 6, 9, 7, 5, 6, 10, 3, 0, 1, 8, 5, 4, 6, 5, 3. Construye una tabla con frecuencia absoluta, frecuencia relativa y porcentaje de cada calificación.

[TABLA]
| Calificación | F. absoluta | F. relativa | Porcentaje |
|---|---|---|---|
| 0 | 1 | 0,05 | 5 % |
| 1 | 1 | 0,05 | 5 % |
| 2 | 0 | 0 | 0 % |
| 3 | 2 | 0,1 | 10 % |
| 4 | 2 | 0,1 | 10 % |
| 5 | 4 | 0,2 | 20 % |
| 6 | 4 | 0,2 | 20 % |
| 7 | 2 | 0,1 | 10 % |
| 8 | 2 | 0,1 | 10 % |
| 9 | 1 | 0,05 | 5 % |
| 10 | 1 | 0,05 | 5 % |
| Total | 20 | 1 | 100 % |
[/TABLA]
[/EJEMPLO]

[EJEMPLO]
EJ. Deporte favorito en un grupo de 40 personas.

[TABLA]
| Deporte | F. absoluta | F. relativa (Σ = 1) | Porcentaje (Σ = 100 %) |
|---|---|---|---|
| Fútbol | 12 | 0,3 | 30 % |
| Baloncesto | 10 | 0,25 | 25 % |
| Natación | 8 | 0,2 | 20 % |
| Tenis | 6 | 0,15 | 15 % |
| Ciclismo | 4 | 0,1 | 10 % |
| Total | 40 | 1,00 | 100 % |
[/TABLA]

[FÓRMULA] FR=\frac{12}{40}=0{,}3\;\Rightarrow\;0{,}3\times100=30\%
[/EJEMPLO]

[FIN SECCIÓN]

[INICIO SECCIÓN]

[TÍTULO APARTADO] 10. Representaciones gráficas

[SUBTÍTULO] Gráfica de barras (clasificación)

[EJEMPLO]
EJ. Número de coches estacionados según su marca. ¿SEAT? 7.

[IMAGEN] imagenes/barras_coches.png

[FÓRMULA] \text{Total}=7+4+1+5=17\qquad \text{SEAT}=\frac{7}{17}\cdot100=41{,}18\%
[/EJEMPLO]

[EJEMPLO]
EJ. Flores: 500 tulipanes, 1.500 gardenias, 2.000 rosas.

[IMAGEN] imagenes/barras_flores.png
[/EJEMPLO]

[EJEMPLO]
EJ. Encuesta sobre comidas favoritas (solo se puede elegir una): 8 personas eligen macarrones, 10 cocido, 5 lubina, 7 pisto y 12 otra.

[IMAGEN] imagenes/barras_comidas.png

¿A cuántas personas les gusta la lubina o el pisto? $5+7=12$ personas.

¿Cuántas han elegido algo distinto al cocido? $8+5+7+12=32$ personas.
[/EJEMPLO]

[SUBTÍTULO] Gráfica de sectores o circular

[TEXTO] Partes de un total que han de sumar 100 %.

[EJEMPLO]
EJ. Calificaciones del alumnado (%).

[IMAGEN] imagenes/sectores_calif.png

[FÓRMULA] \text{IN}=\frac{1}{4}\cdot100=25\%\text{ (ocupa }1/4\text{ del círculo)}\qquad \text{B}=\frac{1}{8}\cdot100=12{,}5\%
[/EJEMPLO]

[EJEMPLO]
EJ. Representa en un gráfico de sectores: 5 coches son negros, 10 blancos y 5 verdes.

[FÓRMULA] \text{Total}=5+10+5=20\qquad \tfrac{5}{20}=25\%\quad \tfrac{10}{20}=50\%\quad \tfrac{5}{20}=25\%

[IMAGEN] imagenes/sectores_coches_color.png
[/EJEMPLO]

[EJEMPLO]
Reparto: matemáticas 33,33 %, otros 16,67 %, suspensos 50 %.

[IMAGEN] imagenes/sectores_mates.png
[/EJEMPLO]

[SUBTÍTULO] Gráfica de líneas

[TEXTO] Uso: evolución de una magnitud (cantidad) a lo largo del tiempo.

[EJEMPLO]
EJ. Temperatura por día.

[IMAGEN] imagenes/lineas_temp.png
[/EJEMPLO]

[EJEMPLO]
EJ. Cambio/bajada de peso (kg/años).

[IMAGEN] imagenes/lineas_peso.png
[/EJEMPLO]

[EJEMPLO]
EJ. Evolución del precio medio mensual del alquiler de un piso concreto entre 2021 y 2025 (650, 680, 750, 790 y 820 €).

[IMAGEN] imagenes/lineas_alquiler.png
[/EJEMPLO]

[EJEMPLO]
EJ. Representa gráficamente del mejor modo posible esta información (lineal).

[IMAGEN] imagenes/lineas_1980.png

Variaciones entre 1995 y 1980: $V_A=250\quad V_P=16{,}67\%$ (ver apartado 4).
[/EJEMPLO]

[EJEMPLO]
EJ. Camiones descargados.

[TABLA]
| Año | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Camiones | 100.000 | 115.000 | 95.000 | 120.000 | 105.000 | 90.000 | 125.000 |
[/TABLA]

[IMAGEN] imagenes/lineas_camiones.png
[/EJEMPLO]

[FIN SECCIÓN]
