// Example JavaScript to toggle a class for responsive menu
function toggleMenu() {
    const nav = document.querySelector('nav ul');
    nav.classList.toggle('active');
}

document.addEventListener('DOMContentLoaded', function() {
    const textToType = "I am a Python Backend Developer with experience in developing scalable web applications. My expertise includes working with Django, Flask, and building RESTful APIs. I am passionate about learning new technologies and solving real-world restrictions through code.";
    const typingSpeed = 80;
    const element = document.getElementById('typing-effect');
    let i = 0;

    function typeWriter() {
        if (i < textToType.length) {
            element.innerHTML += textToType.charAt(i);
            i++;
            setTimeout(typeWriter, typingSpeed);
        }
    }

    typeWriter();
});
