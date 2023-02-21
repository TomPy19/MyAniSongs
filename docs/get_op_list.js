function get_op_list(show_data) {
    var op_list = {};

    for (var i = 0; i < show_data.length; i++) {
        op_list[i] = {
            "name": show_data[i]["anime"]["title"]
        };
    }
}

export { get_op_list }