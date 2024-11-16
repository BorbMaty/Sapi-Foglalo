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
        { name: "Villamosmernoki Tanszek", class: "room nonclickable r223" }
    ]],
    [3, [
        { name: "Room 301", class: "room" },
        { name: "Room 302", class: "room" },
        { name: "Library", class: "room library" }
    ]]
]);
function replaceContent(level) {
    const container = document.getElementsByClassName('blueprint')[0];
    container.innerHTML = '';  // Clear existing content

    // Get the rooms for the specified level
    const rooms = levels.get(level);

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
        if (!room.class.includes('nonclickable') && !room.class.includes('leveling-button') && room.name) {
            roomDiv.onclick = () => bookRoom(room.name);
        }
        container.appendChild(roomDiv);
    });
}

function scaleContent() {
    const container = document.querySelector('.shrink');
    const widthScale = window.innerWidth / 1500; // Scale based on width
    const heightScale = window.innerHeight / 700; // Scale based on height (600px is your original height)

    const scale = Math.min(widthScale, heightScale); // Choose the smaller scale to fit within both dimensions
    container.style.transform = `scale(${scale})`;
    container.style.transformOrigin = 'top'; // Keep scaling consistent
}

window.onresize = scaleContent; // Recalculate scale on resize

window.onload = function () {
    scaleContent();
    replaceContent(1);
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

// Function to open the booking modal with the selected room name
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


