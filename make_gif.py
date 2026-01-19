# make_gif.py
# Crea un GIF animado con Pillow (sin imágenes externas)

from PIL import Image, ImageDraw
import math

WIDTH, HEIGHT = 320, 180
FRAMES = 40
BG = (10, 12, 25)          # fondo oscuro
STAR = (200, 200, 255)     # estrellitas
ORB = (120, 210, 255)      # orb principal
ORB_GLOW = (60, 120, 200)  # brillo

frames = []

for t in range(FRAMES):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    # Estrellas (patrón simple que “parpadea”)
    for i in range(25):
        x = (i * 37 + t * 3) % WIDTH
        y = (i * 23 + t * 2) % HEIGHT
        if (i + t) % 7 == 0:
            draw.point((x, y), fill=STAR)

    # Movimiento del orb (onda)
    x = int((WIDTH / 2) + math.sin(t * 0.25) * 90)
    y = int((HEIGHT / 2) + math.cos(t * 0.20) * 35)

    # Brillo (círculos concéntricos)
    for r in range(22, 0, -1):
        alpha_color = (
            ORB_GLOW[0],
            ORB_GLOW[1],
            ORB_GLOW[2],
        )
        # dibujamos “glow” con varios tamaños
        draw.ellipse((x - r, y - r, x + r, y + r), outline=ORB_GLOW)

    # Orb sólido
    draw.ellipse((x - 10, y - 10, x + 10, y + 10), fill=ORB)

    frames.append(img)

# Guardar GIF
frames[0].save(
    "output.gif",
    save_all=True,
    append_images=frames[1:],
    duration=60,   # ms por frame (60ms ≈ 16.6 fps)
    loop=0
)

print("✅ GIF creado: output.gif")
