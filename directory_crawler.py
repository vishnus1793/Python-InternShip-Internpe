#!/usr/bin/env python3
"""
directory_crawler.py
--------------------
A Python-based directory crawler that recursively scans a given directory and its subdirectories, collecting information such as file names, sizes, types, and paths. Handles hidden files, symbolic links, and permission errors efficiently.
"""
import os
import sys
import argparse
import json
from typing import List, Dict, Any

def get_file_info(root: str, name: str) -> Dict[str, Any]:
    path = os.path.join(root, name)
    try:
        stat = os.lstat(path)
        file_type = (
            'symlink' if os.path.islink(path) else
            'directory' if os.path.isdir(path) else
            'file' if os.path.isfile(path) else
            'other'
        )
        return {
            'name': name,
            'path': os.path.abspath(path),
            'size': stat.st_size,
            'type': file_type
        }
    except PermissionError:
        return {
            'name': name,
            'path': os.path.abspath(path),
            'size': None,
            'type': 'permission_error',
            'error': 'Permission denied'
        }
    except Exception as e:
        return {
            'name': name,
            'path': os.path.abspath(path),
            'size': None,
            'type': 'error',
            'error': str(e)
        }

def crawl_directory(directory: str) -> List[Dict[str, Any]]:
    results = []
    for root, dirs, files in os.walk(directory, onerror=None, followlinks=False):
        # Include hidden files and directories
        entries = files + dirs
        for name in entries:
            info = get_file_info(root, name)
            results.append(info)
    return results

def main():
    parser = argparse.ArgumentParser(description='Recursively crawl a directory and collect file information.')
    parser.add_argument('directory', nargs='?', default='.', help='Directory to crawl (default: current directory)')
    parser.add_argument('-o', '--output', help='Output file (JSON). If not specified, prints to stdout.')
    args = parser.parse_args()

    directory = os.path.abspath(args.directory)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning directory: {directory}")
    results = crawl_directory(directory)

    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2)
            print(f"Results written to {args.output}")
        except Exception as e:
            print(f"Error writing to output file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(json.dumps(results, indent=2))

if __name__ == '__main__':
    main() 