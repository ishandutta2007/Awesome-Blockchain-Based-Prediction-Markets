import re
import subprocess
import json
import os

readme_path = r"C:\Users\ishan\Documents\Projects\Awesome-Blockchain-Based-Prediction-Markets\README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "## 💻 Open-Source Software & Self-Hosted Solutions (Primary Emphasis)\n\n"
end_marker = "\n\nSee the"

start_idx = content.find(start_marker) + len(start_marker)
end_idx = content.find(end_marker, start_idx)

section = content[start_idx:end_idx]

lines = section.split("\n")
repo_lines = []
other_lines = []

def get_stars(owner_repo):
    try:
        res = subprocess.run(["gh", "repo", "view", owner_repo, "--json", "stargazerCount"], capture_output=True, text=True, check=True)
        data = json.loads(res.stdout)
        return data.get("stargazerCount", 0)
    except Exception as e:
        return -1

parsed_lines = []

current_item = []
for line in lines:
    if line.startswith("- "):
        if current_item:
            parsed_lines.append("\n".join(current_item))
        current_item = [line]
    elif line.startswith("  -") or line.strip() == "" or line.startswith(" "):
        if current_item:
            current_item.append(line)
        else:
            other_lines.append(line)
if current_item:
    parsed_lines.append("\n".join(current_item))

items_with_stars = []

for item in parsed_lines:
    if not item.startswith("- **Additional Repos**:"):
        # find github links
        match = re.search(r"https://github\.com/([^/)\s]+)/([^/)\s]+)", item)
        if match:
            owner, repo = match.groups()
            owner_repo = f"{owner}/{repo}"
            stars = get_stars(owner_repo)
            if stars >= 0:
                # Add badge
                badge = f"[![Stars](https://img.shields.io/github/stars/{owner}/{repo}?style=social&color=white)](https://github.com/{owner}/{repo}/stargazers)"
                
                # We need to insert the badge after the repo name
                # E.g. - **Augur** [](https://github.com/AugurProject/augur)
                # Should become - **Augur** [![Stars](...)](...) [](https://github.com/AugurProject/augur)
                # But wait, the instructions say "the star badge beside each opensource name".
                # Let's put it right after the name.
                
                # regex to find the name: - **Name**
                item = re.sub(r"(- \*\*.*?\*\*)", r"\1 " + badge, item, count=1)
                items_with_stars.append((stars, item))
            else:
                items_with_stars.append((-1, item))
        else:
            items_with_stars.append((-1, item))
    else:
        # Additional repos is a sublist, we don't sort it but keep it at the end
        items_with_stars.append((-2, item))

# Sort by stars descending
items_with_stars.sort(key=lambda x: x[0], reverse=True)

new_section_lines = []
for stars, item in items_with_stars:
    new_section_lines.append(item)

new_section = "\n".join(new_section_lines)

new_content = content[:start_idx] + new_section + content[end_idx:]

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_content)
