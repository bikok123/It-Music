$(document).ready(function () {
    $('#remove').on('click', function (e) {
        let playlist_item = $('#delete_id').val();
        e.preventDefault();
        $.ajax({
            url: 'remove_from_playlist',
            data: {
                playlist_item: playlist_item,
            },
            dataType: 'json',
            success: function (response) {
                $('#track').text(response.count);
            }
        });
        $(".item-"+playlist_item).css("display", "none");
    });
});