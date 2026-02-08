from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Dhanush Gallery</title>
    <style>
        body { margin:0; font-family:Arial; background:#f3f3f3 }
        h1 { text-align:center; padding:25px }
        .gallery {
            display:grid;
            grid-template-columns:repeat(4,1fr);
            gap:25px;
            max-width:1400px;
            margin:auto;
            padding:20px;
        }
        .video-frame {
            grid-column:2/span 2;
            background:black;
            padding:14px;
            border-radius:20px;
        }
        video { width:100%; border-radius:14px }
        .frame img {
            width:100%;
            height:560px;
            object-fit:cover;
            border-radius:14px;
        }
        @media(max-width:700px){
            .gallery{ grid-template-columns:1fr }
            .video-frame{ grid-column:auto }
        }
    </style>
</head>
<body>

<h1>Dhanush Gallery</h1>

<div class="gallery">

<div class="video-frame">
<video autoplay muted loop controls>
<source src="static/videos/WhatsApp Video 2026-02-05 at 11.04.06 PM.mp4">
</video>
</div>

<img src="static/photos/WhatsApp Image 2026-02-04 at 9.58.43 PM (1).jpeg">
<img src="static/photos/WhatsApp Image 2026-02-04 at 9.58.43 PM.jpeg">
<img src="static/photos/WhatsApp Image 2026-02-04 at 9.58.45 PM (1).jpeg">
<img src="static/photos/WhatsApp Image 2026-02-04 at 9.58.44 PM (1).jpeg">
<img src="static/photos/WhatsApp Image 2026-02-04 at 9.58.44 PM.jpeg">
<img src="static/photos/WhatsApp Image 2026-02-04 at 9.58.45 PM (2).jpeg">
<img src="static/photos/WhatsApp Image 2026-02-04 at 9.58.45 PM.jpeg">
<img src="static/photos/WhatsApp Image 2026-02-04 at 9.58.46 PM (1).jpeg">
<img src="static/photos/WhatsApp Image 2026-02-04 at 9.58.46 PM.jpeg">

</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)
