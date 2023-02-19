function get_show_data(user_list) {
  var shows = {};
  var i = 0;

  for (i; i < user_list.length; i++) {
    const show_data = query_name(user_list[i]['title'], user_list[i]['id']);
    if (show_data) {
      shows[i] = show_data['search'];
      console.log(show_data['search']['anime'][0]['name']);
      i++;
    }
  }

  return shows;
}

function query_name(name, id) {
  const url = 'https://api.animethemes.moe/search'

  const params = {
    'q': [
      name
    ],

    'page[limit]': [
      1
    ],

    'include[anime]': [
      'animethemes.song.artists',
      'animethemes.animethemeentries.videos',
      'resources'
    ],

    'fields[search]': [
      'anime'
    ],

    'fields[anime]': [
      'year',
      'name'
    ],

    'fields[song]': [
      'title'
    ],

    'fields[artist]': [
      'name'
    ],

    'fields[video]': [
      'resolution',
      'link'
    ],

    'fields[animethemeentry': [
      'id'
    ],

    'fields[resource]': [
      'external_id',
      'site'
    ]
  }

  const options = {
    method: 'GET',

  }

  const show_data = fetch(url + '?' + new URLSearchParams(params)).json();

  if (show_data['search']['anime'][0]['resources'][0]['site'] === 'MyAnimeList') {
    const mal_id = show_data['search']['anime'][0]['resources'][0]['external_id'];
  } else {
    const mal_id = 0;
  }

  if (mal_id === id) return show_data;

  return;
}