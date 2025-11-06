#!/bin/bash

# Function to download and optimize image from Unsplash
download_image() {
    local query="$1"
    local filename="$2"
    local width=400
    
    # Unsplash Source API - provides random images based on search term
    # Using 800px width to ensure quality, will resize to 400px max-width
    curl -L "https://source.unsplash.com/800x600/?${query}" -o "${filename}" 2>/dev/null
    
    if [ -f "${filename}" ]; then
        # Use sips (macOS built-in) to resize if needed
        sips -Z 400 "${filename}" >/dev/null 2>&1
        echo "Downloaded: ${filename}"
    else
        echo "Failed: ${filename}"
    fi
}

# Download images for each item
download_image "kitchenaid,stand,mixer,professional" "kitchenaid-mixer.jpg"
download_image "ebike,battery,52v" "ariel-rider-battery.jpg"
download_image "ebike,battery,48v,rad" "rad-power-battery.jpg"
download_image "boss,rc505,loop,station" "boss-rc505.jpg"
download_image "project,turntable,vinyl" "project-turntable.jpg"
download_image "tplink,deco,mesh,wifi,router" "tplink-deco.jpg"
download_image "cricut,maker,cutting,machine" "cricut-maker-3.jpg"
download_image "ableton,push,midi,controller" "ableton-push-2.jpg"
download_image "vitamix,blender,professional" "vitamix-blender.jpg"
download_image "lg,window,air,conditioner" "lg-ac-unit.jpg"
download_image "sonos,beam,soundbar,black" "sonos-beam-gen2.jpg"
download_image "sonos,sub,mini,subwoofer" "sonos-sub-mini.jpg"
download_image "sonos,beam,soundbar,white" "sonos-beam-gen1.jpg"
download_image "ebike,hub,motor,wheel" "grizzly-hub-motors.jpg"
download_image "looptimus,midi,foot,pedal" "looptimus-pedal.jpg"
download_image "boss,dr202,drum,machine" "boss-dr202.jpg"
download_image "recumbent,bike,bachetta" "recumbent-bike.jpg"
download_image "delonghi,espresso,machine" "delonghi-espresso.jpg"
download_image "stanton,turntable,dj,str8" "stanton-turntable.jpg"
download_image "phish,poster,concert,donut" "phish-bakers-dozen.jpg"
download_image "phish,poster,concert,festival" "phish-curveball.jpg"
download_image "sodastream,sparkling,water" "sodastream.jpg"
download_image "sonos,one,speaker,compact" "sonos-one-sl.jpg"
download_image "sonos,five,speaker,premium" "sonos-five.jpg"

echo "All downloads complete!"
