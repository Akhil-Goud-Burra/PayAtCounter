# To Create and Activate Virtual Environment in Power Shell
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1

# Install Dependencies
pip install -r requirements.txt

# Verify LangGraph Installation
python test_langgraph.py