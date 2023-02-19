function hq(videos) {
    let h_res = 0;
    let hq;

    for (let i = 0; i < videos.length; i++) {
        if (videos[i]['resolution'] > h_res) {
            h_res = videos[i]['resolution']
            hq = videos[i]['link']
        }
    }

    return hq;
}

function format_data(current_show, theme) {
    let artist = 'Unknown';
    let sequence = 1;

    if (theme['song']['artists'] < 0) {
        artist = theme['song']['artists'][0]['name'];
    }
    if (theme[sequence]) {
        sequence = theme['sequence'];
    }

    return {
        'show_title': current_show['name'],
        'year': current_show['year'],
        'song_title': theme['song']['title'],
        'artist': artist,
        'sequence': sequence,
        'hq_link': hq(theme['animethemeentries'][0]['videos'])
    };
}

function parse_data(data) {
    let parsed_data = {};
    let k = 0;

    for (i; i < data.length; i++) {
        let seq = [];
        const current_show = data[i]['anime]'][0];
        if (theme['type'] === 'OP') {
            if (theme[sequence] === 'null') {
                parsed_data[k] = format_data(current_show, theme);
                k++;
            } else {
                if (!seq.includes(theme['sequence'])) {
                    seq.push(theme['sequence']);
                    parsed_data[k] = format_data(current_show, theme);
                    k++;
                }
            }
        }
    }


}