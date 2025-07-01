import os
import yaml
import json
from typing import List, Dict

def parse_markdown(file_path: str) -> Dict:
    """Parse markdown file front matter and return metadata."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if lines[0].strip() != '---':
        raise ValueError(f"Missing front matter in {file_path}")

    front_matter_lines = []
    for line in lines[1:]:
        if line.strip() == '---':
            break
        front_matter_lines.append(line)
    front_matter = yaml.safe_load(''.join(front_matter_lines)) or {}
    front_matter['source_path'] = file_path
    return front_matter

def traverse_handbook(path: str) -> List[Dict]:
    """Traverse path and collect metadata for markdown files."""
    metadata_list = []
    for root, _, files in os.walk(path):
        for name in files:
            if name.endswith('.md'):
                file_path = os.path.join(root, name)
                try:
                    meta = parse_markdown(file_path)
                    metadata_list.append(meta)
                except Exception as exc:
                    print(f"Skipping {file_path}: {exc}")
    return metadata_list

if __name__ == '__main__':
    handbook_dir = os.environ.get('HANDBOOK_DIR', 'handbook')
    metadata = traverse_handbook(handbook_dir)
    print(json.dumps(metadata, indent=2))
