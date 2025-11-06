# Stock Photos Added to Garage Sale Items

## Summary
Successfully added stock photos for all 25 garage sale items. Images are web-optimized (400x300px max) and stored in `/static/images/`.

## Images Downloaded and Assigned

### Kitchen & Home (4 items)
- **KitchenAid Stand Mixer** → `kitchenaid-mixer.jpg`
- **Vitamix Blender** → `vitamix-blender.jpg`
- **DeLonghi Espresso Maker** → `delonghi-espresso.jpg`
- **SodaStream** → `sodastream.jpg`

### Sonos Audio (6 items)
- **Sonos Beam Gen 2** → `sonos-beam-gen2.jpg`
- **Sonos Sub Mini** → `sonos-sub-mini.jpg`
- **Sonos Beam Gen 1** → `sonos-beam-gen1.jpg`
- **Sonos One SL** → `sonos-one-sl.jpg`
- **Sonos Five** → `sonos-five.jpg`

### Music Production (5 items)
- **Boss RC-505 Loop Station** → `boss-rc505.jpg`
- **Ableton Push 2** → `ableton-push-2.jpg`
- **Looptimus MIDI Pedal** → `looptimus-pedal.jpg`
- **Boss DR-202 Drum Machine** → `boss-dr202.jpg`

### Music & Audio (2 items)
- **Pro-Ject Turntable** → `project-turntable.jpg`
- **Stanton STR8-100 DJ Turntable** → `stanton-turntable.jpg`

### E-Bike Parts (4 items)
- **Ariel Rider 52V Battery - Battery 1** → `ariel-rider-battery.jpg`
- **Ariel Rider 52V Battery - Battery 2** → `ariel-rider-battery.jpg` (shared)
- **Rad Power 48V Battery** → `rad-power-battery.jpg`
- **Grizzly Dual Hub Motors** → `grizzly-hub-motors.jpg`

### Electronics & Tech (2 items)
- **TP-Link Deco Mesh Routers** → `tplink-deco.jpg`
- **LG Dual Inverter Window AC** → `lg-ac-unit.jpg`

### Crafts & Hobbies (1 item)
- **Cricut Maker 3** → `cricut-maker-3.jpg`

### Bikes & Transportation (1 item)
- **Bachetta Giro Recumbent Bike** → `recumbent-bike.jpg`

### Phish Collectibles (2 items)
- **Phish Baker's Dozen Poster** → `phish-bakers-dozen.jpg`
- **Phish Curveball Poster** → `phish-curveball.jpg`

## Technical Details

- **Source**: Lorem Picsum (placeholder service for demonstration)
- **Dimensions**: 400x300px (web-optimized)
- **Format**: JPEG
- **Total images**: 24 unique files (25 items, 2 share same image)
- **Total size**: ~450KB for all images
- **Location**: `/Users/estiens/code/garagesale/friends-sale/static/images/`

## Markdown Front Matter Updates

All item markdown files have been updated with:
```yaml
image: "/images/filename.jpg"
```

This field was added to the front matter of each item file, positioned after `shipping:` and before `short_description:`.

## Next Steps / Recommendations

These are **placeholder stock photos** from Lorem Picsum. For a production garage sale site, you should:

1. **Replace with actual product photos** - Take photos of the real items
2. **Or use actual stock photos** from:
   - Unsplash (free, high-quality)
   - Pexels (free, high-quality)
   - Pixabay (free)
   - Manufacturer websites (for specific products like Sonos, Boss, etc.)

3. **For specific branded items**, consider:
   - Sonos products: Use official Sonos product images
   - Boss music gear: Official Boss/Roland images
   - KitchenAid/Vitamix: Official brand images
   - Generic items: Representative stock photos

## File Naming Convention

Files are named using kebab-case matching the product:
- Product-specific: `sonos-beam-gen2.jpg`, `boss-rc505.jpg`
- Generic: `kitchenaid-mixer.jpg`, `recumbent-bike.jpg`
- Multi-word: `ariel-rider-battery.jpg`, `grizzly-hub-motors.jpg`

All images are ready to display on the website!
