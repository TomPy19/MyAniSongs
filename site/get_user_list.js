function get_user_list(access_token, url, result, it) {
  params = {
    headers: {'X-MAL-CLIENT-ID': access_token},
    method: 'GET'
  };

  response = fetch(url, params);

  const list = response.body.json();

  try {
    const data = list['data']
    for (var i = 0; i < data.length; i++) {
      result[i+(it*10)] = {'id': data[i]['node']['id'], 'title': data[i]['node']['title']};
    }
  } catch {
    result = result;
  }

  try {
    const next_url = list['paging']['next'];
  } catch {
    const next_url = 0;
  }

  if (next_url) {
    it++;
    get_user_list(access_token, next_url, result, it);
  }

  return result;
}