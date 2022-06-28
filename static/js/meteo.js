function get_meteo(s, id) {
    var js, fjs = document.getElementsByTagName(s)[0];
    if (!document.getElementById(id)) {
        js = document.createElement(s);
        js.id = id;
        js.src = 'https://weatherwidget.io/js/widget.min.js';
        fjs.parentNode.insertBefore(js, fjs);
        setTimeout(30100)
    }

}
get_meteo('script', 'weatherwidget-io-js');
