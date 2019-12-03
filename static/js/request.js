$(document).ready(function () {
    $('.request-form').on('submit', function (e) {
        var name = $('#name').val();
        var telephone = $('#telephone').val();
        var email = $('#email').val();
        var comment = $('#comment').val();
        e.preventDefault();
        $.ajax({
            url: '/enroll/',
            data: {
                name: name,
                telephone: telephone,
                email: email,
                comment: comment,
            },
            dataType: 'json',
            success: function () {
                $('#name').val('');
                $('#email').val('');
                $('#comment').val('');
                $('#telephone').val('');
                $('.modal').modal('toggle');
                $("#course-alert").fadeTo(4000, 800).slideUp(700, function() {
                    $("#success-alert").slideUp(600);
                });
            }
        });
    });
});