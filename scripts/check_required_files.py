import os
import sys

# List of required files
required_files = [
    "README.md",
    ".gitignore"
]

missing_files = []

for file in required_files:
    if not os.path.exists(file):
        missing_files.append(file)

if missing_files:
    print("❌ Missing required files:")
    for file in missing_files:
        print(f"- {file}")
    sys.exit(1)  # Fail the pipeline
else:
    print("✅ All required files are present.")
    sys.exit(0)  # Success
