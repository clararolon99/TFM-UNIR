# Bitácora del TFM de UNIR

## 8 de noviembre de 2026

Quedó preparada la reconstrucción del TFM. Se revisaron los seis documentos de la carpeta Docs y, tras instalar las dos skills, se abrieron los dos archivos de indicaciones. Docs/indicaciones.md tenía 0 bytes. Se adoptaron las pautas del archivo indicaciones.md de la raíz, que enumera los materiales y describe cómo usarlos. La versión de partida para el nuevo TFM será una copia de la plantilla oficial.

Se recuperaron los 27 comentarios del director del borrador revisado, con sus identificadores y pasajes asociados. La tabla de seguimiento recoge las actuaciones pendientes. La metodología de ese borrador conserva texto de la plantilla y se elaborará a partir del caso aprobado.

## Tema aprobado

**Diseño de una instalación solar fotovoltaica conectada a red para autoconsumo en una vivienda unifamiliar en Ciudad del Este, Paraguay.**

Autora: Clara María De Los Ángeles Rolón Duré. Director: René Martín Miranda Urbina. Trabajo individual de Tipo 1 del Máster Universitario en Energías Renovables.

El caso parte del consumo real de la vivienda según las facturas de ANDE y del recurso solar de Ciudad del Este. El diseño debe justificar la potencia y configuración del generador, el inversor y los demás componentes. La evaluación incluye el desempeño energético, el ahorro y las emisiones evitadas. La conexión y el tratamiento de los excedentes se determinarán con fuentes aplicables al suministro del caso.

## Qué rige cada parte del trabajo

| Material | Uso |
| --- | --- |
| [Tema aprobado](<Docs/Tema TFM Clara Maria de Los Angeles Rolon Dure.docx>) | Título literal, identificación del director, alcance y justificación de la propuesta aprobada. |
| [Instrucciones de UNIR](Docs/instrucciones.pdf) | Estructura, extensión y contenido exigido para el Tipo 1. Véanse las páginas 4–8 y 14–16 para formato y desarrollo técnico, y las páginas 18–20 para resultados, conclusiones, referencias y anexos. |
| [Plantilla Tipo 1](<Docs/plantilla_tipo1 (2).docx>) | Documento Word de partida. Sus estilos, portada, encabezados e índices gobiernan la maquetación. |
| [Rúbrica Tipo 1](Docs/rubrica_tipo1.pdf) | Cotejo con la columna de sobresaliente. La estructura y el estilo pesan un 20 %, el contenido un 50 % y la exposición un 30 %. La exposición requiere al menos 1,5 puntos para aprobar. |
| [Guía de citas de UNIR](Docs/APA_7ed_UNIR.pdf) | Adaptación de APA 7 para las citas, las referencias y la atribución de tablas y figuras. |
| [Borrador con observaciones](<Docs/B-1-TFM-Clara Maria De Los Angeles Rolon Dure-revisado (1).docx>) | Evidencia de las observaciones del director y punto de partida para localizar los datos transcritos. El título, la estructura, las referencias y los datos de este borrador se cotejan con las fuentes correspondientes. |
| [Indicaciones de la autora](indicaciones.md) | Reconstrucción desde la plantilla, atención a cada comentario y aplicación de lo aprendido en la asignatura. |

La guía establece 60 a 100 páginas para el trabajo individual, excluidas la portada, los índices y los anexos. Los borradores se entregan en Word y el depósito final se hace en PDF. El resumen se redacta al terminar y tiene de 150 a 300 palabras. La plantilla incluye resumen, abstract y de 3 a 5 palabras clave en cada idioma.

El núcleo técnico del Tipo 1 se distribuye entre requisitos de diseño, metodología, evaluación del recurso, diseño de la instalación y análisis económico y ambiental. El capítulo de resultados debe discutir los hallazgos. Las conclusiones deben responder a los objetivos específicos. La estructura de UNIR gobierna la organización de la discusión y de las referencias.

## Skills obligatorias

