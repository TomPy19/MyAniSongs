"use strict";

import user_data from './lists/parsed_data.json' assert {type: 'json'};

const op_order = [];

for (i = 0; i < Object.keys(user_data).length; i++) {
    op_order[i] = i;
}

const shuffled_ops = op_order.sort((a, b) => 0.5 - Math.random());
var curl = user_data[op_order[0]];

console.log('yippee');

const videoPlayer = document.querySelector('.video-player');
const video = videoPlayer.querySelector('.video');
const nextButton = videoPlayer.querySelector('.next');
const prevButton = videoPlayer.querySelector('.prev');
const animeTitle = document.querySelector('.anime-title');
const songTitle = document.querySelector('.song-title');

setURL(curl);
video.addEventListener('ended', next);
nextButton.addEventListener('click', next);
prevButton.addEventListener('click', prev);

var i = 0;

function next() {
    if (i === shuffled_ops.length - 1) {
        i = 0;
    } else {
        i++;
    }

    curl = user_data[op_order[i]];
    setURL(curl);
}

function prev() {
    if (i === 0) {
        i = shuffled_ops.length - 1;
    } else {
        i--;
    }

    curl = user_data[op_order[i]];
    setURL(curl);
}

function setURL(curl) {
    video.setAttribute("src", curl.hq_link);
    animeTitle.innerHTML = curl.show_title + ' (' + curl.year + ') - Opening ' + curl.sequence;
    songTitle.innerHTML = curl.song_title + ' - ' + curl.artist
}