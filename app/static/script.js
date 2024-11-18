const levels = new Map([
    [1, [
        { name: "133", class: "room r133"},
        { name: "132", class: "room r132"},
        { name: "131", class: "room r131"},
        { name: "130", class: "room r130"},
        { name: "129", class: "room r129"},
        { name: "128", class: "room r128"},
        { name: "Gepeszmernoki Tanszek", class: "room nonclickable r127" },
        { name: "Aula", class: "room nonclickable aula" },
        { name: "114", class: "room r114"},
        { name: "Porta", class: "room nonclickable porta" },
        { name: "Bufe", class: "room nonclickable bufe" },
        { name: "111", class: "room r111"},
        { name: "112", class: "room r112"},
        { name: "113", class: "room r113"}
    ]],
    [2, [
        { name: "217", class: "room r217"},
        { name: "216", class: "room r216"},
        { name: "213", class: "room r213"},
        { name: "212", class: "room r212"},
        { name: "209", class: "room r209"},
        { name: "208", class: "room r208"},
        { name: "207", class: "room r207"},
        { name: "Villamosmernoki Tanszek", class: "room nonclickable r223" },
        { name: "Aula", class: "room nonclickable aula" },
        { name: "230", class: "room r230"},
        { name: "231", class: "room r231"},
        { name: "232", class: "room nonclickable r232"},
        { name: "240", class: "room nonclickable r240"},
        { name: "241", class: "room r241"},
        { name: "242", class: "room r242"},
        { name: "243", class: "room r243"}
    ]],
    [3, [
        // { name: "Room 301", class: "room" },
        // { name: "Room 302", class: "room" },
        // { name: "Library", class: "room library" }
    ]],
    [4, [
        { name: "414", class: "room r414" },
        { name: "415", class: "room r415" },
        { name: "416", class: "room r416" },
        { name: "417", class: "room r417" },
        { name: "418", class: "room r418" },
        { name: "412", class: "room nonclickable r412" },
        { name: "413", class: "room nonclickable r413" },
        { name: "411", class: "room r411" }
    ]]
]);
function replaceContent(level) {
    const container = document.getElementsByClassName('blueprint')[0];
    container.innerHTML = '';  // Clear existing content

    const rooms = levels.get(level); // Get the rooms for the specified level

    // Check if rooms exist for the given level
    if (!rooms) {
        console.error(`Level ${level} does not exist.`);
        return;
    }

    // Create and append each room div to the container
    rooms.forEach(room => {
        const roomDiv = document.createElement('div');
        roomDiv.className = room.class;
        roomDiv.textContent = room.name;

         // Attach onclick only if the room is clickable
        if (!room.class.includes('nonclickable') && room.name) {
            roomDiv.onclick = () => bookRoom(room.name);
        }
        container.appendChild(roomDiv);
    });
}

function scaleContent() {
    const container = document.querySelector('.shrink');
    const widthScale = window.innerWidth / 1500;
    const heightScale = window.innerHeight / 700;

    const scale = Math.min(widthScale, heightScale); // Choose the smaller scale to fit within both dimensions
    container.style.transform = `scale(${scale})`;
    container.style.transformOrigin = 'top'; // Keep scaling consistent
}

window.onresize = scaleContent; // Recalculate scale on resize

window.onload = function () {
    scaleContent();
    replaceContent(1); // Loading the first floor on opening the site
};

let currentLevel = 1; // Start at level 1
const maxLevel = 4; // Maximum level
const minLevel = 1; // Minimum level

function increaseLevel() {
    if (currentLevel < maxLevel) {
        currentLevel++;
        replaceContent(currentLevel);
    }
}

function decreaseLevel() {
    if (currentLevel > minLevel) {
        currentLevel--;
        replaceContent(currentLevel);
    }
}

const button_up = document.getElementsByClassName('leveling-up')[0];
const button_down = document.getElementsByClassName('leveling-down')[0];

document.addEventListener('keydown', (event) => {
    if (event.key === '+' && !event.shiftKey && !event.ctrlKey && !event.altKey) {
        button_up.click();
    }
});

document.addEventListener('keydown', (event) => {
    if (event.key === '-' && !event.shiftKey && !event.ctrlKey && !event.altKey) {
        button_down.click();
    }
});

function bookRoom(room) {
    // Ensure the room name is displayed in the appropriate element
    const roomNameElement = document.getElementById('roomName');
    if (roomNameElement) {
        roomNameElement.textContent = room;
    } else {
        console.error('Element with ID "roomName" not found.');
    }

    // Ensure the booking modal exists and is displayed correctly
    const bookingModal = document.getElementById('bookingModal');
    if (bookingModal) {
        bookingModal.style.display = 'flex';  // Show the modal
    } else {
        console.error('Element with ID "bookingModal" not found.');
    }
}

// Function to close the modal
function closeModal() {
    document.getElementById('bookingModal').style.display = 'none';
}

// Function to simulate booking submission
function submitBooking() {
    const name = document.getElementById('name').value;
    const date = document.getElementById('date').value;
    const start_hour = document.getElementById('start_hour').value;
    const end_hour = document.getElementById('end_hour').value;
    const room = document.getElementById('roomName').textContent;
    
    if (name && date) {
        alert(`Room "${room}" booked successfully by ${name} on ${date} from ${start_hour} to ${end_hour}!`);
        closeModal();
    } else {
        alert("Please fill in all the details.");
    }
}


