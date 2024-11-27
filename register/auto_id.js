function generateYouChatID() {
    // Get the current year and take the last two digits
    const year = new Date().getFullYear().toString().slice(-2);

    // Generate a 6-digit random number
    const randomNumber = Math.floor(100000 + Math.random() * 900000); // Ensures 6 digits

    // Combine year and random number
    const youChatID = year + randomNumber;

    // Set the value of the input field
    document.getElementById('youchat-id').value = youChatID;
}