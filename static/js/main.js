
document.addEventListener('DOMContentLoaded', (event) => {
    // Code to handle form submission for pitch deck creation
    const form = document.querySelector('#create-deck-form');
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        const formData = new FormData(form);
        fetch('/pitch_deck/create/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = `/pitch_deck/view/${data.deck_id}/`;
            } else {
                alert('There was an error creating the pitch deck. Please try again.');
            }
        });
    });
});
