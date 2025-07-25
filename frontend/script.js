// Notification utility
function showNotification(message, isError = false) {
  const notif = document.getElementById('notification');
  notif.textContent = message;
  notif.className = isError ? 'show error' : 'show';
  setTimeout(() => {
    notif.className = notif.className.replace('show', '');
  }, 2500);
}

// Handle Bogie Checksheet Form Submission
document.getElementById('bogieForm').addEventListener('submit', async function(e) {
  e.preventDefault();
  const form = e.target;
  const data = {
    inspector_name: form.inspector_name.value,
    bogie_number: form.bogie_number.value,
    remarks: form.remarks.value
  };
  form.querySelector('button[type="submit"]').disabled = true;
  form.querySelector('button[type="submit"]').textContent = 'Submitting...';
  try {
    const res = await fetch('http://localhost:8000/api/forms/bogie-checksheet', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (res.ok) {
      showNotification('Submitted successfully!');
      form.reset();
    } else {
      showNotification('Submission failed!', true);
    }
  } catch {
    showNotification('Error connecting to server!', true);
  }
  form.querySelector('button[type="submit"]').disabled = false;
  form.querySelector('button[type="submit"]').textContent = 'Submit';
});

// Fetch and display Wheel Specifications
async function fetchWheelSpecs() {
  const list = document.getElementById('wheelSpecsList');
  const btn = document.getElementById('loadSpecsBtn');
  list.innerHTML = '';
  btn.disabled = true;
  btn.textContent = 'Loading...';
  try {
    const res = await fetch('http://localhost:8000/api/forms/wheel-specifications');
    if (res.ok) {
      const specs = await res.json();
      if (specs.length === 0) {
        list.innerHTML = '<li>No wheel specifications found.</li>';
      } else {
        specs.forEach(spec => {
          const li = document.createElement('li');
          li.textContent = `Type: ${spec.wheel_type}, Diameter: ${spec.diameter}, Material: ${spec.material}`;
          list.appendChild(li);
        });
      }
    } else {
      list.innerHTML = '<li>Failed to load specifications.</li>';
      showNotification('Failed to load specifications!', true);
    }
  } catch {
    list.innerHTML = '<li>Error connecting to server.</li>';
    showNotification('Error connecting to server!', true);
  }
  btn.disabled = false;
  btn.textContent = 'Load Wheel Specifications';
}

document.getElementById('loadSpecsBtn').addEventListener('click', fetchWheelSpecs); 