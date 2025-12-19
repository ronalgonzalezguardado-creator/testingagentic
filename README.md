# 🚀 Quickstart: Proyecto Agentic en Python

Un proyecto simple y funcional para comenzar a experimentar con agentes inteligentes en Python.

## 📋 Descripción

Este proyecto implementa un agente simple que:
- ✅ Recibe una tarea
- 🧠 Razona usando un modelo de lenguaje (LLM)
- 🔧 Ejecuta herramientas básicas (calculadora, hora, echo)

## 🎯 Características

- **Simple**: Código minimalista y fácil de entender
- **Funcional**: Listo para usar en segundos
- **Flexible**: Funciona con o sin API de OpenAI (modo demo)
- **Extensible**: Fácil de agregar nuevas herramientas

## 🛠️ Requisitos

- Python 3.10 o superior
- (Opcional) Clave API de OpenAI para usar LLM real

## ⚡ Instalación Rápida

### 1. Clonar el repositorio

```bash
git clone https://github.com/ronalgonzalezguardado-creator/testingagentic.git
cd testingagentic
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. (Opcional) Configurar API de OpenAI

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env y agregar tu API key
# OPENAI_API_KEY=tu_clave_aqui
```

**Nota**: Si no configuras la API key, el agente funciona en **modo demo** con respuestas simuladas.

## 🎮 Uso

### Ejecutar ejemplos predeterminados

```bash
python main.py
```

Esto ejecutará tres tareas de ejemplo:
- Calcular 25 * 4
- Obtener la hora actual
- Hacer echo de un mensaje

### Ejecutar una tarea personalizada

```bash
python main.py "Calculate 15 + 27"
python main.py "What time is it?"
python main.py "Echo: Hello World"
```

## 📚 Ejemplo de Salida

```
============================================================
🚀 Quickstart Agentic Project
============================================================

📋 Running example tasks...

🤖 Agent received task: Calculate 25 * 4
💭 Reasoning...
🧠 Agent thinks: I'll calculate that for you: calculator(25 * 4)
🔧 Executing tool: calculator(25 * 4)
✅ Result: Result: 100

🤖 Agent received task: What time is it?
💭 Reasoning...
🧠 Agent thinks: I'll get the current time for you: get_time()
🔧 Executing tool: get_time()
✅ Result: Current time: 2025-12-19 06:34:15

🤖 Agent received task: Echo: Hello, Agentic World!
💭 Reasoning...
🧠 Agent thinks: I'll echo your message: echo(Hello, Agentic World!)
🔧 Executing tool: echo(Hello, Agentic World!)
✅ Result: Echo: Hello, Agentic World!

============================================================
✨ Done!
============================================================
```

## 🔧 Herramientas Disponibles

El agente incluye tres herramientas básicas:

1. **calculator(operation)**: Evalúa expresiones matemáticas
   - Ejemplo: `calculator(10 + 5 * 2)`

2. **get_time()**: Obtiene la fecha y hora actual
   - Ejemplo: `get_time()`

3. **echo(message)**: Devuelve el mensaje recibido
   - Ejemplo: `echo(Hello World)`

## 🎨 Estructura del Proyecto

```
testingagentic/
├── main.py              # Script principal con agente y herramientas
├── requirements.txt     # Dependencias del proyecto
├── .env.example        # Plantilla de configuración
├── .gitignore          # Archivos a ignorar en Git
└── README.md           # Este archivo
```

## 🧩 Cómo Funciona

1. **Agente recibe tarea**: El usuario proporciona una instrucción
2. **Razonamiento**: El agente (o LLM) analiza qué herramienta usar
3. **Ejecución**: Se ejecuta la herramienta apropiada
4. **Resultado**: Se muestra el resultado al usuario

## 🚀 Extender el Agente

Para agregar una nueva herramienta, simplemente añádela a la clase `Tools`:

```python
class Tools:
    @staticmethod
    def mi_nueva_herramienta(param: str) -> str:
        """Descripción de la herramienta."""
        # Tu lógica aquí
        return f"Resultado: {param}"
```

Y regístrala en el diccionario `available_tools` del agente:

```python
self.available_tools = {
    "calculator": self.tools.calculator,
    "get_time": self.tools.get_time,
    "echo": self.tools.echo,
    "mi_nueva_herramienta": self.tools.mi_nueva_herramienta,  # Nueva
}
```

## 📝 Notas

- El proyecto está diseñado para ser simple y didáctico
- En modo demo (sin API key), usa lógica basada en reglas
- Con API key de OpenAI, usa razonamiento real con LLM
- No incluye arquitectura compleja intencionalmente
- Ideal como punto de inicio para proyectos más complejos

## 🤝 Contribuir

Este es un proyecto de aprendizaje. ¡Siéntete libre de experimentar y mejorarlo!

## 📄 Licencia

Proyecto de código abierto para aprendizaje.
