document.addEventListener('DOMContentLoaded', function() {
    const typewriterElement = document.getElementById('typewriter');
    const text = 'This looks like a type writer';
    typewriterElement.innerHTML = `<span class="typewriter">${text}</span>`;
});
