import { get_user_list } from './docs/get_user_list'
import { get_show_data } from './docs/get_show_data'
import { parse_data } from './docs/parse_data'

const { spawn } = require('child_process')

const videoPlayer = document.querySelector('.video-player')
const video = videoPlayer.querySelector('.video')
const nextButton = videoPlayer.querySelector('.next')
const prevButton = videoPlayer.querySelector('.prev')
const animeTitle = document.querySelector('.anime-title')
const songTitle = document.querySelector('.song-title')
const tbox = document.querySelector('#user_input')
const input_button = document.querySelector('#input_button')

let op_order = []
let user = ''
let user_data = ''
let curl = ''
let shuffled_ops = []

// setURL(curl);
video.addEventListener('ended', next)
nextButton.addEventListener('click', next)
prevButton.addEventListener('click', prev)
input_button.addEventListener('click', setUser)

var i = 0;

function next() {
    if (i === shuffled_ops.length - 1) {
        i = 0
    } else {
        i++
    }

    curl = user_data[op_order[i]]
        // setURL(curl)
    console.log('Next')
}

function prev() {
    if (i === 0) {
        i = shuffled_ops.length - 1
    } else {
        i--
    }

    curl = user_data[op_order[i]]
        // setURL(curl)
    console.log('Prev')
}

function setURL(curl) {
    video.setAttribute("src", curl.hq_link)
    animeTitle.innerHTML = curl.show_title + ' (' + curl.year + ') - Opening ' + curl.sequence
    songTitle.innerHTML = curl.song_title + ' - ' + curl.artist
}

function setUser() {
    user = tbox.value
        // const childPython = spawn('python', ['docs/test.py'])
        // childPython.stdout.on('data', (data) => {
        //     console.log(`stdout: ${data}`)
        // })
    user_data = get_data_from_mal(user)
    console.log(user)

    for (i = 0; i < Object.keys(user_data).length; i++) {
        op_order[i] = i
    }
    shuffled_ops = op_order.sort((a, b) => 0.5 - Math.random())
    curl = user_data[op_order[0]]
    setURL(curl)
}

function get_data_from_mal(user) {
    let data = localStorage.getItem(user)

    if (data) {
        return data
    } else {
        const access_token = '32ef86fd993671eb0a7281d3031f0be4'

        const url = 'https://jigsaw.w3.org/css-validator/validator' +
            'https://api.myanimelist.net/v2/users/' + user + '/animelist'
        const user_list = get_user_list(access_token, url, {}, 0)
        const show_data = get_show_data(user_list)
        const parsed_data = parse_data(show_data)

        localStorage.setItem(user, parsed_data)
        return localStorage.getItem(user)
    }
}