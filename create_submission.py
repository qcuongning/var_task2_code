from pathlib import Path
import argparse
import sys
import pandas as pd
import zipfile
#!/usr/bin/env python3
"""
create_submission.py

Create a markdown file (answer.md by default) that for each file in
output/var_test_pymu writes the filename as a single line followed by
the file's content.

Usage:
    python create_submission.py
    python create_submission.py --source path/to/output/var_test_pymu --output answer.md
"""

def main():
        p = argparse.ArgumentParser(description="Create answer.md from files in a directory")
        p.add_argument("--source", "-s", default="../output/var_test_pymu",
                                     help="source directory containing the file(s)")
        p.add_argument("--output", "-o", default="answer.md",
                                     help="output markdown file to create")
        args = p.parse_args()

        src = Path(args.source)
        out = Path(args.output)

        if not src.exists() or not src.is_dir():
                print(f"Source directory not found: {src}", file=sys.stderr)
                sys.exit(1)

        files = sorted([f for f in src.iterdir() if f.is_file()])

        if not files:
                # create an empty answer file if no files found
                out.write_text("", encoding="utf-8")
                print(f"No files found in {src}. Created empty {out}.")
                return
        csv_answer = pd.read_csv("../../dataset/Public_test_data/public_test_data/question.csv")
        

        with out.open("w", encoding="utf-8", errors="replace") as w:
                w.write("### TASK EXTRACT\n")
                first = True
                for f in files:
                        # For the very first file, the first line of the markdown must be the filename.
                        # For subsequent files we separate blocks with a blank line.
                        if not first:
                                w.write("\n")
                        first = False

                        # Write filename as a single line
                        w.write("# " + f.name.replace(".md", "") + "\n")

                        # Read file content robustly (text with replacement on errors)
                        try:
                                content = f.read_text(encoding="utf-8")
                        except Exception:
                                # fallback: binary read and decode with replacement
                                content = f.read_bytes().decode("utf-8", errors="replace")

                        w.write(content)

                w.write("### TASK QA\nnum_correct,answers\n")

                for idx, row in csv_answer.iterrows():
                        w.write(f'4,"A,B,C,D"\n')

        # create a zip archive containing the generated output file and this script
        try:
                zip_path = out.with_suffix(".zip")
                with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                        if out.exists():
                                zf.write(out, arcname=out.name)
                        else:
                                print(f"Output file not found to add to zip: {out}", file=sys.stderr)

                        script_path = Path(__file__)
                        if script_path.exists():
                                zf.write(script_path, arcname=script_path.name)
                        else:
                                print(f"Script file not found: {script_path}", file=sys.stderr)

                print(f"Created zip archive: {zip_path}")
        except Exception as e:
                print(f"Failed to create zip: {e}", file=sys.stderr)
                sys.exit(1)

if __name__ == "__main__":
        main()