$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    const val = data['hello'];

    $('DIV#hello').text(val);
})
