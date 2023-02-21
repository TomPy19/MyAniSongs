function get_user_list(access_token, url, result, it) {
  const options = {
    headers: {'X-MAL-CLIENT-ID': access_token},
  }

  let next_url;
  
  requestMal()

  // let list
  async function requestMal() {
    const list = await fetch(url, options).then((res) => res.json())

    try {
      const data = list['data']
      for (var i = 0; i < data.length; i++) {
        result[i + (it * 10)] = { 'id': data[i]['node']['id'], 'title': data[i]['node']['title'] };
      }
    } catch {
      result = result;
    }

    try {
      next_url = list['paging']['next'];
    } catch {
      next_url = 0;
    }

    if (next_url) {
      it++;
      get_user_list(access_token, next_url, result, it);
    }

    return result;
  }
  
}

export { get_user_list }