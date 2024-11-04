// Function to open the booking modal with the selected room name
function bookRoom(room) {
    document.getElementById('roomName').textContent = room;
    document.getElementById('bookingModal').style.display = 'flex';
}

// Function to close the modal
function closeModal() {
    document.getElementById('bookingModal').style.display = 'none';
}

// Function to simulate booking submission
function submitBooking() {
    const name = document.getElementById('name').value;
    const date = document.getElementById('date').value;
    const room = document.getElementById('roomName').textContent;
    
    if (name && date) {
        alert(`Room "${room}" booked successfully by ${name} on ${date}!`);
        closeModal();
    } else {
        alert("Please fill in all the details.");
    }
}
