$(document).ready(function () {
    $('.form-class').on('submit', function (e) {
        var name = $('#contactName').val();
        var email = $('#contactEmail').val();
        var question = $('#contactQuestion').val();
        e.preventDefault();
        $.ajax({
            url: '/ask/',
            data: {
                name: name,
                email: email,
                question: question,
            },
            dataType: 'json',
            success: function () {
                $('#contactName').val('');
                $('#contactEmail').val('');
                $('#contactQuestion').val('');
                $("#success-alert").fadeTo(4000, 800).slideUp(700, function() {
                    $("#success-alert").slideUp(600);
                });
            }
        });
    });
});