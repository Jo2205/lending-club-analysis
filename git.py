# Create comprehensive .gitignore
print("📝 CREATING .gitignore:")
print("="*80)

gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
venv/
env/
ENV/
.venv

# Jupyter Notebook
.ipynb_checkpoints
*/.ipynb_checkpoints/*

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Data Files (IMPORTANT - Don't upload large data!)
data/raw/*.xlsx
data/raw/*.csv
data/raw/*.xls
data/raw/*.parquet
data/raw/*.zip
*.xlsx
*.csv
!outputs/reports/*.csv  # Allow small report CSVs

# Large processed data (optional - comment out if you want to include)
outputs/data/processed_data.csv

# Models (large files)
outputs/models/*.pkl
outputs/models/*.h5
outputs/models/*.joblib

# Sensitive Information
*.env
.env
config_local.py
secrets.py
credentials.json
*.pem
*.key

# OS Files
.DS_Store
Thumbs.db
desktop.ini

# Logs
*.log
logs/

# Temporary files
tmp/
temp/
*.tmp

# Output files that are too large (optional)
# outputs/visualizations/*.png  # Uncomment if images are too large

# Specific project exclusions
outputs/data/*.csv  # Large processed datasets
data/processed/*.csv
"""

# Save .gitignore with UTF-8 encoding
with open('.gitignore', 'w', encoding='utf-8') as f:
    f.write(gitignore_content)

print("✅ .gitignore created!")
print("\n📋 What will be EXCLUDED from Git:")
print("   ❌ Large data files (CSV, Excel)")
print("   ❌ Trained models (.pkl)")
print("   ❌ Virtual environments")
print("   ❌ IDE config files")
print("   ❌ Sensitive credentials")
print("\n📋 What WILL BE included:")
print("   ✅ Code (.py, .ipynb)")
print("   ✅ Small reports")
print("   ✅ Visualizations (PNG)")
print("   ✅ Documentation (README, .txt)")