$(document).ready(function() {
    const cameras = [
        {
            id: 1,
            lugar: "AMBIENTE A201",
            ip_cam: "192.168.1.1",
            sector: 1,
            puerto: 8080,
            usuario: "cam-agv",
            contraseña: "1221"
        },
        {
            id: 2,
            lugar: "AMBIENTE B202",
            ip_cam: "192.168.1.2",
            sector: 2,
            puerto: 8081,
            usuario: "cam-bhv",
            contraseña: "2233"
        },
        {
            id: 3,
            lugar: "AMBIENTE C303",
            ip_cam: "192.168.1.3",
            sector: 3,
            puerto: 8082,
            usuario: "cam-ciw",
            contraseña: "3344"
        },
        {
            id: 4,
            lugar: "AMBIENTE D404",
            ip_cam: "192.168.1.4",
            sector: 4,
            puerto: 8083,
            usuario: "cam-djx",
            contraseña: "4455"
        },
        {
            id: 5,
            lugar: "AMBIENTE E505",
            ip_cam: "192.168.1.5",
            sector: 5,
            puerto: 8084,
            usuario: "cam-eky",
            contraseña: "5566"
        },
        {
            id: 6,
            lugar: "AMBIENTE F606",
            ip_cam: "192.168.1.6",
            sector: 6,
            puerto: 8085,
            usuario: "cam-flz",
            contraseña: "6677"
        },
        {
            id: 7,
            lugar: "AMBIENTE G707",
            ip_cam: "192.168.1.7",
            sector: 7,
            puerto: 8086,
            usuario: "cam-gma",
            contraseña: "7788"
        },
        {
            id: 8,
            lugar: "AMBIENTE H808",
            ip_cam: "192.168.1.8",
            sector: 8,
            puerto: 8087,
            usuario: "cam-hnb",
            contraseña: "8899"
        },
        {
            id: 9,
            lugar: "AMBIENTE I909",
            ip_cam: "192.168.1.9",
            sector: 9,
            puerto: 8088,
            usuario: "cam-ico",
            contraseña: "9900"
        },
        {
            id: 10,
            lugar: "AMBIENTE J010",
            ip_cam: "192.168.1.10",
            sector: 10,
            puerto: 8089,
            usuario: "cam-jpd",
            contraseña: "1010"
        }
    ];

    // Función para mostrar los datos de las cámaras
    function displayCameras(cameras) {
        const $container = $('#cameras');

        cameras.forEach(camera => {
            const cameraDiv = document.createElement("a");
            cameraDiv.classList.add("cam");
            cameraDiv.setAttribute('href', `/cameras/${camera.id}/`);

            const infoCam = document.createElement("footer");
            const lugarCam = document.createElement("span");
            lugarCam.textContent = camera.lugar;

            const eyeIcon = document.createElement("img");
            eyeIcon.setAttribute('src', '/static/images/icons/eye-line.svg');

            infoCam.append(lugarCam);
            infoCam.append(eyeIcon);
            cameraDiv.append(infoCam);

            $container.append(cameraDiv);
        });
    }

    // Llama a la función para mostrar las cámaras
    displayCameras(cameras);
});
