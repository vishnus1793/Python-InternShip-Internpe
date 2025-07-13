# Directory Crawler

## Overview

Directory Crawler is a Python-based tool that recursively scans a given directory and its subdirectories, collecting detailed information about each file and directory. It efficiently handles hidden files, symbolic links, and permission errors, making it suitable for comprehensive filesystem analysis.

## Features

- **Recursive Scanning:** Traverses all subdirectories.
- **File Information:** Collects file name, absolute path, size, and type (file, directory, symlink, etc.).
- **Handles Edge Cases:** Supports hidden files, symbolic links, and gracefully handles permission errors.
- **Flexible Output:** Prints results to the console or saves as a JSON file.
- **Cross-Platform:** Works on Linux, macOS, and Windows (Python 3.6+).

## Installation

1. Ensure you have Python 3.6 or higher installed:
   ```sh
   python3 --version
   ```
2. Download or clone this repository.
3. (Optional) Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
4. No external dependencies are required (uses only Python standard library).

## Usage

Run the script from the command line:

```sh
python3 directory_crawler.py [DIRECTORY] [-o OUTPUT.json]
```

- `DIRECTORY` (optional): Path to the directory to scan. Defaults to the current directory.
- `-o OUTPUT.json` (optional): Write output to a JSON file instead of printing to the console.

### Examples

Scan the current directory and print results:
```sh
python3 directory_crawler.py
```

Scan a specific directory and save results to a file:
```sh
python3 directory_crawler.py /path/to/scan -o results.json
```

## Output Format

The output is a JSON array, where each entry contains:

- `name`: File or directory name
- `path`: Absolute path
- `size`: Size in bytes (or `null` if not accessible)
- `type`: One of `file`, `directory`, `symlink`, `other`, `permission_error`, or `error`
- `error`: (optional) Error message if access failed

Example output:
```json
[
  {
    "name": "example.txt",
    "path": "/home/user/example.txt",
    "size": 1234,
    "type": "file"
  },
  {
    "name": ".hiddenfile",
    "path": "/home/user/.hiddenfile",
    "size": 56,
    "type": "file"
  },
  {
    "name": "somedir",
    "path": "/home/user/somedir",
    "size": 4096,
    "type": "directory"
  },
  {
    "name": "brokenlink",
    "path": "/home/user/brokenlink",
    "size": null,
    "type": "symlink"
  },
  {
    "name": "restricted",
    "path": "/home/user/restricted",
    "size": null,
    "type": "permission_error",
    "error": "Permission denied"
  }
]
```

## License

This project is licensed under the MIT License. 