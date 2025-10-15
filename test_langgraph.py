"""
Simple test to verify LangGraph installation
"""
try:
    from langgraph.graph import StateGraph, END
    from typing import TypedDict
    print("LangGraph successfully imported!")
    print("StateGraph available")
    print("Installation verified - You're ready to build with LangGraph!")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please run: pip install -r requirements.txt")
