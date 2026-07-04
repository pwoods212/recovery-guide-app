from PIL import Image, ImageDraw

PINE = (47, 74, 61, 255)
CREAM = (251, 251, 247, 255)
ACCENT = (193, 98, 46, 255)

def draw_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    pad = int(size * 0.08)
    d.rounded_rectangle([pad, pad, size - pad, size - pad], radius=int(size * 0.22), fill=PINE)

    cx = size / 2
    s = size * 0.62  # figure scale reference (viewbox-ish)
    top = size * 0.20

    def pt(x, y):
        return (cx + (x - 50) / 100 * s, top + (y - 10) / 90 * s)

    lw = max(2, int(size * 0.045))

    # head
    hx, hy = pt(50, 16)
    r = size * 0.075
    d.ellipse([hx - r, hy - r, hx + r, hy + r], fill=CREAM)

    # torso (simple rounded trapezoid)
    p1, p2, p3, p4 = pt(35, 34), pt(65, 34), pt(58, 62), pt(42, 62)
    d.polygon([p1, p2, p3, p4], fill=CREAM)

    # arms
    d.line([pt(30, 34), pt(22, 52)], fill=CREAM, width=lw)
    d.line([pt(70, 34), pt(78, 52)], fill=CREAM, width=lw)

    # legs
    d.line([pt(42, 62), pt(40, 88)], fill=CREAM, width=lw)
    d.line([pt(58, 62), pt(60, 88)], fill=CREAM, width=lw)

    # accent glow dot (the "massage marker" motif) on the shoulder
    gx, gy = pt(70, 34)
    gr = size * 0.045
    d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=ACCENT)

    return img

for size in [192, 512]:
    draw_icon(size).save(f"/Users/paulwoods/muscle-recovery-app/icons/icon-{size}.png")

draw_icon(180).save("/Users/paulwoods/muscle-recovery-app/icons/apple-touch-icon.png")
print("done")
