import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format="[%(asctime)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

project_name = "soccer_ai"

# Tailored directory and file structure for the Soccer AI Chatbot SaaS
list_of_files = [
    # GitHub Actions / CI
    ".github/workflows/ci.yml",
    
    # Core Source Code
    f"src/{project_name}/__init__.py",
    
    # API Layer (FastAPI)
    f"src/{project_name}/api/__init__.py",
    f"src/{project_name}/api/routes.py",
    f"src/{project_name}/api/schemas.py",          # Pydantic models for req/res
    
    # Chat & LangChain Layer
    f"src/{project_name}/chat/__init__.py",
    f"src/{project_name}/chat/chain.py",           # LangChain runnable setup
    f"src/{project_name}/chat/prompts.py",         # System prompts and templates
    f"src/{project_name}/chat/memory.py",          # Redis/chat history management
    
    # Insights Engine (Deterministic stats processing)
    f"src/{project_name}/insights/__init__.py",
    f"src/{project_name}/insights/engine.py",      # Delta computation, ranking logic
    f"src/{project_name}/insights/models.py",      # PlayerContext pydantic model
    
    # Guardrails & Safety
    f"src/{project_name}/guardrails/__init__.py",
    f"src/{project_name}/guardrails/safety.py",    # Prompt injection, PII filtering
    f"src/{project_name}/guardrails/escalation.py",# Injury/mental health escalation logic
    
    # Storage Layer (Snapshots & History)
    f"src/{project_name}/storage/__init__.py",
    f"src/{project_name}/storage/snapshot_db.py",  # Postgres/Mongo for stat history
    f"src/{project_name}/storage/redis_client.py", # Redis connection for chat memory
    
    # Evaluation Layer
    f"src/{project_name}/evals/__init__.py",
    f"src/{project_name}/evals/langsmith_eval.py", # LangSmith evaluation scripts
    
    # Configuration
    "config/config.yaml",
    ".env.example",
    
    # Project Root Files
    "requirements.txt",
    "pyproject.toml",                             # Modern Python project metadata
    "main.py",                                    # FastAPI entry point
    "README.md",
    
    # Testing
    "tests/__init__.py",
    "tests/test_insights.py",
    "tests/test_chain.py",
    
    # Research & Experimentation
    "research/01_prompt_testing.ipynb",
    "research/02_langchain_prototype.ipynb",
]

def create_project_structure():
    logging.info(f"Starting project structure creation for: {project_name}")
    
    for filepath_str in list_of_files:
        filepath = Path(filepath_str)
        
        # Create parent directories if they don't exist
        if filepath.parent != Path("."):
            filepath.parent.mkdir(parents=True, exist_ok=True)
            logging.info(f"Ensured directory exists: {filepath.parent}")
        
        # Create file if it doesn't exist or is empty
        if not filepath.exists() or filepath.stat().st_size == 0:
            # Add a tiny placeholder to Python files so they aren't completely blank
            if filepath.suffix == ".py":
                filepath.write_text('"""Placeholder for soccer_ai module."""\n')
            elif filepath.suffix == ".yml" or filepath.suffix == ".yaml":
                filepath.write_text("# Configuration file\n")
            elif filepath.suffix == ".md":
                filepath.write_text(f"# {project_name}\n\nSoccer AI Chatbot SaaS\n")
            elif filepath.name == ".env.example":
                filepath.write_text("OPENAI_API_KEY=\nREDIS_URL=\nDATABASE_URL=\n")
            else:
                filepath.touch()
                
            logging.info(f"Created file: {filepath}")
        else:
            logging.info(f"File already exists (skipping): {filepath}")

    logging.info("✅ Project structure setup completed successfully!")

if __name__ == "__main__":
    create_project_structure()