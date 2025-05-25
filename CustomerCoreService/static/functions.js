fetch('menu')
        .then(response => response.text())
        .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const targetDiv = doc.getElementById('menu');
        document.getElementById('menu').innerHTML = targetDiv.innerHTML;
        });

fetch('header')
        .then(response => response.text())
        .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const targetDiv = doc.getElementById('header');
        document.getElementById('header').innerHTML = targetDiv.innerHTML;
        });