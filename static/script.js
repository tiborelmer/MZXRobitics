document.addEventListener("DOMContentLoaded", function () {
    let images = document.querySelectorAll(".slideshow img");
    let currentIndex = 0;

    function showNextImage() {
        images[currentIndex].style.opacity = 0;
        currentIndex = (currentIndex + 1) % images.length;
        images[currentIndex].style.opacity = 1;
    }

    images[currentIndex].style.opacity = 1;
    setInterval(showNextImage, 4000); // Change d'image toutes les 4 secondes
});

document.getElementById("languageSelect").addEventListener("change", function() {
    const selectedLanguage = this.value;
    alert("Language changed to: " + selectedLanguage);
    // Ici, tu peux rediriger vers une page ou recharger avec la langue sélectionnée
});

document.addEventListener("DOMContentLoaded", function () {
    const track = document.querySelector(".image-track");
    const images = track.innerHTML; // Sauvegarde les images actuelles
    track.innerHTML += images; // Duplique les images pour un effet continu
});




