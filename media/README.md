# Stretch demonstration media

This folder is where you drop real photos or short video clips demonstrating
each stretch. Nothing in the app shows a "Watch demo" button until you add an
entry pointing to a file here — there's no placeholder or broken UI in the
meantime.

## How to add one

1. Put the file in this folder (e.g. `media/figure-4-stretch.mp4`).
2. Open `index.html`, find `const STRETCH_MEDIA = {` (search for it), and add
   a line like:

   ```js
   "hip__0": { type: "video", src: "media/figure-4-stretch.mp4" },
   ```

   The key on the left (`"hip__0"`) is `<region>__<cause index>` — it matches
   the `data-cause-id` on that card. The easiest way to find the right key
   for a specific cause: open the app, browser dev tools, inspect the
   `.cause-card` you want, and read its `data-cause-id` attribute.

3. **Many causes share the exact same physical stretch.** Point them at the
   same file rather than re-shooting it — e.g. every "Figure-4 stretch"
   variant (there are 4: glutes, hip, hamstring, knee) can all reference
   `media/figure-4-stretch.mp4`.

## What to film (priority order)

You don't need 68 separate clips — the same handful of physical positions
repeat across most causes. These ~26 cover the large majority of the app:

**Upper body**
- Jaw opening stretch
- Neck side-bend stretch
- Chin tuck (+ gentle extension)
- Cross-body shoulder stretch + sleeper stretch
- Doorway pec stretch
- Pendulum swing (frozen shoulder)
- Thoracic extension over a foam roller
- Seated thoracic rotation + cat-cow
- Wrist flexion stretch (palm down, pulling hand back)
- Wrist extension stretch (palm up, pulling hand back)
- Prayer stretch / reverse prayer stretch
- Thumb-tuck wrist stretch
- Nerve glide — wrist/median (fingers + wrist extended, elbow straight)
- Nerve glide — elbow/ulnar (arm straight, wrist back)

**Lower body**
- Kneeling hip flexor stretch
- Child's pose / knee-to-chest stretch
- Figure-4 stretch, lying on back
- Seated figure-4 / pigeon pose
- Standing hamstring stretch
- Standing quad stretch
- Standing IT band stretch (cross leg behind, lean away)
- Nerve glide — seated leg extension (sciatic)
- Wall calf stretch (straight-leg and bent-knee versions)
- Kneeling shin stretch
- Plantar fascia stretch (pull toes back)
- Ankle circles

## Format guidance

- **Video**: 5-10 seconds, looping, no audio needed (the player mutes and
  loops automatically). Vertical or square framing works best on mobile.
  MP4 (H.264) is the safest format for broad browser support.
- **Photo**: a single clear frame showing the end position of the stretch is
  often enough — doesn't need to be video.
- Keep file sizes small (compress video — a few MB max) since this is a
  website people load on mobile data.
- Name files descriptively and in lowercase-with-hyphens, matching the
  stretch name (e.g. `doorway-pec-stretch.mp4`, `figure-4-stretch.jpg`).

## Filming accuracy

Whoever demonstrates these (ideally a physio, trainer, or someone confident
in correct form) should:
- Show the *end position* clearly, not just the movement into it
- Keep the described cues visible (e.g. "ear toward shoulder," "knee pointing
  down") so the video matches the text instructions exactly
- Avoid overstretching or forcing range — these are meant to model the safe,
  moderate version described in the app, not maximum flexibility
