$(document).ready(() => {
  get_users = () => {
    $.ajax({
      url: 'http://tompy.site/flask/users',
      method: 'GET',
      success: function (data) {
        console.log(data);
      }
    })
  }

  get_user = (user) => {
    $.ajax({
      url: 'http://tompy.site/flask/get/'+user,
      method: 'GET',
      success: function (data) {
        console.log(data);
      }
    })
  }

  // let op_order = [];

  // for (i = 0; i < Object.keys(user_data).length; i++) {
  //   op_order[i] = i;
  // }

  // const shuffled_ops = op_order.sort((a, b) => 0.5 - Math.random());
  // var curl = user_data[op_order[0]];\

  // const videoPlayer = $('.video-player');
  // const video = $('.video');
  // const nextButton = $('.next');
  // const prevButton = $('.prev');
  // const animeTitle = $('.anime-title');
  // const songTitle = $('.song-title');

  // setURL(curl);
  // video.addEventListener('ended', next);
  // nextButton.addEventListener('click', next);
  // prevButton.addEventListener('click', prev);

  // var i = 0;

  // function next() {
  //   if (i === shuffled_ops.length - 1) {
  //     i = 0;
  //   } else {
  //     i++;
  //   }

  //   curl = user_data[op_order[i]];
  //   setURL(curl);
  // }

  // function prev() {
  //   if (i === 0) {
  //     i = shuffled_ops.length - 1;
  //   } else {
  //     i--;
  //   }

  //   curl = user_data[op_order[i]];
  //   setURL(curl);
  // }

  // function setURL(curl) {
  //   video.setAttribute("src", curl.hq_link);
  //   animeTitle.innerHTML = curl.show_title + ' (' + curl.year + ') - Opening ' + curl.sequence;
  //   songTitle.innerHTML = curl.song_title + ' - ' + curl.artist
  // }
});