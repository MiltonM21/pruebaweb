

function identifyRace() {
    const selectedImage = localStorage.getItem('selectedImage');
    if (selectedImage) {
        // Aquí deberías implementar la lógica para identificar la raza
        // Puedes utilizar bibliotecas de aprendizaje automático como TensorFlow.js o enviar la imagen a un 
        //servicio de identificación de razas de perros en línea mediante una solicitud HTTP
        // Por ahora, simplemente agregaremos un texto de ejemplo debajo de la imagen
        const raceIdentifier = document.getElementById('raceIdentifier');
        raceIdentifier.innerText = 'Raza identificada: Labrador Retriever';

        // Puedes agregar aquí la lógica para guardar la imagen en el servidor si es necesario
    } else {
        alert('Primero selecciona una imagen.');
    }
}




const toggleModeBtn = document.getElementById("toggleModeBtn");

function applyMode(mode) {
    document.body.classList.remove("light-mode", "dark-mode");
    document.body.classList.add(mode);
}

function cambiarModo() {
    var body = document.body;
    if (body.classList.contains("dark-mode")) {
        body.classList.remove("dark-mode");
        body.classList.add("light-mode");
        localStorage.setItem("modo", "light");
    } else {
        body.classList.remove("light-mode");
        body.classList.add("dark-mode");
        localStorage.setItem("modo", "dark");
    }
}

function toggleMode() {
    const isDarkMode = document.body.classList.contains("dark-mode");
    const newMode = isDarkMode ? "light-mode" : "dark-mode";

    localStorage.setItem("mode", newMode);

    applyMode(newMode);

    // Cambiar la imagen del botón después de cambiar el modo
    if (newMode === "dark-mode") {
        document.getElementById("modoIcono").src = "./static/boton_sol.png"; // Ruta a la imagen de botón de modo oscuro
    } else {
        document.getElementById("modoIcono").src = "./static/boton_luna.png"; // Ruta a la imagen de botón de modo claro
    }

    // Cambiar el estilo de los botones según el modo
    cambiarEstiloBotonesInicio(newMode);
}

toggleModeBtn.addEventListener("click", toggleMode);

// Recuperar el estado del modo al cargar la página
const savedMode = localStorage.getItem("mode");
if (savedMode) {
    applyMode(savedMode);

    // Actualizar la imagen del botón según el estado del modo
    if (savedMode === "dark-mode") {
        document.getElementById("modoIcono").src = "./static/boton_sol.png"; // Ruta a la imagen de botón de modo oscuro
    } else {
        document.getElementById("modoIcono").src = "./static/boton_luna.png"; // Ruta a la imagen de botón de modo claro
    }
}


// Función para cambiar los estilos de los botones según el modo en la página de inicio
function cambiarEstiloBotonesInicio() {
    const irAConfiguracionesBtn = document.getElementById("irAConfiguracionesBtn");
    const cerrarSesionBtn = document.getElementById("cerrarSesionBtn");
    const toggleModeBtn = document.getElementById("toggleModeBtn");
    const identifyButton = document.getElementById("identifyButton");
    const fileInput = document.getElementById("fileInput");
    const savedMode = localStorage.getItem("mode");

    if (savedMode === "dark-mode") {
        // Si el modo guardado es oscuro, aplica la clase 'btn-dark' a los botones
        irAConfiguracionesBtn.classList.remove("btn-light");
        irAConfiguracionesBtn.classList.add("btn-dark");
        cerrarSesionBtn.classList.remove("btn-light");
        cerrarSesionBtn.classList.add("btn-dark");
        toggleModeBtn.classList.remove("btn-light");
        toggleModeBtn.classList.add("btn-dark");
        identifyButton.classList.remove("btn-light");
        identifyButton.classList.add("btn-dark");
        fileInput.classList.remove("btn-light");
        fileInput.classList.add("btn-dark");
    } else {
        // Si el modo guardado es claro o no está definido, aplica la clase 'btn-light' a los botones
        irAConfiguracionesBtn.classList.remove("btn-dark");
        irAConfiguracionesBtn.classList.add("btn-light");
        cerrarSesionBtn.classList.remove("btn-dark");
        cerrarSesionBtn.classList.add("btn-light");
        toggleModeBtn.classList.remove("btn-dark");
        toggleModeBtn.classList.add("btn-light");
        identifyButton.classList.remove("btn-dark");
        identifyButton.classList.add("btn-light");
        fileInput.classList.remove("btn-dark");
        fileInput.classList.add("btn-light");
    }
}


// Llamar a cambiarEstiloBotones al cargar la página
window.addEventListener("load", cambiarEstiloBotonesInicio);
