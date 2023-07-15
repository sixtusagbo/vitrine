$(document).ready(function () {
  let currentTab = 0; // Current tab is set to be the first tab (0)
  showTab(currentTab); // Display the current tab

  function showTab(n) {
    // This function will display the specified tab of the form...
    const x = document.getElementsByClassName('tab');
    // x[n].style.display = 'block';
    $(x[n]).show();

    // display or hide Previous/Next buttons:
    if (n === 0) {
      document.getElementById('prevBtn').style.display = 'none';
    } else {
      document.getElementById('prevBtn').style.display = 'inline-block';
    }
    if (n === x.length - 1) {
      document.getElementById('nextBtn').innerHTML = 'Submit';
    } else {
      document.getElementById('nextBtn').innerHTML = 'Continue';
    }

    // update step indicators
    fixStepIndicator(n);
  }

  /* Figure out which tab to display */
  function changeStep(n) {
    const tabs = document.getElementsByClassName('tab');
    // If I'm to move forward and any field in the current tab is invalid exit the function
    if (n === 1 && !validateForm()) return false;
    // Hide the current tab
    tabs[currentTab].style.display = 'none';
    // Increase or decrease the current tab by 1
    currentTab = currentTab + n;

    // if you have reached the end of the form
    if (currentTab >= tabs.length) {
      // submit the form
      document.getElementById('vixpertForm').submit();
      return false;
    }
    // otherwise, display the correct tab
    showTab(currentTab);
  }

  /* Deal with validation of the form fields */
  function validateForm() {
    let x = true;
    let y = true;
    let i = true;
    let valid = true;
    x = document.getElementsByClassName('tab');
    y = x[currentTab].getElementsByTagName('input');

    // Check every input field in the current tab
    for (i = 0; i < y.length; i++) {
      // If a field is empty
      if (y[i].value === '') {
        // add "is-invalid" class to the field
        if ($(y[i]).hasClass('is-valid')) $(y[i]).removeClass('is-valid');
        if (!$(y[i]).hasClass('is-invalid')) $(y[i]).addClass('is-invalid');
        // and set the current valid status to false
        valid = false;
      } else {
        if ($(y[i]).hasClass('is-invalid')) $(y[i]).removeClass('is-invalid');
        if (!$(y[i]).hasClass('is-valid')) $(y[i]).addClass('is-valid');
      }
    }

    // If the valid status is true, mark the step as finished and valid
    if (valid) {
      document.getElementsByClassName('step')[currentTab].className +=
        ' finish';
    }

    return valid;
  }

  /* Update active step indicator */
  function fixStepIndicator(n) {
    let i = document.getElementsByClassName('step');
    const x = document.getElementsByClassName('step');

    for (i = 0; i < x.length; i++) {
      x[i].className = x[i].className.replace(' active', '');
    }

    // add "active" class on the current step:
    $(x[n]).addClass('active');
  }

  document
    .getElementById('nextBtn')
    .addEventListener('click', () => changeStep(1));
  document
    .getElementById('prevBtn')
    .addEventListener('click', () => changeStep(-1));

  $('#add_detail_point_input').click(function (e) {
    e.preventDefault();

    $('#detail_points').append(
      '<input type="text" class="form-control form-control bg-gray-800 border-dark detail_point mb-2">'
    );

    if ($('.detail_point').length === 5) {
      $(this).remove();
    }
  });
});
