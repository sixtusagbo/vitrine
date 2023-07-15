// for dynamic url
const { protocol, hostname, pathname, href: currentUrl } = window.location;
const apiUrl = `${protocol}//${hostname}:5001/api/v1`;
let brand = {};
const handle = pathname.substr(1);

const populateDOM = () => {
  // inside head tag
  $('title').text(`${brand.name} | Vitrine`);
  $('meta[name="title"]').attr('content', `${brand.name} | Vitrine`);
  $('meta[property="og:title"]').attr('content', `${brand.name} | Vitrine`);
  $('meta[property="twitter:title"]').attr('content', `${brand.name} | Vitrine`);
  $('meta[property="og:url"]').attr('content', currentUrl);
  $('meta[property="twitter:url"]').attr('content', currentUrl);

  if (brand.description) {
    $('meta[name="description"]').attr('content', brand.description);
    $('meta[property="og:description"]').attr('content', brand.description);
    $('meta[property="twitter:description"]').attr('content', brand.description);
  } else {
    $('meta[name="description"]').remove();
    $('meta[property="og:description"]').remove();
    $('meta[property="twitter:description"]').remove();
  }

  if (brand.cover_image) {
    $('meta[property="og:image"]').attr('content', brand.cover_image);
    $('meta[property="twitter:image"]').attr('content', brand.cover_image);
  } else {
    $('meta[property="og:image"]').remove();
    $('meta[property="twitter:image"]').remove();
  }

  // inside body tag
  $('.brandname').text(brand.name);
  if (brand.statement) $('.header #statement').text(brand.statement);
  if (brand.description) $('.description').text(brand.description);
  if (brand.cover_image) $('.header #cover_image').attr('src', brand.cover_image);
  if (brand.detail_lead) $('#details #detail_lead').text(brand.detail_lead);
  if (brand.detail_image) $('#details #detail_image').attr('src', brand.detail_image);

  if (brand.is_solopreneur) {
    $('.solopreneur').text(brand.is_solopreneur ? 'me' : 'us');
    $('footer .solopreneur').text(brand.is_solopreneur ? 'I' : 'We');
  }

  if (brand.detail_points) {
    $('#detail_points').empty();

    for (const point of brand.detail_points) {
      let listItem = '<li class="d-flex">';
      listItem += '<i class="fas fa-square"></i>';
      listItem += '<p class="flex-grow-1">';
      listItem += point;
      listItem += '</p>';
      listItem += '</li>';
      $('#detail_points').append(listItem);
    }
  }

  populateWorks();

  if (brand.address) {
    $('#googleMaps').attr('src', `https://www.google.com/maps/embed/v1/place?key=AIzaSyCNveGQ9bfpKFwWzQLLftrR9hNiHwdqQG8&q=${brand.address}`);
  }

  if (brand.twitter_url) {
    $('#twitter-link').attr('href', brand.twitter_url);
  } else {
    $('#twitter-link').parent().hide();
  }

  if (brand.instagram_url) {
    $('#instagram-link').attr('href', brand.instagram_url);
  } else {
    $('#instagram-link').parent().hide();
  }

  if (brand.youtube_url) {
    $('#youtube-link').attr('href', brand.youtube_url);
  } else {
    $('#youtube-link').parent().hide();
  }

  if (brand.telegram_url) {
    $('#telegram-link').attr('href', brand.telegram_url);
  } else {
    $('#telegram-link').parent().hide();
  }

  $('#brand-email').attr('href', `mailto:${brand.email}`);
  $('#brand-email strong').text(brand.email);

  $('#whatsapp-btn').attr('href', `https://wa.me/${brand.whatsapp_no}`);

  const createdAt = new Date(brand.created_at);
  $('#created-year').text(createdAt.getFullYear());
};

const populateWorks = async () => {
  await $.get(`${apiUrl}/brands/${handle}/works`,
    function (data) {
      brand.works = data;
    }
  );

  if (brand.works.length) {
    $('#works').empty();

    for (const work of brand.works) {
      let project = '<div class="card">';
      project += `<img class="img-fluid" src="${work.image_url}" alt="${work.title}">`;
      project += '<div class="card-body">';
      project += `<h5 class="card-title">${work.title}</h5>`;
      project += `<p class="card-text">${work.description}</p>`;
      project += '</div>';
      project += '</div>';
      $('#works').append(project);
    }
  }
};

const setup = () => {
  $.get(`${apiUrl}/brands/${handle}/public`,
    function (data) {
      brand = data;

      populateDOM();
    }
  );
};

$(document).ready(setup);
