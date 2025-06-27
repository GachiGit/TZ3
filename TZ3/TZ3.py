import sys
import json

def parse_version(version_str):
    
    return tuple(map(int, version_str.strip().split(".")))

def generate_versions_from_template(template):
    parts = template.split(".")
    versions = []

    for i in range(2):
        new_parts = []
        for part in parts:
            if part == "*":
                new_parts.append(str(3 + i * 4))
            else:
                new_parts.append(part)
        versions.append(".".join(new_parts))

    return versions

def main():
    if len(sys.argv) != 3:
        print("Using: python TZ3.py <target_version> <config_file>")
        return

    target_version_str = sys.argv[1]
    config_file = sys.argv[2]

    try:
        with open(config_file, "r") as f:
            templates = json.load(f)
    except Exception as e:
        print(f"Error with reading config file: {e}")
        return

    all_versions = []

    for key, template in templates.items():
        generated = generate_versions_from_template(template)
        all_versions.extend(generated)

    all_versions.sort(key=parse_version)

    print("All generated versions")
    for version in all_versions:
        print(version)

    print(f"\nVersions < {target_version_str}")
    target_version = parse_version(target_version_str)
    for version in all_versions:
        if parse_version(version) < target_version:
            print(version)

if __name__ == "__main__":
    main()
