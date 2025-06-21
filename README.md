![Image](https://github.com/user-attachments/assets/9bff182b-a438-4e39-92af-3a4e89df8037)

# 🔧 Three Address Code Generator (TAC Compiler Project)

This project is a **mini compiler** built using Python and Flask that takes high-level expressions and generates:

- ✅ Tokens (Lexical Analysis)
- ✅ Abstract Syntax Tree (AST)
- ✅ Three Address Code (TAC)
- ✅ Quadruples (Intermediate Representation)
- ✅ AST Image via Graphviz

It supports arithmetic expressions, conditional statements (`if`, `if-else`), and can be easily extended to support loops (`while`, `for`, etc.).

---

## 🚀 Features

- 🧠 Converts infix to postfix (Shunting Yard algorithm)
- 🌳 Builds Abstract Syntax Tree (AST)
- ✍️ Generates intermediate code (TAC)
- 🧾 Produces quadruples (4-tuples for expressions)
- 📷 Renders AST as image using Graphviz
- 🌐 Interactive Web Interface using Flask + HTML + Jinja2

---

## 🛠️ Tech Stack

| Component    | Technology       |
|--------------|------------------|
| Language     | Python 3.x       |
| Frontend     | HTML5, CSS3, Jinja2 |
| Backend      | Flask            |
| Visualization| Graphviz (for AST) |
| Rendering    | Digraph (graphviz Python module) |

---

## 🔄 Compilation Process

1. **Lexical Analysis**  
   - Tokenizes the input using `lexer.py`

2. **Parsing**  
   - Converts to postfix and builds AST (`parser.py`)

3. **Intermediate Code Generation**  
   - Generates Three Address Code (`code_generator.py`)
   - Converts to Quadruples (`representation.py`)

4. **AST Visualization**  
   - Draws tree using `Graphviz` via `save_ast_image`

5. **Web Interface**  
   - Input/output rendered using Flask and Jinja2 templates

---

## 📥 Installation

```bash
git clone https://github.com/Jatin9826/ThreeaddreshCode.git
cd ThreeaddreshCode
pip install -r requirements.txt
