mindmap
  root((Traductores y Compiladores))
    Introducción
      Traductor
        "Convierte programa fuente → programa objeto"
        Ejemplo: "C a Pascal"
    Tipos de Traductores
      Ensamblador (Assembler)
        "Fuente: ensamblador"
        "Objeto: código máquina"
        "Correspondencia 1 a 1"
        Ejemplo: "LD HL, #0100 → 65h.00h.01h"
        Ventajas
          "Veloces"
          "Exactos"
        Desventajas
          "Difícil de escribir/leer"
          "Dependiente de máquina"
      Intérprete (Interpreter)
        "Lee y ejecuta sentencia por sentencia"
        "Permite agregar sentencias en ejecución"
        Ejemplos: "BASIC, Python, Ruby, JS"
      Compilador (Compiler)
        "Fuente: alto nivel"
        "Objeto: bajo nivel"
        "Analiza todo el programa"
        "Genera programa objeto → ejecución rápida"
        Ejemplos: "C, C++, Pascal, Fortran, COBOL, Go"
        Historia
          1951 Grace Hopper: A-0 (UNIVAC)
          1954 John Backus: FORTRAN (IBM 704)
    Diferencias
      "Intérprete → ejecuta directamente"
      "Compilador → genera ejecutable binario"
    Herramientas de Compilación
      Editores
        "Leer/escribir programas"
        "Integrados en IDEs"
        "Formato ASCII"
      Preprocesadores
        "Sustituye macros"
        "Incluye librerías"
        "Elimina comentarios"
      Enlazadores (Linkers)
        Unen módulos en ejecutable
        Enlazan con librerías (.lib / .dll)
      Cargadores (Loaders)
        "Asignan direcciones de memoria"
        "Código reubicable → direcciones reales"
      Depuradores (Debuggers)
        "Detectar y corregir errores"
        "Ejecución paso a paso"
      Desensambladores
        "Código máquina → ensamblador"
      Decompiladores
        "Código máquina → alto nivel"
      Transpiladores
        Fuente → otro lenguaje/version
        Ejemplo: Babel (JS moderno → antiguo)
    Funcionamiento Compilador
      Etapas
        Análisis
          "Genera estructuras intermedias"
        Síntesis
          "Genera salida desde estructuras intermedias"
      Fases
        Frontend
          "Fuente → código intermedio"
        Backend
          "Código intermedio → código final"
      Tablas
        "Símbolos → variables, funciones, parámetros"
        "Tipos → básicos y definidos"
      Gestión de errores
        "En todas las fases"
        "Informa ubicación y tipo de error"
    Fases Detalladas
      Analizador Léxico
        "Agrupa caracteres en tokens"
      Analizador Sintáctico
        "Tokens → árbol sintáctico"
      Analizador Semántico
        "Verifica tipos y reglas semánticas"
      Generador de Código Intermedio
        "Código ensamblador objetivo"
      Optimizador
        "Reduce instrucciones"
      Generador de Código Final
        "Código máquina optimizado"
    Creación de Lenguaje de Programación
      "Definir propósito del lenguaje"
      "Especificación léxica, sintáctica, semántica"
      "Definir código intermedio y final"
      "Elegir lenguaje base e implementación"
    Diseño del Compilador
      "Diagramas de Tombstone"
    Tipos de Lenguajes
      "Alto nivel"
      "Bajo nivel"
      "Intermedios"

Link a Mermaid: https://www.mermaidchart.com/app/projects/ce7befff-14ab-49aa-bde9-41ec8ad8fd5e/diagrams/f3979dee-a91a-4e87-9dd1-a4edfe7774fd/version/v0.1/edit