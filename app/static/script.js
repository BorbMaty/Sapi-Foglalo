const API_BASE_URL = "http://127.0.0.1:8000";

const levels = new Map([
    [1, [
        { id: 133, name: "133", class: "room r133", isClickable: true },
        { id: 132, name: "132", class: "room r132" },
        { id: 131, name: "131", class: "room r131" },
        { id: 130, name: "130", class: "room r130" },
        { id: 129, name: "129", class: "room r129" },
        { id: 128, name: "128", class: "room r128" },
        { id: 127, name: "Gepeszmernoki Tanszek", class: "room nonclickable r127" },
        { id: 1, name: "Aula", class: "room nonclickable aula" },
        { id: 114, name: "114", class: "room r114" },
        { id: 109, name: "Porta", class: "room nonclickable porta" },
        { id: 134, name: "Bufe", class: "room nonclickable bufe" },
        { id: 111, name: "111", class: "room r111" },
        { id: 112, name: "112", class: "room r112" },
        { id: 113, name: "113", class: "room r113" }
    ]],
    [2, [
        { id: 217, name: "217", class: "room r217" },
        { id: 216, name: "216", class: "room r216" },
        { id: 213, name: "213", class: "room r213" },
        { id: 212, name: "212", class: "room r212" },
        { id: 209, name: "209", class: "room r209" },
        { id: 208, name: "208", class: "room r208" },
        { id: 207, name: "207", class: "room r207" },
        { id: 223, name: "Villamosmernoki Tanszek", class: "room nonclickable r223" },
        { id: 1, name: "Aula", class: "room nonclickable aula" },
        { id: 230, name: "230", class: "room r230" },
        { id: 231, name: "231", class: "room r231" },
        { id: 232, name: "232", class: "room nonclickable r232" },
        { id: 240, name: "240", class: "room nonclickable r240" },
        { id: 241, name: "241", class: "room r241" },
        { id: 242, name: "242", class: "room r242" },
        { id: 243, name: "243", class: "room r243" }
    ]],
    [3, [
        { id: 301, name: "Room 301", class: "room r301" },
        { id: 302, name: "Room 302", class: "room r302" },
        { id: 303, name: "Library", class: "room library" }
    ]],
    [4, [
        { id: 414, name: "414", class: "room r414" },
        { id: 415, name: "415", class: "room r415" },
        { id: 416, name: "416", class: "room r416" },
        { id: 417, name: "417", class: "room r417" },
        { id: 418, name: "418", class: "room r418" },
        { id: 412, name: "412", class: "room nonclickable r412" },
        { id: 413, name: "413", class: "room nonclickable r413" },
        { id: 411, name: "411", class: "room r411" }
    ]]
]);


let currentLevel = 1;
const maxLevel = 4;
const minLevel = 1;

// Function to replace content for the selected level
async function replaceContent(level) {
    const container = document.querySelector('.blueprint');
    container.innerHTML = ''; // Clear existing content

    const rooms = levels.get(level);
    if (!rooms) {
        console.error(`Level ${level} does not exist.`);
        return;
    }

   try {
        const response = await fetch(`${API_BASE_URL}/rooms`);
        if (!response.ok) throw new Error("Failed to fetch rooms.");
        const dbRooms = await response.json();

        // Create and append each room div
        rooms.forEach(room => {
            const roomDiv = document.createElement('div');
            roomDiv.className = room.class;
            roomDiv.textContent = room.name;

           // const isAvailable = dbRooms.some(dbRoom => dbRoom.id === room.id);
            if (!room.class.includes('nonclickable')) {
                roomDiv.onclick = () => openBookingModal(room.id);
            }

            container.appendChild(roomDiv);
        });
    } catch (err) {
        console.error("Error fetching rooms:", err);
    }
}

// Function to open the booking modal
function openBookingModal(roomId) {
    document.getElementById('roomName').textContent = `${roomId}`;
    document.getElementById('bookingModal').style.display = 'flex';
    document.getElementById('bookingForm').dataset.roomId = roomId; // Store the room ID in the form
}
function query(){
    document.getElementById('query').style.display = 'flex';
}

// Function to close the modal
function closeModal() {
    document.getElementById('bookingModal').style.display = 'none';
}

// Function to submit booking
async function submitBooking() {
    const roomId = document.getElementById('bookingForm').dataset.roomId;
    const name = document.getElementById('name').value;
    const date = document.getElementById('date').value;
    const startHour = document.getElementById('start_hour').value;
    const endHour = document.getElementById('end_hour').value;

    const bookingData = {
        user_id: 1, // Replace with dynamic user ID if available
        room_id: parseInt(roomId),
        date: date,
        start_hour: startHour,
        end_hour: endHour
    };

    try {
        const response = await fetch(`${API_BASE_URL}/reserves`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(bookingData)
        });

        if (response.ok) {
            alert("Booking successful!");
        } else {
            const error = await response.json();
            alert(`Failed to book room: ${error.detail}`);
        }
    } catch (err) {
        console.error("Error submitting booking:", err);
        alert("An error occurred. Please try again.");
    } finally {
        closeModal();
    }
}

