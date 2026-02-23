import json
import re

INPUT_FILE = "roadmaps.json"
OUTPUT_FILE = "clean_roadmaps.json"

# Words/phrases to REMOVE completely
BLOCK_PHRASES = [
    "roadmap",
    "roadmap.sh",
    "find the detailed version",
    "along with other similar",
    "visit the following",
    "shout out",
    "helped",
    "review and publish",
    "personal recommendation",
    "opinion",
    "linkedin profile",
    "github",
    "interactive version",
    "more roadmaps",
    "keep learning",
    "continue learning"
]

def is_valid_node(node):

    lower = node.lower()

    for phrase in BLOCK_PHRASES:
        if phrase in lower:
            return False

    if len(node.split()) > 6:
        return False

    if len(node.strip()) < 4:
        return False

    return True

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

cleaned = {}

for skill, content in data.items():

    nodes = content["nodes"]
    edges = content["edges"]

    valid_nodes = [n for n in nodes if is_valid_node(n)]

    valid_edges = [
        [a, b]
        for a, b in edges
        if a in valid_nodes and b in valid_nodes
    ]

    cleaned[skill] = {
        "nodes": valid_nodes,
        "edges": valid_edges
    }

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(cleaned, f, indent=2)

print("Clean roadmap file generated successfully!")
