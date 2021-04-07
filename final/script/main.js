document.addEventListener('DOMContentLoaded', (event) => {
    var image = document.getElementById("dm-btn");

    image.onclick = function(e) {
        document.body.classList.toggle('dark-mode');
    }
})
