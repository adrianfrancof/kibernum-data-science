# Data Science Bootcamp - AI Coding Guidelines

## Project Structure & Architecture

This is a **Data Science Bootcamp (Bootcamp 0024)** educational repository organized with a hierarchical module-session structure:
- `M1/`, `M2/`, etc. = **Modules** (course units)
- `S1/`, `S2/`, etc. = **Sessions** within each module
- Content includes Jupyter notebooks, Python scripts, and practical exercises

**Key Pattern**: Files follow Spanish naming conventions with numbered sequences:
- `06 - Demo Sentencias Básicas Python.ipynb`
- `09 - Guia Tipos de datos.ipynb`
- `actividad_calculadora.py`

## Content Creation Standards

When creating educational content:

### Jupyter Notebooks
- **Spanish language** for all explanations and markdown cells
- **Bilingual comments** in code cells (Spanish explanations, English variable names)
- Structure: Title → Learning objectives → Theory → Code examples → Exercises
- Use markdown cells for section headers and explanations
- Example pattern from `06 - Demo Sentencias Básicas Python.ipynb`:
  ```markdown
  # Sentencias Básicas Python
  - Operaciones Aritméticas
  - Variables
  - Cadenas de Caracteres
  ```

### Python Scripts
- **Function-based approach** for exercises (see `actividad_calculadora.py`)
- **Error handling** with Spanish user messages
- **Input validation** with try-catch blocks
- **Docstrings in Spanish** at file top explaining the exercise
- Main execution pattern:
  ```python
  def calculadora():
      print("Bienvenido a la calculadora Python")
      # implementation
  ```

## Development Workflow

### File Organization
- Place content in appropriate `M{X}/S{Y}/` folders
- Use descriptive Spanish filenames with numbers for sequencing
- Keep practical exercises as separate `.py` files
- Notebooks should be self-contained with all necessary imports

### Code Standards
- **Spanish for user-facing text** (print statements, error messages, prompts)
- **English for technical elements** (variable names, function names)
- **Comprehensive error handling** for educational clarity
- **Interactive console input/output** for practical exercises

## Educational Patterns

### Progressive Learning Structure
- Start with basic concepts (`Tipos de datos`, `Variables y operadores`)
- Build to complex operations (`Sentencias Condicionales`)
- Include practical applications (calculator exercise)

### Content Types
1. **Demo notebooks**: Concept introduction with live examples
2. **Guía notebooks**: Comprehensive guides with theory and practice
3. **Actividad scripts**: Standalone practical exercises

When adding new content, follow the existing numbering scheme and maintain the Spanish educational approach while ensuring code examples are clear and executable.