| Skill | Decisión y aplicación | Versión instalada |
| --- | --- | --- |
| thesis-writing | Sirve para organizar y revisar un TFM por secciones, vincular las afirmaciones con su evidencia y documentar métodos reproducibles. Admite Word y da prioridad al formato institucional. Se aplican sus pautas de estructura y revisión al diseño de ingeniería según la guía de UNIR. | [santifs/thesis-writing-skill](https://github.com/santifs/thesis-writing-skill/tree/d2484deeff288da550222afc74fc939648d9288d/thesis-writing) |
| humanizer | Se usa al cerrar cada sección, en español académico o en inglés para el abstract. La revisión elimina repeticiones y frases vacías. Al terminar, se cotejan el sentido técnico, las citas, los términos, las cifras, las unidades y las ecuaciones con el texto validado. | [blader/humanizer v3.1.0](https://github.com/blader/humanizer/tree/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8) |

También se consideraron academic-writing, con un modo útil para revisar comentarios y citas APA 7 pero con comprobaciones especializadas en psicología y procesamiento del lenguaje, y la colección scientific-agent-skills, orientada a un conjunto más amplio de tareas científicas. Para este caso pesaron el flujo específico de TFM, la posibilidad de trabajar en Word y el uso de la plantilla institucional. [academic-writing](https://github.com/David-Saeteros/claude-skills/tree/main/skills/academic-writing) · [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

Se instalaron en C:\Users\HP\.agents\skills con el instalador de Codex y una copia verificada de los archivos necesarios. Las dos quedaron habilitadas con alcance de usuario. La comprobación con Codex dio el mismo resultado en el proyecto y en una carpeta ajena. Se conservaron los recursos de thesis-writing, las licencias y los metadatos de Humanizer para Codex.

## Seguimiento de las observaciones del director

Los números son los identificadores de los comentarios del Word de origen. La tabla recoge las acciones identificadas al preparar el proyecto. El estado por versión figura en las entradas posteriores.

| ID | Lugar en el borrador | Acción por comprobar en la nueva versión |
| --- | --- | --- |
| 1 | Portada y encabezados | Usar el título aprobado literalmente en todo el documento. |
| 2 | Comentario general en portada | Precisar la necesidad del caso. Desarrollar la metodología técnica con ecuaciones explicadas y revisar la coherencia, la ortografía y la presentación de todo el TFM. |
| 4 | Portada | Completar el campo del director con el nombre del documento aprobado. |
| 9 | Planteamiento del problema | Volver al alcance de la primera tutoría que recoge la propuesta aprobada. Exponer con claridad la necesidad de la vivienda y revisar la fluidez del apartado. |
| 10 | Planteamiento del problema | Tratar el desfase entre la demanda y la generación en el desarrollo técnico. |
| 11 | Cierre del problema | Identificar la necesidad concreta que debe atenderse y explicar cómo el autoconsumo fotovoltaico puede contribuir a resolverla. |
| 13 | Justificación | Explicar por qué hace falta el trabajo y para qué servirá, a partir del problema ya delimitado. |
| 16 | Justificación | Vincular la evaluación del caso a esa necesidad. Sustentar cualquier afirmación de novedad con evidencia. |
| 17 | Justificación | Presentar el dimensionamiento como parte del desarrollo técnico. |
| 18 | Cierre de la justificación | Ordenar los argumentos para que conduzcan al aporte concreto y documentable del estudio de la vivienda. |
| 20 | Inicio de Contexto y estado del arte | Reubicar los fundamentos técnicos en el apartado que corresponda de acuerdo con su función. |
| 21 | Sistema eléctrico y demanda | Recuperar la pregunta sobre qué parte de la demanda de la vivienda puede cubrir la generación propia. Llevarla al planteamiento de manera clara. |
| 22 | Delimitación del caso residencial | Eliminar la repetición del problema y de la justificación. Llevar las condiciones técnicas a requisitos o diseño según su función. |
| 23 | Antecedentes de Paraguay | Investigar los trabajos del Centro de Tecnologías Apropiadas de la UCA y de otras instituciones, con atención a los casos residenciales. |
| 24 | Comparación de antecedentes | Resolver la contradicción entre contexto, problema y justificación. Conservar en cada apartado solo los argumentos que cumplen su función. |
| 25 | Marco normativo y tarifario | Reubicar los requisitos normativos del suministro y de la conexión en Requisitos de diseño. Verificar la aplicación al caso. |
| 26 | Marco teórico del autoconsumo | Trasladar los fundamentos de cálculo y los indicadores a Metodología. |
| 27 | Síntesis del estado del arte | Desarrollar en varias páginas la evolución de la tecnología y de sus componentes, con evidencia de las opciones destacadas en el mercado mundial y en Paraguay. |
| 29 | Objetivos | Formular cada objetivo con un solo verbo, generalmente en infinitivo, y una meta explícita. |
| 32 | Objetivo general | Redactar una meta técnica que se distinga del título y cumpla la regla de un verbo. |
| 33 | Objetivos específicos | Vincular cada objetivo a un resultado comprobable y a una conclusión. |
| 34 | Objetivo sobre recurso y emplazamiento | Integrar el análisis del recurso y de las condiciones del sitio en el desarrollo del diseño. |
| 35 | Objetivo sobre dimensionamiento | Suprimir la coletilla «de acuerdo con la demanda y las restricciones de diseño» al reformularlo. |
| 36 | Objetivo de ahorro | Sustituir «Cuantificar» por un verbo que exprese la evaluación económica que realmente se hará. |
| 39 | Hipótesis | Formular valores contrastables de ahorro energético, ahorro económico y CO₂ equivalente evitado. Documentar el origen de los umbrales. |
| 42 | Localización | Resguardar la dirección exacta y aportar la información geográfica necesaria para reproducir la evaluación del recurso. |
| 43 | Caracterización de la demanda | Identificar el bloque fucsia señalado en Requisitos de diseño y trasladar su desarrollo técnico a Diseño de la instalación. Corregir la ortografía. Mantener en Requisitos los datos de partida que exige la guía. |

## Datos identificados en la fase de preparación

- La tabla de facturación del borrador contiene 13 períodos de julio de 2025 a julio de 2026. Sus filas suman 13.753 kWh, Gs. 5.890.707 de energía activa y Gs. 7.154.000 de facturación total. Se comprobó la suma de las cifras transcritas. Las facturas de origen quedan pendientes de cotejo. Antes de estimar la demanda anual, se debe seleccionar un período representativo y dejar constancia de sus fechas y días facturados.
- La tabla de suministro del borrador identifica a ANDE y deja pendiente la evaluación del punto de conexión. Deben verificarse el perfil temporal de carga, el área útil y las sombras de la cubierta, las características de la acometida, las protecciones y la puesta a tierra. Cada dato se registrará como medido, documentado o supuesto.
- Los artículos, normas, tarifas y fuentes de datos citados en el borrador son pistas de búsqueda. Verificar versión, vigencia y aplicabilidad antes de emplearlos. Documentar el tratamiento de excedentes y la procedencia del factor de emisiones antes de calcular los ahorros y el CO₂ equivalente evitado.

## Material de Energía Solar Fotovoltaica

La carpeta de la asignatura está en C:\Users\HP\OneDrive - pti.org.py\Escritorio\Maestria Energias Renovables\Energia Solar fotovoltaica. El inventario inicial contiene 95 archivos. Se localizaron los capítulos y pasajes pertinentes en nueve PDF.

| Material localizado | Uso en el TFM |
| --- | --- |
| Temas 1 y 3 | Radiación y geometría solar, orientación e inclinación, sombras, pérdidas y configuración eléctrica de los módulos. |
| Temas 6 y 7 | Inversor de conexión a red, requisitos eléctricos, cargas y mantenimiento. |
| Tema 8 | Topología, punto de conexión, dimensionamiento de una instalación conectada a red y protecciones. |
| Clase 7 | Ejercicios de gestión y aprovechamiento de la energía generada. Aplicar al caso solo los elementos pertinentes al autoconsumo en red. |
| Actividad 1 | Trabajo de la autora sobre carta solar, inclinación, separación de paneles y configuración del generador. Sirve para recuperar el procedimiento y aplicarlo con los datos de la vivienda. |
| Actividad 3 y manual PVsyst 8.1 para conexión a red | La actividad corresponde a un sistema aislado en A Coruña y documenta experiencia con PVsyst. El manual de conexión a red es la referencia para configurar la simulación del nuevo caso con los datos de Ciudad del Este. |

El material docente respalda los procedimientos aprendidos. Los requisitos regulatorios y tarifarios se comprobarán para Paraguay y ANDE con las fuentes correspondientes.

## Plan de la fase de preparación

1. Delimitar la necesidad de la vivienda con la propuesta aprobada y los comentarios 2, 9, 10, 11, 13 y 21. En paralelo, preparar la metodología de cálculo que pidió el director.
2. Para cada ecuación, registrar qué calcula, sus variables y unidades, la fuente, los datos de entrada y la comprobación prevista. Contrastar las facturas y las condiciones de la vivienda antes de fijar escenarios e hipótesis.
3. Vincular objetivos, método, resultados y conclusiones en la estructura Tipo 1. Rehacer el estado del arte con antecedentes locales y evidencia sobre tecnologías y componentes.
4. Trabajar en una copia de la plantilla oficial. Registrar en esta bitácora el nombre de cada versión, las fuentes verificadas, los supuestos, las comprobaciones, los comentarios resueltos y las secciones que ya pasaron por Humanizer.

## 8 de noviembre de 2026 · Borrador v0.1

La autora indicó que el crecimiento de la demanda eléctrica en la zona debe fundamentar el problema. Durante el trabajo aportó los 13 recibos originales de ANDE y las coordenadas de la cubierta para medirla en Google Earth. Docs/indicaciones.md ya contiene el mismo texto que la copia de la raíz. Se comprobó su coincidencia antes de elaborar el Word.

### Archivos de esta versión

- [TFM · Borrador v0.1](<TFM - Borrador v0.1.docx>). Manuscrito de trabajo de 35 páginas, con portada, resumen, abstract, índices, 12 capítulos, referencias y anexo. Se siguió la plantilla Tipo 1 y se pasó la redacción en ambos idiomas por thesis-writing y humanizer. Se cotejaron cifras, unidades y citas tras la revisión.
- [Croquis de la cubierta](Calculos/Croquis_cubierta.png). Contorno medido y configuración preliminar de diez módulos. El croquis usa un origen local y se incorpora como Figura 3 del Word.
- [Modelo reproducible](Calculos/modelo_preliminar.py) y [series originales de PVGIS](Calculos/PVGIS_Ciudad_del_Este_2021_2023.zip). Ejecutar el script con Python 3.10 o posterior en una carpeta que contenga el ZIP. Imprime los resultados en JSON y comprueba el cierre del balance de demanda y los cargos de energía.

### Evidencia y decisiones de cálculo

| Tema | Verificación e interpretación |
| --- | --- |
| Demanda regional | El apartado 1.2 de la compilación de ANDE registra 3.201.156 MWh en 2019, 3.297.053 en 2020, 3.466.103 en 2021, 3.414.894 en 2022 y 3.827.806 en 2023. El crecimiento acumulado es 19,6 % y el interanual de 2023 es 12,1 %. La unidad de análisis es el Sistema Este, que comprende Alto Paraná y Canindeyú según el Plan Maestro de Distribución, apartado 3.3.2. |
| Evidencia local | Se incorporaron la planificación de alimentadores para Ciudad del Este y las obras en K15 y Presidente Franco de 2026. En K15, la capacidad instalada pasó de 60 a 100,7 MVA. Las capacidades de transformación se mantienen separadas del consumo regional en MWh y de los datos de la vivienda. |
| Facturas | Se verificaron fechas iniciales y finales, kWh, categoría 142, mínimo de 120 kWh, cargo por energía y total de los 13 recibos de Docs/Facturas ANDE. Los doce ciclos de referencia van del 26/07/2025 al 25/07/2026 y suman 364 días, 12.958 kWh, Gs. 5.556.592 de energía activa y Gs. 6.751.000 en importes totales. La primera factura se conserva como antecedente. |
| Cubierta | Google Earth, consulta del 08/11/2026 en vista cenital con norte arriba. El polígono central visible dio 152,03 m² y 49,23 m de perímetro. El polígono interior occidental dio 46,38 m² y 28,45 m de perímetro. El lado corto mide 5,06 m, con rumbo aproximado de 91,66°, y el largo 9,18 m. Son proyecciones en planta. La dirección, las coordenadas precisas y los identificadores de facturación se excluyeron del Word y el croquis. |
| Cabida | Dos módulos Jinko de 2,274 × 1,134 m por fila, con 20 mm de separación entre marcos, dan 4,57 m de ancho. A 25° de inclinación y con el criterio de 10:00 a 14:00 de hora solar en el solsticio de invierno, el paso entre filas es 1,76 m. Tres, cinco y siete filas ocupan 4,56, 8,08 y 11,61 m. Las opciones de 3,3 y 5,5 kWp pasan a contraste en campo. El ejemplo de cadena de diez módulos da 531 V en la comprobación fría ilustrativa. |
| Recurso y balance | Dos archivos PVGIS 5.3, ERA5, 2021–2023, en un punto representativo de Ciudad del Este. Irradiación media de 1.820 kWh/m² en horizontal, 1.950 kWh/m² en el plano inclinado y 1.466 kWh/kWp de rendimiento medio. Se simularon 27 combinaciones con 3 potencias, 3 fracciones diurnas y 3 pérdidas adicionales por sombra. En el escenario central de 5,5 kWp se estiman 4.681 kWh de autoconsumo, 8.277 kWh de compra y 36,1 % de cobertura. El rango sin sombra adicional entre perfiles es de 23,9 % a 45,6 %. |
| Economía y ambiente | El Pliego N.º 21 reprodujo los 13 cargos base. Se simuló la faja correspondiente a cada ciclo sin ingresos por excedentes. Para 5,5 kWp y 50 % de consumo diurno, el ahorro medio en energía activa es de Gs. 2,07 millones. El umbral de inversión de Gs. 17,9 millones es condicional a 20 años, descuento real del 8 %, reducción anual del ahorro del 0,5 %, operación anual del 1 % de la inversión y ausencia de reposición en esa comparación. El factor operativo de JICA para Paraguay da 0 kg de CO₂ evitados dentro del límite del modelo. |
| Control del Word | Se generaron 20 ecuaciones editables, 3 figuras y 6 tablas. Se actualizaron los tres índices en Word y se verificaron sus campos y referencias. Se exportó el archivo final para inspección visual. Se comprobó la conservación de estilos, márgenes, numeración de secciones y partes de plantilla que no se editaron. |

Fuentes de demanda y regulación consultadas. [Compilación ANDE](https://www.ande.gov.py/finanzas/2.%20COMPILACION%20ESTADISTICA%202003-2023/ANDE%20-%20Compilacion%20Estadistica%202003-2023.pdf) · [Plan Maestro de Distribución](https://www.ande.gov.py/documentos/plan_maestro/RP49741%20ANEXO%20III%20%20Plan%20Maestro%20de%20Distribucion%202024-2033.pdf) · [Obra en K15](https://www.ande.gov.py/interna.php?id=14984) · [Obra en Presidente Franco](https://www.ande.gov.py/interna.php?id=15222) · [Pliego N.º 21](https://www.ande.gov.py/docs/tarifas/Pliego%20de%20Tarifas%20Nro%2021%20-%20Version%20Actualizada%2027-11-2024.pdf) · [Registro de autogeneradores del MOPC](https://minasyenergia.mopc.gov.py/index.php?Itemid=645&id=2410&option=com_content&view=article)

### Estado de los comentarios del director

| ID | Estado en v0.1 |
| --- | --- |
| 1, 4, 42 | Título literal en portada y encabezados, director incorporado y localización precisa reservada. |
| 2, 9, 10, 11, 13, 16, 17, 18, 21, 22, 24 | Nuevo problema y justificación a partir de la demanda regional y la necesidad de reducir las compras de la vivienda. Se separaron la motivación, el contexto y los criterios de diseño. El capítulo 6 desarrolla las ecuaciones. La revisión integral se repite en cada versión. |
| 20, 25, 26, 43 | La normativa y los datos de partida se ubican en el capítulo 5. El balance y las ecuaciones se ubican en el capítulo 6. La aplicación al campo fotovoltaico y al punto de conexión se desarrolla en el capítulo 8. Se sustituyó el texto de origen en la reconstrucción. |
| 29, 32, 33, 34, 35, 36, 39 | Objetivos con un verbo principal, conclusiones en correspondencia, análisis del recurso integrado al desarrollo y tres hipótesis con criterios cuantificados. H1 y H2 se cumplen con el perfil diurno de referencia y dejan de cumplirse con 30 % de consumo diurno. H3 queda vinculada al factor operativo escogido. |
| 23, 27 | Avance en antecedentes de la FPUNE y del atlas PESE-PY, oferta comercial paraguaya y tecnología mundial. Queda por localizar documentación técnica de proyectos fotovoltaicos concretos del CTA y ampliar la comparación de componentes y disponibilidad local con evidencia verificable. |

### Punto de reanudación

1. Conservar el borrador v0.1 como referencia. Incorporar a una nueva versión las mediciones de pendiente, estructura, obstáculos, sombras y accesos de la cubierta.
2. Registrar la carga horaria o subhoraria por fase en el punto de conexión. Confirmar tensión, fases, protecciones, puesta a tierra y condiciones de autogeneración y limitación de vertido con ANDE.
3. Comparar 3,3 y 5,5 kWp con datos de campo, fichas definitivas, unifilar, secciones, protecciones y cotizaciones. La simulación de v0.1 se hizo con PVGIS y el balance propio. El siguiente contraste puede hacerse en PVsyst con el modelo de equipo y sombras.
4. Ampliar el estado del arte y el diseño de detalle antes de la versión de depósito. La extensión exigida y la revisión contra la rúbrica se comprueban sobre esa versión.


## 8 de noviembre de 2026 · Entrega v0.2 para revisión

### Archivos y alcance

- [TFM · Entrega v0.2](<TFM - Entrega v0.2.docx>). Documento de 85 páginas físicas. El cuerpo tiene 66 páginas entre introducción y conclusiones. Se incorporaron los 12 capítulos del Tipo 1, el resumen y el abstract, los índices de contenidos, figuras y tablas, 44 tablas, 8 figuras, 22 ecuaciones editables, 35 referencias y tres anexos. El título y los datos de portada se cotejaron con el tema aprobado. La plantilla oficial conserva su SHA-256 original.
- [Croquis coplanar](Calculos/Croquis_cubierta_v0.2.png) y [esquema unifilar](Calculos/Esquema_unifilar_v0.2.png). Se incorporaron al Word y se guardaron como láminas aparte. El croquis de v0.1 conserva la configuración anterior para el historial.
- [Programa de cálculo](Calculos/modelo_entrega.py), [respuestas originales de PVGIS para norte y sur](Calculos/PVGIS_CDE_16_7_2021_2023.zip), [archivo horario de diseño](Calculos/Perfil_horario_diseno_v0.2.csv) y [resultados y flujos de caja](Calculos/Resultados_v0.2.json). El programa lee el ZIP anterior para la irradiación horizontal y reutiliza la transcripción y la tarifa de modelo_preliminar.py. Ejecutar python Calculos/modelo_entrega.py con Python 3.10 o posterior.
- Se aplicaron thesis-writing y humanizer a la estructura, la redacción y la revisión, incluido el abstract. Se comprobó la correspondencia entre objetivos, hipótesis, método, resultados y conclusiones. Word actualizó los tres índices y se verificaron 136 campos de referencia de página, las ecuaciones nativas y la vista exportada del archivo final. Se corrigieron dos cortes de párrafo detectados en la primera exportación.

### Decisiones técnicas y datos de partida

| Tema | Decisión y procedencia |
| --- | --- |
| Problema | El aumento del 19,6 % del consumo del Sistema Este entre 2019 y 2023 fundamenta el caso. Se distinguen la serie regional en MWh, las ampliaciones de transformación en MVA y la compra de la vivienda. Las obras de K15 y Presidente Franco aportan contexto local. |
| Cubierta | Se retiene el relevamiento cenital de Google Earth del 08/11/2026, 152,03 m² visibles y franja de 46,38 m² con cotas de 5,06 × 9,18 m en planta. La vivienda se informó con dos niveles, tejado de teja y plano sin obstáculos ni sombras cercanas. Se adoptaron 30 % de pendiente y 16,70° a partir de CYPE Paraguay y plano norte de aspecto −178° en PVGIS. La inclinación, la cara norte, las reservas de paso y las condiciones estructurales se tratan como decisiones o requisitos de proyecto. Se resguardan las coordenadas exactas y los datos del suministro. |
| Cabida | Nueve módulos verticales y uno apaisado, todos coplanares, con juntas de 20 mm, banda lateral de servicio de 0,80 m y separación transversal de 0,60 m. Proyección de módulos de 24,70 m². El anclaje, las zonas de grapa, el acceso seguro y la revisión de viento quedan en el plan de verificación. |
| Demanda horaria | Doce ciclos y 364 días de referencia, con 12.958 kWh contrastados con las facturas. El perfil de diseño normaliza cada ciclo y distingue actividad, carga de fondo, fin de semana y respuesta al calor a partir de la temperatura ERA5. En el central, 55,8 % de la energía cae entre 07:00 y 19:00. Reparto por fase 38/33/29, sensibilidad 34/33/33 y 43/35/22. Los datos horarios corresponden al modelo y no se atribuyen a una campaña de medida. El CSV de 2022 cierra en sus 8.736 horas y en cada uno de los doce ciclos. El Word promedia tres años meteorológicos. |
| Acometida y control | Se interpretó el suministro reportado de 220 V trifásico como 220 V fase–neutro y 380 V fase–fase, 50 Hz y neutro presente. Se diseñó una rama para Huawei SUN2000-5K-MAP0 con medidor DTSU666-H, TT y control por fase. El cálculo base usa despacho simétrico limitado por la fase débil. El modo efectivo, el código de red, la medida y la respuesta al perder enlace deben comprobarse antes de conexión. |
| Cadena y protecciones | Una cadena de diez Jinko JKM550M-72HL4-V, PV1, 5,50 kWp y 5 kW de CA. Voc fría 537,88 V a −5 °C, Vmp caliente 310,84 V a 85 °C, Isc de diseño 17,54 A. CC 2 × 6 mm² y 25 m, caída 0,81 %. CA 5G4 mm² y 20 m, caída 0,43 %. Se especificaron seccionamiento, DPS, automático 16 A, diferencial tipo B 100 mA y equipotencialidad. Los valores de tablero y tierra son parámetros de diseño sujetos a coordinación y ensayo. |
| Evaluación | Irradiación norte media de 1.938 kWh/m² en tres años civiles y rendimiento de referencia de 1.456 kWh/kWp. En los 364 días facturados, 7.986 kWh de producción disponible, 4.522 kWh de autoconsumo, 8.436 kWh de compra y 3.465 kWh de recorte de control. Cobertura 34,9 % y aprovechamiento 56,6 %. La comprobación independiente con NOCT da 4.783 kWh útiles. En fase débil de 22 % se obtienen 3.624 kWh útiles. |
| Economía y ambiente | Ahorro de Gs. 1.994.839 al año en energía activa, 35,9 %. Inversión de referencia de Gs. 38.391.100 con dos referencias comerciales y provisiones de proyecto. A 20 años y 8 % real, VAN de Gs. −26.474.136. Umbral de inversión de Gs. 14.283.849. Las cuatro potencias tienen VAN negativo. Se desarrolló 5,50 kWp por continuidad del anteproyecto. 3,30 kWp tiene el VAN menos negativo y 4,40 kWp el menor coste nivelado de energía útil. H1 y H2 se cumplen en el central y dejan de cumplirse en el escenario de fase débil. H3 no se cumple con el factor operativo JICA de 0,000 tCO₂/MWh. |
| Regulación | Ley 7599/2025, Decreto 6034/2026, Resolución 996/2026 y registro del MOPC de hasta 1 MW. Se distingue inscripción de aceptación del paralelo por ANDE. El caso de referencia no monetiza excedentes. |

Referencias incorporadas en esta fase. [Pendiente de teja en CYPE Paraguay](https://paraguay.generadordeprecios.info/obra_nueva/Cubiertas/Inclinadas/Tejados/Cubierta_inclinada_de_tejas.html) · [Perfil residencial FP-UNA](https://www.pol.una.py/2026/aceptan-trabajo-de-investigadores-del-gitv-para-presentacion-en-la-iceer-2026/) · [Balance Nacional de Energía Útil](https://minasyenergia.mopc.gov.py/pdf/BNEU/BEU%20Paraguay%202023.pdf) · [Manual Huawei, edición 13](https://info.support.huawei.com/Energy/info/en_US/solar/docView/EDOC1100366802) · [Catálogo comercial de módulos](https://mp.com.py/catalogo-de-paneles-solares/) · [Referencia comercial de inversor](https://nissei.com/py/ferreteria-construccion/ferreteria/sistemas-de-energia-alternativa/inversores-y-convertidores/inversor-hibrido-trifasico-5kw-huawei-ele-129564) · [IEA PVPS Snapshot 2026](https://iea-pvps.org/wp-content/uploads/2026/05/Snapshot-2026-FS.pdf) · [JICA Climate-FIT 7.0](https://www.jica.go.jp/english/activities/issues/climate/__icsFiles/afieldfile/2026/04/08/Appendix_en_ver7.0.pdf)

### Comentarios del director y punto de reanudación

- Los comentarios 1, 4 y 42 quedan atendidos con título literal, director y privacidad. Los 2, 9 a 11, 13, 16 a 18, 21, 22 y 24 se tratan en el planteamiento, la justificación y la delimitación de la escala regional y de vivienda.
- El capítulo 2 amplía los comentarios 23 y 27 con antecedentes institucionales paraguayos, el CTA y la documentación de un prototipo fotovoltaico universitario con otra aplicación, comparativa de tecnologías y precios, y evidencia internacional. La documentación pública consultada no permite atribuir al CTA resultados medidos de un sistema residencial conectado a red. Si el director aporta un informe de esa naturaleza, revisar 2.3 y 2.4.
- Los comentarios 20, 25, 26 y 43 se abordan separando los requisitos, las ecuaciones de cálculo y el dimensionamiento aplicado. Los 29, 32 a 36 y 39 se contrastan con la matriz de objetivos y los resultados de las tres hipótesis.
- Retomar desde esta v0.2 cuando llegue la devolución del director. Registrar cada observación y su capítulo antes de editar. Las entradas de mayor valor para una siguiente revisión son la inspección de pendiente, faldón, estructura y acceso, el registro subhorario por fase, la confirmación de la acometida y el esquema de tierra, las condiciones de ANDE y una cotización con alcance equivalente. La planilla del Anexo C vincula esos datos con las verificaciones. Actualizar el modelo, las tablas, los índices y la paginación en ese orden. El contraste independiente usado en esta entrega es el modelo NOCT con irradiación PVGIS.



## 10–11 de noviembre de 2026 · Entrega v0.3 y revisión del método de cálculo

La autora pidió rehacer el cálculo siguiendo como referencia principal el TFM de Yulisa Mishell Álvarez Arcos y las actividades cursadas en Energía Solar Fotovoltaica. Solicitó presentar primero las fórmulas y sus variables, y después aplicar los datos de la vivienda para obtener demanda, potencia FV, módulos, orientación, inclinación, inversor, conductores, producción, presupuesto y evaluaciones. También solicitó un plano en AutoCAD o formato equivalente. Se aplicaron thesis-writing y humanizer durante la revisión y se cotejaron las cifras después de editar.

### Entregables de esta revisión

- [TFM · Entrega v0.3](<TFM - Entrega v0.3.docx>). Word de 93 páginas físicas. Hay 71 páginas de cuerpo entre introducción y conclusiones, seis de referencias y seis de anexos. Conserva el título y la plantilla Tipo 1. Contiene 45 tablas, siete figuras y 50 referencias. El capítulo 6 plantea 33 ecuaciones con sus variables, unidades y procedencia. El capítulo 8 desarrolla 16 sustituciones editables y las comprobaciones de diseño. Las variables de la prosa también se formatearon con notación matemática. Se actualizaron los tres índices y 141 referencias de página.
- [Plano CAD editable](Planos/Instalacion_FV_v0.3.dxf) y [dos láminas en PDF A3](Planos/Planos_instalacion_FV_v0.3.pdf). El DXF usa unidades de milímetros y contiene ambas láminas en espacio modelo, con capas de módulos, rieles, CC, CA, PE, control, texto y cotas. FV-01 presenta planta, anclajes y sección a 1:50 en A3. FV-02 contiene el unifilar sin escala física. Se verificaron 266 entidades, diez rectángulos de módulo dentro de la franja y auditoría DXF sin errores. El PDF se inspeccionó visualmente y tiene dos páginas A3.
- [Cálculo secuencial](Calculos/dimensionamiento_v0_3.py), [resultados v0.3](Calculos/Resultados_v0.3.json), [serie de inclinación 21,3°](Calculos/PVGIS_CDE_21_3_2021_2023.zip) y [generador del plano](Calculos/plano_v0_3.py). El cálculo reutiliza las facturas, la función tarifaria, la distribución horaria y los ZIP de la v0.2. El plano requiere ezdxf, reportlab, pypdfium2 y Pillow. El Anexo B da las instrucciones de reproducción. Los PNG de Planos permiten incorporar las figuras a la memoria.

### Fuentes docentes y referencia principal

Se leyó el PDF completo de Álvarez Arcos, con atención al planteamiento de modelos de las páginas 45–50, la aplicación de las páginas 53–58 y el presupuesto y evaluación desde las páginas 65–70. La portada identifica el trabajo de 2021 sobre el Comercial Xaviercito y su sistema autónomo. Se adoptó el orden de fórmulas, datos y sustitución para la vivienda conectada a red del tema aprobado.

Se revisaron la Actividad 1 de la autora, la Actividad 2 grupal de Laura Juliana Pérez Jaramillo, Clara Rolón Duré y Andrés Francisco Vanegas Basanta, y la Actividad 3 de PVsyst. Se consultaron los temas 1, 3, 6, 7 y 8, las clases 2, 4, 5, 7, 9, 10, 11 y 12 y el ejercicio resuelto de la Actividad 1. La bibliografía incorpora los materiales que sostienen directamente el método y el Anexo D recoge una matriz de procedencia.

| Paso | Procedencia y aplicación |
| --- | --- |
| Demanda | Facturas de ANDE, duración efectiva y cálculo de kWh/día. La Actividad 3 respalda la distinción entre potencia y energía de cargas. |
| Potencia y módulos | Relación de demanda objetivo, HSP y PR de Álvarez Arcos y Clase 5. Redondeo superior del número de módulos y potencia instalada resultante. |
| Geometría solar | Actividad 1 y Clase 2 para alturas solares, inclinación, ocupación y separación. Comparación de la fórmula empírica de Álvarez Arcos con la pendiente del proyecto mediante PVGIS. |
| Inversor y cadenas | Actividad 2 y Tema 8 para relación CC/CA, tensión, corriente y límites de seguimiento. Fichas definitivas del equipo local de corriente alta. |
| Conductores | Álvarez Arcos, Actividad 2 y Tema 8 para caída admisible, sección mínima, selección comercial y caída real. Comprobación de ampacidad con fichas primarias de Prysmian y Nexans. |
| Producción | Producto de HSP, kWp, PR y días. Contraste con PVGIS como en la Actividad 2. Balance horario posterior para autoconsumo y recorte. |
| Economía y ambiente | Fórmulas generales en metodología y cifras después. Tarifa ANDE, partidas y flujos con la misma energía útil, factor JICA y frontera de ciclo de vida. |

### Resultados y decisiones

| Aspecto | Resultado de v0.3 |
| --- | --- |
| Demanda | 12.958 kWh en 364 días. Media de 35,60 kWh/día. El perfil de diseño coloca 55,80 % entre 07:00 y 19:00 y da 19,8645 kWh/día de objetivo. La energía de cada ciclo sigue fijada por las facturas. |
| Predimensionamiento | HSP de 5,3094 h/día, PR de proyecto de 0,75 y potencia requerida de 4,9885 kWp. El redondeo a módulos de 0,550 kWp requiere diez módulos y da 5,50 kWp. Con toda la demanda diaria el cociente daría 8,94 kWp. El proyecto comprueba la coincidencia de la demanda diurna en lugar de asignar producción a consumos nocturnos. |
| Inclinación | La fórmula de referencia da 21,30°. La cubierta de proyecto conserva 16,70° y la orientación norte de aproximadamente 2° hacia el este. PVGIS da 8.007,22 kWh/año para 16,70° y 8.056,42 para 21,30°, diferencia de 0,61 %. |
| Módulo y montaje | YH SUNPRO YHP550W de MP Energía Propia, Gs. 954.000 por unidad. Vmp 42,13 V, Imp 13,06 A, Voc 50,10 V e Isc 13,90 A, coincidentes con la familia YH550W-36MH de Isola. La oferta local identifica marco de 30 mm y la ficha de familia muestra 35 mm. Confirmar variante y grapas con el proveedor. La longitud y anchura usadas son 2,279 y 1,134 m. |
| Estructura | Sistema de referencia Romagnole comercializado por Energía 360, con perfiles RS-327 de 4,80 m y fijación para teja de la familia RS-223. Despiece de ocho perfiles, 30 anclajes, 16 grapas finales, 12 intermedias y accesorios. Se provisiona el precio de esas partidas y se mantiene la verificación del soporte real, las zonas de apriete y el viento NP 196. |
| Planta | Tres filas de tres módulos verticales y un módulo apaisado. Envolvente de 3,442 × 8,275 m, caras de 25,84 m² y proyección de 24,75 m². Los módulos comienzan a 1,20 m del límite oeste de la franja para que los rieles respeten la banda de servicio de 0,80 m más el borde de 0,30 m. Márgenes norte y sur de 0,453 m. |
| Inversor y control | Se especificó Huawei SUN2000-5KTL-M1 de corriente alta, ofertado por Electropar. La referencia de precio minorista de Nissei para 5 kW es Gs. 12.871.000. Se confirma en placa la versión de 13,5 A y 19,5 A por MPPT. Una cadena de diez módulos en PV1, relación CC/CA de 1,10 y 5 kW nominales de CA. El manual FusionSolar con SDongle de 2023 lista la familia M1 y describe la limitación Single-phase power. Se especifican DTSU666-H y SDongleA-05, con ensayo del modo por fase y del estado seguro. |
| Compatibilidad | Voc fría de 554,73 V a −5 °C con tolerancia de 3 %, Vmp caliente de 322,72 V a 85 °C y Vmp fría de 470,59 V. Isc de diseño de 17,90 A. El coeficiente de Vmp de −0,39 %/°C se aproxima a partir de potencia y corriente y se declara en el cálculo. |
| Conductores | CC de 25 m de ida, Cu, mínimo por caída de 4,16 mm² y selección de 6 mm². Caída de diseño 3,36 V, 1,04 %. CA de 20 m, corriente máxima 8,50 A, mínimo de 1,74 mm² y selección 5G4 mm². Caída 1,66 V, 0,44 %. Se documentan las condiciones de ampacidad y los factores que deben verificarse por montaje. |
| Producción y consumo | Fórmula anual de HSP y PR, 7.993,92 kWh. Contraste PVGIS, 8.007,22 kWh en el año civil medio. Sobre los 364 días facturados, 7.986 kWh disponibles y 4.522 útiles bajo la limitación por fase. Cobertura de 34,9 %. |
| Presupuesto y finanzas | Coste directo de Gs. 38.261.000 y contingencia de Gs. 3.826.100. Inversión de Gs. 42.087.100. Los precios sin publicación de proveedor son provisiones. Ahorro anual medio de energía de Gs. 1.994.839. VAN de Gs. −30.533.015 a 20 años y 8 % real, con mantenimiento de 1 % y recambio en el año 13. Umbral de inversión de Gs. 14.283.849. |
| Ambiente | Se conserva la frontera operativa JICA de 0,000 tCO₂/MWh. El resultado operativo evitado es 0,000 tCO₂e/año. El análisis de materiales y ciclo de vida se mantiene con su frontera y limitaciones. |

Fuentes primarias incorporadas. [TFM de Álvarez Arcos en Re-UNIR](https://reunir.unir.net/items/cebd84aa-dee1-4ef0-9e6c-8b7f58a4b756) · [Módulo ofertado en Paraguay](https://mp.com.py/producto/panel-solar-yh-sunpro-yhp550w/) · [Ficha de familia YH550W](https://www.zjisola.com/product-5468116967345280.html) · [Inversor de Electropar](https://www.electropar.com.py/producto/inversor-hibrido-trifasico-5kw-huawei/consultar) · [M1 de corriente alta](https://solar.huawei.com/admin/asset/v1/pro/view/e60b9d03018f4744852eb07e72d730a1.pdf) · [Sistema FusionSolar y SDongle](https://solar.huawei.com/admin/asset/v1/pro/view/f23454e0dfcf41d0aa4a5062cce50801.pdf) · [Estructuras Romagnole en Paraguay](https://energia360.com.py/brands/romagnole/) · [CYPE para soporte inclinado](https://paraguay.generadordeprecios.info/rehabilitacion/Instalaciones/Electricas/Solar_fotovoltaica/IEF003_Estructura_soporte_para_modulo_sola.html)

### Verificaciones y reanudación

Se inspeccionaron las 93 páginas de la exportación del Word final. Resumen de 223 palabras y abstract de 203. Se verificaron ecuaciones editables, variables, cálculos, secciones y tablas, y se conservó el SHA-256 original de la plantilla oficial. La comparación de las dos exportaciones solo detectó 219 píxeles distintos en una línea de la página física 28, con texto idéntico. Se revisó la exportación final y se mantuvo el diseño. El DXF pasó la auditoría de formato y de cabida. El PDF de planos es A3 de dos páginas.

SHA-256 de la entrega Word, 9dcf4c5b434f7eec2db0316977f18b978f54ebe52cd8df79f9b54b959dfc7175. El tamaño es 583.268 bytes.

Retomar desde v0.3 y consultar primero la petición metodológica de esta entrada. Ante cambios del director, actualizar demanda y condiciones, ejecutar dimensionamiento_v0_3.py, revisar fichas y presupuesto, regenerar el DXF/PDF, trasladar los resultados al Word y actualizar sus índices y paginación. El perfil horario, PR, ruta de cable y precios provisionados son parámetros de proyecto. La pendiente y la orientación del faldón, el apoyo estructural, la acometida, la puesta a tierra, el modo de control y los modelos de suministro se confirman con sus documentos o ensayos al pasar a ejecución. Estas comprobaciones ya figuran en los anexos, sin presentarlas como medidas realizadas.



## 11 de noviembre de 2026 · Control de versiones del TFM

Se configuró la rama inicial main y el remoto origin para TFM-UNIR en GitHub. El repositorio remoto es público. El primer commit del proyecto reúne las versiones de entrega, los cálculos reproducibles, las series de PVGIS, los planos, las referencias y las instrucciones. La transcripción de consumos anonimizados está en los cálculos y en el anexo de facturación del TFM.

Los trece comprobantes originales de ANDE contienen identificadores del suministro. El borrador con comentarios del director contiene coordenadas precisas. Ambos insumos quedan en OneDrive y se excluyen de Git mediante .gitignore junto con los temporales de elaboración y de Office. El CSV horario contiene 8.736 filas con calendario, temperatura, irradiación y energía.

El documento base para retomar la redacción es TFM - Entrega v0.3.docx. La entrada anterior describe cómo actualizar los cálculos, planos e índices. [Repositorio TFM-UNIR](https://github.com/clararolon99/TFM-UNIR)
