$(document).ready(function () {
    $('.arrowToggle').on('click', function() {
        $(".sidebar").toggleClass("showSideBar");
        $(".arrowToggle img").toggleClass("rotateArrow");
    })
})