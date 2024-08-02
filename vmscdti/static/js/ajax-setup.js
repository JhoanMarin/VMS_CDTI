// ajax_setup.js
$(document).ready(function() {
    // Función para obtener la cookie CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Obtener el token CSRF
    const csrfToken = getCookie('csrftoken');

    // Configurar todas las solicitudes AJAX para incluir el token CSRF
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Solo añade el token CSRF si la URL no es externa
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            }
        }
    });
});
