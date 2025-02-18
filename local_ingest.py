import os

output_file = "combined_code.md"

with open(output_file, "w", encoding="utf-8") as out:
    out.write("# Combined Code\n\n")
    
    # Walk through the current directory and subdirectories
    for root, dirs, files in os.walk("."):
        # Sort for consistent order
        for file in sorted(files):
            # Skip the output file itself
            if file == output_file:
                continue

            # Get the relative path for the file
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, ".")
            
            # Check if the file is a Python file (extension .py, case-insensitive)
            if file.lower().endswith(".py"):
                # Add a header with the relative path
                out.write(f"## {relative_path}\n\n")
                # Open a Python code block and add a comment with the file path at the top
                out.write("```python\n")
                out.write(f"# {relative_path}\n")
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        out.write(f.read())
                except Exception as e:
                    out.write(f"# Error reading file: {e}\n")
                out.write("\n```\n\n")
            else:
                # For non-Python files, just add a header with the relative path and a note
                out.write(f"## {relative_path}\n\n")
                out.write(f"**Non-Python file:** {relative_path}\n\n")

print(f"Combined Markdown file created.")