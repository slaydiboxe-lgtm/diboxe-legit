import json
from pathlib import Path

root = Path("assets/services")
allowed = {".png", ".jpg", ".jpeg", ".webp", ".gif"}

root.mkdir(parents=True, exist_ok=True)
products = []

for folder in sorted(root.iterdir(), key=lambda p: p.name.lower()):
    if not folder.is_dir() or folder.name.startswith("."):
        continue

    info_file = folder / "info.json"
    if not info_file.is_file():
        continue

    try:
        info = json.loads(info_file.read_text(encoding="utf-8"))
    except Exception:
        continue

    images = [
        p for p in sorted(folder.iterdir(), key=lambda p: p.name.lower())
        if p.is_file() and p.suffix.lower() in allowed
    ]
    image = info.get("image")
    if image:
        candidate = folder / str(image)
        if not candidate.is_file():
            image = None

    if not image and images:
        image = images[0].name

    image_path = ""
    if image:
        image_path = "assets/services/" + folder.name + "/" + str(image).replace("\\", "/")

    products.append({
        "id": str(info.get("id") or folder.name),
        "name": str(info.get("name") or folder.name.replace("-", " ").replace("_", " ").title()),
        "price": info.get("price", ""),
        "currency": str(info.get("currency") or "€"),
        "description": str(info.get("description") or ""),
        "category": str(info.get("category") or ""),
        "badge": str(info.get("badge") or ""),
        "available": info.get("available", True) is not False,
        "image": image_path,
        "order_message": str(info.get("order_message") or "")
    })

(root / "index.json").write_text(
    json.dumps(products, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8"
)
