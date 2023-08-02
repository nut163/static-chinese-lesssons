// Function to navigate to a different page
function navigateToPage(page) {
    window.location.href = page;
}

// Function to sign up a new user
function signupUser(user) {
    // AJAX call to server to sign up user
    $.ajax({
        url: '/signup',
        type: 'POST',
        data: user,
        success: function(data) {
            // Display success message
            $('#signupSuccess').show();
        },
        error: function(error) {
            // Display error message
            $('#signupError').show();
        }
    });
}

// Function to load course content
function loadCourseContent(content) {
    $('#main-content').html(content);
}

// Event listener for navigation
$('#navbar a').click(function(e) {
    e.preventDefault();
    navigateToPage($(this).attr('href'));
});

// Event listener for sign up form
$('#signup-form').submit(function(e) {
    e.preventDefault();
    var user = {
        name: $('#name').val(),
        email: $('#email').val(),
        password: $('#password').val()
    };
    signupUser(user);
});

// Load initial course content
loadCourseContent('Welcome to Your 30-Day Chinese Language Journey!');