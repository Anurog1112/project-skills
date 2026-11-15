"""Build one self-contained Markdown download per project type."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ("website", "dashboard", "app")


def build():
    common = (ROOT / "skills/professional-web/SKILL.md").read_text(encoding="utf-8")
    quality = (ROOT / "skills/frontend-ui-quality/SKILL.md").read_text(encoding="utf-8")
    output = ROOT / "profiles"
    output.mkdir(exist_ok=True)
    entries = []
    for name in PROFILES:
        template = (ROOT / "templates" / (name + ".md")).read_text(encoding="utf-8")
        content = (
            common.rstrip() + "\n\n"
            + template.rstrip() + "\n\n"
            + "# Embedded Frontend UI Quality checklist\n\n"
            + "The following source skill retains its metadata and Provenance. "
            + "Use the reporting format and available checks defined in Professional Web above.\n\n"
            + quality.rstrip() + "\n"
        )
        raw = content.encode("utf-8")
        relative = "profiles/" + name + ".md"
        (ROOT / relative).write_bytes(raw)
        entries.append({
            "profile": name,
            "path": relative,
            "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "sources": [
                "skills/professional-web/SKILL.md",
                "templates/" + name + ".md",
                "skills/frontend-ui-quality/SKILL.md",
            ],
        })
    manifest_path = ROOT / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["release"] = "professional-web-pilot-2"
    manifest["profiles"] = entries
    manifest_path.write_bytes((json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    return entries


if __name__ == "__main__":
    print(json.dumps(build(), indent=2))
