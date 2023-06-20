'use strict';

const validateInputs = () => {
  const $handle = $('#handle');
  const handleValue = $handle.val();
  const $brandName = $('#name');
  const nameValue = $brandName.val();
  const $email = $('#email');
  const emailValue = $email.val();
  const $password = $('#password');
  const passwordValue = $password.val();

  // Handle input
  if ($handle.length) {
    if (handleValue === '') {
      $handle.siblings('.invalid-feedback').text('Please provide a handle');
      $handle.addClass('is-invalid');

      return false;
    } else if (handleValue.length < 3) {
      $handle.siblings('.invalid-feedback').text('Must not be less than 3 words');
      $handle.addClass('is-invalid');

      return false;
    } else {
      if ($handle.hasClass('is-invalid')) {
        $handle.removeClass('is-invalid');
      }
      $handle.addClass('is-valid');
    }
  }

  // Brand name input
  if ($brandName.length) {
    if (nameValue === '') {
      $brandName.siblings('.invalid-feedback').text('Please provide a brand name');
      $brandName.addClass('is-invalid');

      return false;
    } else if (nameValue.length < 3) {
      $brandName.siblings('.invalid-feedback').text('Must not be less than 3 words');
      $brandName.addClass('is-invalid');

      return false;
    } else {
      if ($brandName.hasClass('is-invalid')) {
        $brandName.removeClass('is-invalid');
      }
      $brandName.addClass('is-valid');
    }
  }

  // Email input
  if (emailValue === '') {
    $email.siblings('.invalid-feedback').text('Please provide an email');
    $email.addClass('is-invalid');

    return false;
  } else if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(emailValue)) {
    $email.siblings('.invalid-feedback').text('Invalid email');
    $email.addClass('is-invalid');

    return false;
  } else {
    if ($email.hasClass('is-invalid')) {
      $email.removeClass('is-invalid');
    }
    $email.addClass('is-valid');
  }

  // Password input
  if (passwordValue === '') {
    $password.siblings('.invalid-feedback').text('Please provide a password');
    $password.addClass('is-invalid');

    return false;
  } else if (passwordValue.length < 5) {
    $password.siblings('.invalid-feedback').text('Password is too short');
    $password.addClass('is-invalid');

    return false;
  } else {
    if ($password.hasClass('is-invalid')) {
      $password.removeClass('is-invalid');
    }
    $password.addClass('is-valid');
  }

  return true;
}

$(document).ready(
  () => {
    // Fetch all the forms we want to apply custom validation styles to
    const forms = document.querySelectorAll('.needs-validation');

    // Loop over them, validate and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!validateInputs()) {
          event.preventDefault();
          event.stopPropagation();
        }

      }, false);
    })
  }
);
