window.onload = function() {
        load_header();
        load_menu();
    };

function load_header(){
        fetch('header')
                .then(response => response.text())
                .then(html => {
                console.log("Inside load header")
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const targetDiv = doc.getElementById('header');
                document.getElementById('header').innerHTML = targetDiv.innerHTML;
                })
                .catch(error => {console.log("Error loading the header - ", error)});
}

function load_menu(){
        fetch('menu')
                .then(response => response.text())
                .then(html => {
                console.log("Inside load menu")
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const targetDiv = doc.getElementById('menu');
                document.getElementById('menu').innerHTML = targetDiv.innerHTML;
                })
                .catch(error => {console.log("Error loading the menu - ", error)});
}

