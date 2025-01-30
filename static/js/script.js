async function fetchUnidades() {
    try {
        const response = await fetch('/unidades');
        const data = await response.json();
        document.getElementById('unidades-list').innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error('Error:', error);
    }
}

async function fetchUbicaciones() {
    const unidadId = document.getElementById('unidad-id').value;
    try {
        const response = await fetch(`/unidades/${unidadId}/ubicaciones`);
        const data = await response.json();
        document.getElementById('ubicaciones-list').innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error('Error:', error);
    }
}

async function fetchAlcaldias() {
    try {
        const response = await fetch('/alcaldias');
        const data = await response.json();
        document.getElementById('alcaldias-list').innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error('Error:', error);
    }
}

async function fetchParadas() {
    const alcaldiaNombre = document.getElementById('alcaldia-nombre').value;
    try {
        const response = await fetch(`/alcaldias/${alcaldiaNombre}/paradas`);
        const data = await response.json();
        document.getElementById('paradas-list').innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error('Error:', error);
    }
}