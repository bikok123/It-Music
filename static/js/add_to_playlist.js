$(document).ready(function () {
    $('.plus').on('click', function (e) {
        let id = $(this).attr('id');
        // Prevent page refresh
        e.preventDefault();
        console.log("123");
        $.ajax({
            url: 'add_to_playlist',
            data: {
                id: id,
            },
            dataType: 'json',
            success: function (response) {
                $('#i-'+id).removeClass("fa-plus");
                $('#i-'+id).addClass("fa-check");
            }
        });
    });
});