// Level navigation functions
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

// Page scaling
function scaleContent() {
    const container = document.querySelector('.shrink');
    const widthScale = window.innerWidth / 1500;
    const heightScale = window.innerHeight / 700;
    const scale = Math.min(widthScale, heightScale);
    container.style.transform = `scale(${scale})`;
    container.style.transformOrigin = 'top';
}

window.onresize = scaleContent;

// Initialize the page
window.onload = function () {
    scaleContent();
    replaceContent(currentLevel); // Load the first level
};

document.addEventListener('keydown', (event) => {
    if (event.key === '+' && !event.shiftKey && !event.ctrlKey && !event.altKey) {
        increaseLevel();
    }
    if (event.key === '-' && !event.shiftKey && !event.ctrlKey && !event.altKey) {
        decreaseLevel();
    }
});

const inputField = document.getElementById('date');

function onInputChange(event) {
    const reservationDate = event.target.value; // Selected date
    const roomId = document.getElementById('bookingForm').dataset.roomId; // Selected room ID

    if (reservationDate && roomId) {
        query(); // Display the query modal
        populateBookings(roomId, reservationDate); // Fetch and display reservations
    }
}

document.getElementById('date').addEventListener('input', onInputChange);

// // Attach the 'input' event listener to the input field
// inputField.addEventListener('input', onInputChange);

const bookings = {
    foglalt: [
        { start_hour: "10:00 AM", end_hour: "11:00 AM" },
        { start_hour: "11:30 AM", end_hour: "12:30 PM" },
        { start_hour: "1:00 PM", end_hour: "2:00 PM" },
    ],
    szabad: [
        { start_hour: "2:30 PM", end_hour: "3:30 PM" },
        { start_hour: "4:00 PM", end_hour: "5:00 PM" },
        { start_hour: "5:30 PM", end_hour: "6:30 PM" },
    ],
};

async function populateBookings(roomId, reservationDate) {
    const foglaltContainer = document.querySelector(".foglalt");
    const szabadContainer = document.querySelector(".szabad");
    foglaltContainer.innerHTML = ""; // Clear previous data
    szabadContainer.innerHTML = ""; // Clear previous data

    try {
        const response = await fetch(`${API_BASE_URL}/reservations/${roomId}/${reservationDate}`);
        if (!response.ok) throw new Error("Failed to fetch reservations");

        const reservations = await response.json();

        // Populate occupied (foglalt) slots
        reservations.forEach(reservation => {
            const bookingDiv = document.createElement("div");
            bookingDiv.classList.add("booking");

            const startTime = document.createElement("p");
            startTime.innerHTML = `<strong>Start:</strong> ${reservation.start_hour}`;
            bookingDiv.appendChild(startTime);

            const endTime = document.createElement("p");
            endTime.innerHTML = `<strong>End:</strong> ${reservation.end_hour}`;
            bookingDiv.appendChild(endTime);

            foglaltContainer.appendChild(bookingDiv);
        });

        // Logic to calculate and display available slots (szabad)
        const occupiedIntervals = reservations.map(reservation => ({
            start: new Date(`1970-01-01T${reservation.start_hour}`),
            end: new Date(`1970-01-01T${reservation.end_hour}`)
        }));

        const allDay = [
            { start: new Date("1970-01-01T08:00"), end: new Date("1970-01-01T20:00") }
        ];

        const availableIntervals = allDay.flatMap(({ start, end }) => {
            let freeSlots = [];
            let currentStart = start;

            for (const interval of occupiedIntervals) {
                if (currentStart < interval.start) {
                    freeSlots.push({ start: currentStart, end: interval.start });
                }
                currentStart = interval.end > currentStart ? interval.end : currentStart;
            }

            if (currentStart < end) {
                freeSlots.push({ start: currentStart, end });
            }
            return freeSlots;
        });

        availableIntervals.forEach(interval => {
            const bookingDiv = document.createElement("div");
            bookingDiv.classList.add("booking");

            const startTime = document.createElement("p");
            startTime.innerHTML = `<strong>Start:</strong> ${interval.start.toTimeString().slice(0, 5)}`;
            bookingDiv.appendChild(startTime);

            const endTime = document.createElement("p");
            endTime.innerHTML = `<strong>End:</strong> ${interval.end.toTimeString().slice(0, 5)}`;
            bookingDiv.appendChild(endTime);

            szabadContainer.appendChild(bookingDiv);
        });

    } catch (error) {
        console.error("Error fetching reservations:", error);
        foglaltContainer.innerHTML = "<p>No reservations found.</p>";
        szabadContainer.innerHTML = "<p>Unable to determine free slots.</p>";
    }
}

