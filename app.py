from flask import Flask, render_template_string, url_for

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Dhanush Gallery</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f3f3;
        }

        h1 {
            text-align: center;
            padding: 25px 0;
            font-size: 42px;
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 25px;
            max-width: 1400px;
            margin: auto;
            padding: 20px;
        }

        .video-frame {
            grid-column: 2 / span 2;
            grid-row: 1 / span 2;
            background: black;
            padding: 14px;
            border-radius: 22px;
        }

        .video-frame video {
            width: 100%;
            height: 100%;
            border-radius: 16px;
            object-fit: cover;
        }

        .frame {
            background: black;
            padding: 10px;
            border-radius: 20px;
        }

        .frame img {
            width: 100%;
            height: 560px;
            object-fit: cover;
            border-radius: 16px;
        }

        @media (max-width: 900px) {
            .gallery {
                grid-template-columns: 1fr;
            }

            .video-frame {
                grid-column: auto;
                grid-row: auto;
            }
        }
    </style>
</head>

<body>

<h1>Dhanush Gallery</h1>

<div class="gallery">

    <!-- Center Video -->
    <div class="video-frame">
        <video controls autoplay muted loop>
            <source src="{{ video }}" type="video/mp4">
        </video>
    </div>

    <!-- Photos -->
    {% for photo in photos %}
    <div class="frame">
        <img src="{{ photo }}">
    </div>
    {% endfor %}

</div>

</body>
</html>
"""

# 🔒 ONLY FILE PATHS (NO url_for HERE)
PHOTOS = [
    "photos/WhatsApp Image 2026-02-04 at 9.58.43 PM (1).jpeg",
    "photos/WhatsApp Image 2026-02-04 at 9.58.43 PM.jpeg",
    "photos/WhatsApp Image 2026-02-04 at 9.58.45 PM (1).jpeg",
    "photos/WhatsApp Image 2026-02-04 at 9.58.44 PM (1).jpeg",
    "photos/WhatsApp Image 2026-02-04 at 9.58.44 PM.jpeg",
    "photos/WhatsApp Image 2026-02-04 at 9.58.45 PM (2).jpeg",
    "photos/WhatsApp Image 2026-02-04 at 9.58.45 PM.jpeg",
    "photos/WhatsApp Image 2026-02-04 at 9.58.46 PM (1).jpeg",
    "photos/WhatsApp Image 2026-02-04 at 9.58.46 PM.jpeg",
]

VIDEO = "videos/WhatsApp Video 2026-02-05 at 11.04.06 PM.mp4"

@app.route("/")
def home():
    photos = [url_for("static", filename=p) for p in PHOTOS]
    video = url_for("static", filename=VIDEO)
    return render_template_string(HTML, photos=photos, video=video)

# ❌ NO app.run()  (important for GitHub Pages build)
