// Room data for each floor
const floors = {
    1: [
        { id: "128", name: "128", x: 500, y: 50 },
        { id: "129", name: "129", x: 425, y: 50 },
        { id: "130", name: "130", x: 350, y: 50 },
        { id: "131", name: "131", x: 275, y: 50 },
        { id: "132", name: "132", x: 200, y: 50 },
        { id: "133", name: "133", x: 125, y: 50 },
        { id: "134", name: "134", x: 50, y: 50 },
        { id: "114", name: "114", x: 800, y: 200 },
    ],
    2: [
        { id: "201", name: "201", x: 50, y: 50 },
        { id: "202", name: "202", x: 125, y: 50 },
        { id: "203", name: "203", x: 200, y: 50 }
    ],
    // Add similar room data for other floors...
};

function showFloor(level) {
    const container = document.getElementById('floor-container');
    
    // Set the background image for the selected floor
    container.style.backgroundImage = `url('../images/floor${level}.png')`;
    container.style.backgroundSize = "cover"; // Makes the image cover the container
    container.style.backgroundPosition = "center"; // Centers the image
    
    // Clear previous room layout
    container.innerHTML = '';  

    // Add room elements for the selected floor
    const floorRooms = floors[level];
    floorRooms.forEach(room => {
        const roomDiv = document.createElement('div');
        roomDiv.classList.add('room');
        roomDiv.innerHTML = room.name;
        roomDiv.style.left = `${room.x}px`;
        roomDiv.style.top = `${room.y}px`;
        roomDiv.onclick = () => bookRoom(room.id);

        container.appendChild(roomDiv);
    });
}


function bookRoom(roomId) {
    alert(`Booking Room ${roomId}`);
}
