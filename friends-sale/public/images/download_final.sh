#!/bin/bash

# Download placeholder images using Lorem Picsum which is reliable
download_img() {
    local seed="$1"
    local filename="$2"
    curl -s -L "https://picsum.photos/seed/${seed}/400/300" -o "${filename}"
    echo "Downloaded: ${filename}"
}

# Download all images
download_img "kitchenaid456" "kitchenaid-mixer.jpg"
download_img "ebike789" "ariel-rider-battery.jpg"
download_img "radpower234" "rad-power-battery.jpg"
download_img "bossrc505" "boss-rc505.jpg"
download_img "projecttt567" "project-turntable.jpg"
download_img "tplink890" "tplink-deco.jpg"
download_img "cricut123" "cricut-maker-3.jpg"
download_img "push2abc" "ableton-push-2.jpg"
download_img "vitamix999" "vitamix-blender.jpg"
download_img "lgac777" "lg-ac-unit.jpg"
download_img "beam2xyz" "sonos-beam-gen2.jpg"
download_img "submini111" "sonos-sub-mini.jpg"
download_img "beam1pqr" "sonos-beam-gen1.jpg"
download_img "hubmotor222" "grizzly-hub-motors.jpg"
download_img "looptim333" "looptimus-pedal.jpg"
download_img "dr202abc" "boss-dr202.jpg"
download_img "recumb444" "recumbent-bike.jpg"
download_img "delonghi555" "delonghi-espresso.jpg"
download_img "stanton666" "stanton-turntable.jpg"
download_img "phishdoz777" "phish-bakers-dozen.jpg"
download_img "curveball888" "phish-curveball.jpg"
download_img "soda999" "sodastream.jpg"
download_img "oneslxyz" "sonos-one-sl.jpg"
download_img "fiveabc" "sonos-five.jpg"

echo ""
echo "All images downloaded successfully!"
ls -lh *.jpg | wc -l | xargs echo "Total images:"
