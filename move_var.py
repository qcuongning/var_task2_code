#!/usr/bin/env python3
"""
Move each folder's main.md from dataset/Training_data/output/<folder>/main.md
to a single folder and rename it to <folder>.md (avoid overwriting).
"""
import os
import shutil
import argparse

def unique_path(path):
    base, ext = os.path.splitext(path)
    i = 1
    while os.path.exists(path):
        path = f"{base}_{i}{ext}"
        i += 1
    return path

def collect_main_md(src_root, dst_root):
    os.makedirs(dst_root, exist_ok=True)
    moved = 0
    for entry in os.listdir(src_root):
        folder = os.path.join(src_root, entry)
        if not os.path.isdir(folder):
            continue
        # look for a file named "main.md" case-insensitive
        main_file = None
        for fname in os.listdir(folder):
            if fname.lower() == "main.md":
                main_file = os.path.join(folder, fname)
                break
        if not main_file or not os.path.isfile(main_file):
            continue
        dest_name = f"{entry}.md"
        dest_path = os.path.join(dst_root, dest_name)
        dest_path = unique_path(dest_path)
        shutil.move(main_file, dest_path)
        moved += 1
        print(f"Moved: {main_file} -> {dest_path}")
    print(f"Total moved: {moved}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Collect main.md files and rename them to <folder>.md")
    p.add_argument("--src", default="../../dataset/Training_data/output", help="source root containing subfolders")
    p.add_argument("--dst", default="../data/var/markdown", help="destination folder")
    args = p.parse_args()
    collect_main_md(args.src, args.dst)