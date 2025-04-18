function validateForm() {
    let valid = true;

    // Clear previous error messages
    document.querySelectorAll('.error-message').forEach(error => error.textContent = "");
    document.getElementById("successMsg").textContent = ""; // Clear previous success message
    document.getElementById("errorMsg").textContent = ""; // Clear the general error message

    // Field validation rules
    const fields = [
        { id: "fullName", message: "Full Name is required." },
        { id: "email", message: "Please enter a valid email.", pattern: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/ },
        { id: "username", message: "Username is required." },
        { id: "phone", message: "Please enter a valid phone number.", pattern: /^[0-9]{10}$/ },
        { id: "password", message: "Password is required." }
    ];

    fields.forEach(field => {
        let input = document.getElementById(field.id);
        let errorElement = document.createElement("div"); // Create error message dynamically
        errorElement.classList.add("error-message");

        if (!input.value || (field.pattern && !field.pattern.test(input.value))) {
            errorElement.textContent = field.message;
            input.parentNode.appendChild(errorElement); // Append error below the input field
            valid = false;
        }
    });

    // Confirm Password Validation
    let password = document.getElementById("password").value;
    let confirmPassword = document.getElementById("confirmPassword").value;
    if (confirmPassword !== password) {
        let confirmPasswordError = document.createElement("div");
        confirmPasswordError.classList.add("error-message");
        confirmPasswordError.textContent = "Passwords do not match.";
        document.getElementById("confirmPassword").parentNode.appendChild(confirmPasswordError);
        valid = false;
    }

    // Gender Validation
    if (!document.querySelector('input[name="gender"]:checked')) {
        let genderError = document.createElement("div");
        genderError.classList.add("error-message");
        genderError.textContent = "Please select your gender.";
        document.querySelector(".gender-options").appendChild(genderError);
        valid = false;
    }

    // Display success or error message above the Register button
    if (valid) {
        document.getElementById("successMsg").textContent = "User registered successfully!";
        document.getElementById("successMsg").style.color = "green";
    } else {
        document.getElementById("errorMsg").textContent = "Please fix the errors above.";
        document.getElementById("errorMsg").style.color = "red";
    }

    return valid; // Prevent form submission if validation fails
}
