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

  // Language filter
  const languageFilter = document.getElementById('languageFilter');
  if (languageFilter) {
    languageFilter.addEventListener('change', (e) => {
      const lang = e.target.value;
      if (lang) {
        window.location.href = `/language/${lang}`;
      } else {
        window.location.href = '/';
      }
    });
  }
  
  // Languages link dropdown
  const languagesLink = document.getElementById('languagesLink');
  if (languagesLink) {
    languagesLink.addEventListener('click', (e) => {
      e.preventDefault();
      const lang = prompt('Enter language code (en, hi, ta, te, ml, kn, es, fr, ja, ko):');
      if (lang) {
        window.location.href = `/language/${lang}`;
      }
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

  // Range sliders
  const userScore = document.getElementById('userScore');
  const userScoreValue = document.getElementById('userScoreValue');
  if (userScore && userScoreValue) {
    userScore.addEventListener('input', (e) => {
      userScoreValue.textContent = e.target.value;
    });
  }

  const minVotes = document.getElementById('minVotes');
  const minVotesValue = document.getElementById('minVotesValue');
  if (minVotes && minVotesValue) {
    minVotes.addEventListener('input', (e) => {
      minVotesValue.textContent = e.target.value;
    });
  }

  const runtime = document.getElementById('runtime');
  const runtimeValue = document.getElementById('runtimeValue');
  if (runtime && runtimeValue) {
    runtime.addEventListener('input', (e) => {
      runtimeValue.textContent = e.target.value;
    });
  }

  // Search button functionality
  const searchButton = document.querySelector('.search-button');
  if (searchButton) {
    searchButton.addEventListener('click', () => {
      const genreIds = Array.from(selectedGenres).join(',');
      const fromDate = document.getElementById('fromDate')?.value;
      const toDate = document.getElementById('toDate')?.value;
      const sortBy = document.querySelector('input[name="sortBy"]:checked')?.value || 'release_date.desc';
      const langFilter = document.getElementById('languageFilter')?.value;
      const userScoreVal = document.getElementById('userScore')?.value;
      const minVotesVal = document.getElementById('minVotes')?.value;
      const runtimeVal = document.getElementById('runtime')?.value;
      const keywordsVal = document.getElementById('keywords')?.value;
      
      const params = new URLSearchParams();
      params.append('sort_by', sortBy);
      if (genreIds) params.append('genres', genreIds);
      if (fromDate) params.append('from_date', fromDate);
      if (toDate) params.append('to_date', toDate);
      if (langFilter) params.append('with_original_language', langFilter);
      if (userScoreVal > 0) params.append('vote_average_gte', userScoreVal);
      if (minVotesVal > 0) params.append('vote_count_gte', minVotesVal);
      if (runtimeVal > 0) params.append('with_runtime_gte', runtimeVal);
      if (keywordsVal) params.append('keywords', keywordsVal);
      params.append('page', 1);
      
      window.location.href = `/discover?${params.toString()}`;
    });
  }

  // Add smooth scroll behavior
  document.documentElement.style.scrollBehavior = 'smooth';
});
