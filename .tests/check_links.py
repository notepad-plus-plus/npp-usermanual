import re
import sys
import os

failed = 0

def slugify(text):
    """Converts header text to a GitHub-compatible anchor slug."""
    slug = text.lower().strip()
    slug = re.sub(r'[^\w\s/-]', '', slug)   # Most punctuation becomes empty
    slug = re.sub(r'\xA0', '', slug)        # Remove NBSP
    slug = re.sub(r'\s+', '-', slug)        # Spaces to hyphens
    slug = re.sub(r'/+', '-', slug)         # Forward slashes to hyphens
    slug = re.sub(r'[-]+', '-', slug)       # Collapse multiple hyphens to single
    return slug

def validate_file(file_path):
    """Checks internal #anchors within a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    # 1. Map all possible jump targets
    # Find normal headers
    headers = re.findall(r'^#+\s+(.*?)\s*$', content, re.MULTILINE)
    # Support <a name="anchor"> or <div id="anchor">
    explicit_anchors = re.findall(r'(?:name|id)=["\']([^"\']+)["\']', content)
    # Support hugo's # header name here {#customAnchor}
    custom_anchors = re.findall(r'^#+\s+.*?{#(.*?)}\s*$', content, re.MULTILINE)

    valid_targets = set(explicit_anchors) | set(custom_anchors)
    for h in headers:
        valid_targets.add(slugify(h))

    # 2. Find all local anchor links: [Text](#anchor)
    internal_links = re.findall(r'\[(?:[^\]]+)\]\(#([^\)\s:]+)[^\)]*\)', content)

    # 3. Store all invalid internal links
    broken = [link for link in internal_links if link not in valid_targets]

    # 4. Find and store all / (root) links that aren't to /docs
    badroot_links = re.findall(r'\[(?:[^\]]+)\]\((/[^\s\)]+)[^\)]*\)', content)
    broken.extend(badroot_links)

    # X. Report all broken links -- invalid internal links and invalid root links
    if broken:
        print(f"❌ {file_path}: Found {len(set(broken))} broken link(s)")
        for link in sorted(set(broken)):
            hchar = '#' if link in internal_links else ''
            print(f"   ✗ {hchar}{link}")

        ##if badroot_links:
        ##    for b in sorted(set(badroot_links)):
        ##        print(f"   - [BADROOT] {b}")

        ##for vt in sorted(valid_targets):
        ##    print(f"   :: valid = {vt}")

        global failed
        failed = -2
    elif internal_links:
        print(f"✅ {file_path}: {len(internal_links)} links verified.")

def main():
    global failed
    # If a specific file is passed via command line
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isfile(target):
            validate_file(target)
        else:
            print(f"Error: '{target}' is not a valid file.")
            failed = -3
    else:
        # Default recursive behavior
        content_dir = 'content'
        if not os.path.exists(content_dir):
            print(f"Error: '{content_dir}/' directory not found.")
            failed = -3

        print(f"Scanning '{content_dir}/' hierarchy...")
        for root, _, files in os.walk(content_dir):
            for file in files:
                if file.endswith(".md"):
                    validate_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
    if failed:
        print(f"\n\n❌ Link Checking FAILED ({failed})")
        sys.exit(int(failed))
    else:
        print(f"\n\n✅ Link Checking PASSED")
