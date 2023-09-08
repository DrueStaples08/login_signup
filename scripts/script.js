document.addEventListener('DOMContentLoaded', function () {
    const passwordField = document.getElementById('signup-password');
    const confirmPasswordField = document.getElementById('signup-confirm-password');
    const passwordMatchMessage = document.getElementById('password-match-message');
    const signupButton = document.getElementById('signup-button');
    const signupForm = document.getElementById('signup-form');

    confirmPasswordField.addEventListener('input', function () {
        if (passwordField.value === confirmPasswordField.value) {
            passwordMatchMessage.textContent = 'Passwords match';
            passwordMatchMessage.style.color = 'green';
            signupButton.disabled = false;
        } else {
            passwordMatchMessage.textContent = 'Passwords do not match';
            passwordMatchMessage.style.color = 'red';
            signupButton.disabled = true;
        }
    });

    signupForm.addEventListener('submit', function (event) {
        if (passwordField.value !== confirmPasswordField.value) {
            event.preventDefault(); // Prevent form submission
            passwordMatchMessage.textContent = 'Passwords do not match. Please try again.';
            passwordMatchMessage.style.color = 'red';
            signupButton.disabled = true;
        }
    });
});








// document.addEventListener('DOMContentLoaded', function () {
//     const loginForm = document.getElementById('login-form');
//     const signupForm = document.getElementById('signup-form');
//     const showSignupLink = document.getElementById('show-signup');
//     const showLoginLink = document.getElementById('show-login');

//     // Initially hide the signup form
//     signupForm.style.display = 'none';

//     showSignupLink.addEventListener('click', function (event) {
//         event.preventDefault();
//         loginForm.style.display = 'none';
//         signupForm.style.display = 'block';
//     });

//     showLoginLink.addEventListener('click', function (event) {
//         event.preventDefault();
//         signupForm.style.display = 'none';
//         loginForm.style.display = 'block';
//     });
// });


// document.addEventListener('DOMContentLoaded', function () {
//     const loginForm = document.getElementById('login-form');
//     const signupForm = document.getElementById('signup-form');
//     const showSignupLink = document.getElementById('show-signup');
//     const showLoginLink = document.getElementById('show-login');

//     // Initially hide the signup form
//     signupForm.style.display = 'none';

//     showSignupLink.addEventListener('click', function (event) {
//         event.preventDefault();
//         loginForm.style.display = 'none';
//         signupForm.style.display = 'block';
//     });

//     showLoginLink.addEventListener('click', function (event) {
//         event.preventDefault();
//         signupForm.style.display = 'none';
//         loginForm.style.display = 'block';
//     });
// });
