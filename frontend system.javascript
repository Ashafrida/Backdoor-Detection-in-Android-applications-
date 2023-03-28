const form = document.querySelector('form');
const submitButton = document.querySelector('#submit-button');

submitButton.addEventListener('click', function(event) {
  event.preventDefault(); // prevent default form submission behavior

  const formData = new FormData(form);

  const data = {
    name: formData.get('name'),
    email: formData.get('email'),
    report_time: formData.get('report_time')
  };

  const json = JSON.stringify(data);

  fetch('https://example.com/api/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: json
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
    alert('Registration successful!');
  })
  .catch(error => {
    console.error('Error:', error);
    alert('An error occurred while submitting the form.');
  });
});
