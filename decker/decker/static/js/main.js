$(document).ready(function() {
    $('form').on('submit', function(event) {
        event.preventDefault();
        var brand = $('#brand').val();
        $.ajax({
            type: 'POST',
            url: '/',
            data: {brand: brand},
            success: function(response) {
                window.location.href = '/success';
            }
        });
    });
});