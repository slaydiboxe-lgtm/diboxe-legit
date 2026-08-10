import json
from pathlib import Path

root = Path("assets/scammers")
allowed = {".png", ".jpg", ".jpeg", ".webp", ".gif"}

def clean(value):
    return str(value or "").strip()

reports = []

# New format: one folder per scammer.
for folder in sorted(root.iterdir(), key=lambda p: p.name.lower()):
    if not folder.is_dir() or folder.name.startswith("."):
        continue

    info_file = folder / "info.json"
    info = {}
    if info_file.is_file():
        try:
  info = json.loads(info_file.read_text(encoding="utf-8"))
        except Exception:
  info = {}

    images = []
    for p in sorted(folder.rglob("*"), key=lambda p: p.as_posix().lower()):
        if p.is_file() and p.suffix.lower() in allowed:
  rel = p.relative_to(root).as_posix()
  images.append(rel)

    if not images:
        continue

    profile_name = clean(info.get("profile"))
    profile = None
    if profile_name:
        candidate = folder / profile_name
        if candidate.is_file() and candidate.suffix.lower() in allowed:
  profile = candidate.relative_to(root).as_posix()

    if not profile:
        profile = images[0]

    evidence = [x for x in images if x != profile]

    reports.append({
        "id": clean(info.get("id")) or folder.name,
        "name": clean(info.get("name")) or folder.name.replace("_", " ").replace("-", " ").title(),
        "username": clean(info.get("username")),
        "platform": clean(info.get("platform")),
        "description": clean(info.get("description")),
        "profile": profile,
        "evidence": evidence,
        "images": images
    })

# Backward compatibility: images directly inside assets/scammers/.
root_images = [
    p for p in sorted(root.iterdir(), key=lambda p: p.name.lower())
    if p.is_file() and p.suffix.lower() in allowed
]
for p in root_images:
    title = p.stem.replace("_", " ").replace("-", " ").strip().title()
    reports.append({
        "id": p.stem,
        "name": title or "Scammer Report",
        "username": "",
        "platform": "",
        "description": "",
        "profile": p.relative_to(root).as_posix(),
        "evidence": [],
        "images": [p.relative_to(root).as_posix()]
    })

(root / "index.json").write_text(
    json.dumps(reports, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8"
)
