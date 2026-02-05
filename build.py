from app import app
import os, shutil

OUTPUT = "docs"

with app.app_context():
    html = app.test_client().get("/").data.decode("utf-8")

os.makedirs(OUTPUT, exist_ok=True)

with open(f"{OUTPUT}/index.html", "w", encoding="utf-8") as f:
    f.write(html)

if os.path.exists(f"{OUTPUT}/static"):
    shutil.rmtree(f"{OUTPUT}/static")

shutil.copytree("static", f"{OUTPUT}/static")

print("✅ Website built successfully")
