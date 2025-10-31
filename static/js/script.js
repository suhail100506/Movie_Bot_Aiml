// Genre tag selection
document.addEventListener('DOMContentLoaded', () => {
  const genreTags = document.querySelectorAll('.genre-tag');
  const selectedGenres = new Set();

  genreTags.forEach(tag => {
    tag.addEventListener('click', () => {
      tag.classList.toggle('active');
      const genreId = tag.dataset.id;
      
      if (selectedGenres.has(genreId)) {
        selectedGenres.delete(genreId);
      } else {
        selectedGenres.add(genreId);
      }
      
      console.log('Selected genres:', Array.from(selectedGenres));
    });
  });

  // Language selector
  const languageSelect = document.getElementById('languageSelect');
  if (languageSelect) {
    languageSelect.addEventListener('change', (e) => {
      const lang = e.target.value;
      window.location.href = `/?lang=${lang}`;
    });
  }

  // Search functionality
  const searchBtn = document.querySelector('.search-btn');
  if (searchBtn) {
    searchBtn.addEventListener('click', () => {
      const searchQuery = prompt('Enter movie name:');
      if (searchQuery) {
        window.location.href = `/search?query=${encodeURIComponent(searchQuery)}`;
      }
    });
  }

  // Filter collapsible functionality
  const filterHeaders = document.querySelectorAll('.filter-header.collapsible');
  filterHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const content = header.nextElementSibling;
      const arrow = header.querySelector('.arrow-down');
      
      if (content.style.display === 'none') {
        content.style.display = 'block';
        arrow.style.transform = 'rotate(90deg)';
      } else {
        content.style.display = 'none';
        arrow.style.transform = 'rotate(0deg)';
      }
    });
  });

  // Search button functionality
  const searchButton = document.querySelector('.search-button');
  if (searchButton) {
    searchButton.addEventListener('click', () => {
      // Get selected filters
      const showMe = document.querySelector('input[name="showMe"]:checked')?.value;
      const searchAllAvailabilities = document.getElementById('searchAllAvailabilities')?.checked;
      const searchAllReleases = document.getElementById('searchAllReleases')?.checked;
      
      console.log('Filters:', {
        showMe,
        selectedGenres: Array.from(selectedGenres),
        searchAllAvailabilities,
        searchAllReleases
      });
      
      // You can add filter logic here
      alert('Filters applied! (Feature to be implemented)');
    });
  }

  // Add smooth scroll behavior
  document.documentElement.style.scrollBehavior = 'smooth';
});
