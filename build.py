from app import app
import os
import shutil

OUTPUT = "docs"

with app.app_context():
    html = app.test_client().get("/").data.decode("utf-8")

# create docs folder
os.makedirs(OUTPUT, exist_ok=True)

# write index.html
with open(f"{OUTPUT}/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# copy static files
if os.path.exists(f"{OUTPUT}/static"):
    shutil.rmtree(f"{OUTPUT}/static")

shutil.copytree("static", f"{OUTPUT}/static")

print("✅ Website created successfully")
