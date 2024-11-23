// Set the base API URL
const API_BASE_URL = "http://127.0.0.1:8000";

// Function to open the booking modal
function openBookingModal(roomId) {
    document.getElementById("roomName").textContent = `Room ${roomId}`;
    document.getElementById("bookingModal").style.display = "block";
    document.getElementById("bookingForm").dataset.roomId = roomId; // Store the room ID in the form
}

// Function to close the modal
function closeModal() {
    document.getElementById("bookingModal").style.display = "none";
}

// Function to submit the booking
async function submitBooking() {
    const roomId = document.getElementById("bookingForm").dataset.roomId;
    const name = document.getElementById("name").value;
    const date = document.getElementById("date").value;
    const startHour = document.getElementById("start_hour").value;
    const endHour = document.getElementById("end_hour").value;

    // Construct the request payload
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
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(bookingData),
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

const predefinedRooms = [
    // Level 1 Rooms (IDs starting with 1)
    { id: 111, top: "20px", left: "20px", width: "140px", height: "140px" },
    { id: 112, top: "20px", left: "170px", width: "140px", height: "140px" },
    { id: 113, top: "20px", left: "320px", width: "140px", height: "140px" },
    { id: 114, top: "20px", left: "470px", width: "140px", height: "140px" },
    { id: 128, top: "20px", left: "620px", width: "140px", height: "140px" },
    { id: 129, top: "20px", left: "770px", width: "140px", height: "140px" },
    { id: 130, top: "20px", left: "920px", width: "140px", height: "140px" },
    { id: 131, top: "20px", left: "1070px", width: "140px", height: "140px" },
    { id: 132, top: "20px", left: "1220px", width: "140px", height: "140px" },
    { id: 133, top: "20px", left: "1370px", width: "140px", height: "140px" },

];


async function fetchRooms() {
    try {
        const response = await fetch(`${API_BASE_URL}/rooms`);
        if (!response.ok) {
            throw new Error("Failed to fetch rooms.");
        }

        const dbRooms = await response.json(); // Example: [{ id: 133 }, { id: 132 }]
        console.log("Database rooms:", dbRooms);

        const blueprint = document.querySelector(".blueprint");
        blueprint.innerHTML = ""; // Clear existing content

        predefinedRooms.forEach(predefinedRoom => {
            const matchingDbRoom = dbRooms.find(dbRoom => dbRoom.id === predefinedRoom.id);
            const roomId = matchingDbRoom ? matchingDbRoom.id : 0;

            // Create a room element
            const roomDiv = document.createElement("div");
            roomDiv.className = "room";
            roomDiv.textContent = `Room ${roomId}`;
            roomDiv.onclick = roomId !== 0 ? () => openBookingModal(roomId) : null; // Only clickable if room exists

            // Apply styles
            roomDiv.style.position = "absolute";
            roomDiv.style.top = predefinedRoom.top;
            roomDiv.style.left = predefinedRoom.left;
            roomDiv.style.width = predefinedRoom.width;
            roomDiv.style.height = predefinedRoom.height;

            // Mark non-clickable rooms
            if (roomId === 0) {
                roomDiv.classList.add("nonclickable");
            }

            // Append to the blueprint
            blueprint.appendChild(roomDiv);
        });
    } catch (err) {
        console.error("Error fetching rooms:", err);
    }
}

document.addEventListener("DOMContentLoaded", fetchRooms);




// Load rooms when the page is loaded
document.addEventListener("DOMContentLoaded", fetchRooms);
