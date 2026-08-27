# Environment Setup

This section prepares the Python environment required for NetAutoAI.

## Prerequisites

- Python 3.11 or newer
- Git
- VS Code or another Python-compatible editor

## 1. Verify Python

```bash
python --version

2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
Linux/macOS
source .venv/bin/activate
Windows
.venv\Scripts\activate
4. Install Netmiko
pip install netmiko
5. Verify Netmiko
pip show netmiko
6. Save dependencies
pip freeze > requirements.txt

Why use a virtual environment?

A virtual environment keeps the project's Python dependencies isolated from other Python projects on the system.