import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [businessName, setBusinessName] = useState('');
  const [reviews, setReviews] = useState(null);
  const [error, setError] = useState('');

  const handleInputChange = (e) => {
    setBusinessName(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setReviews(null);
    
    try {
      const response = await axios.post('http://localhost:5000/scrape', { businessName });
      setReviews(response.data);
    } catch (err) {
      setError('Error fetching data. Please try again.');
      console.error(err);
    }
  };

  return (
    <div className="App">
      <h1>Google Business Reviews Scraper</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Business Name or URL:
          <input
            type="text"
            value={businessName}
            onChange={handleInputChange}
            placeholder="Enter Business Name or URL"
            required
          />
        </label>
        <button type="submit">Scrape Reviews</button>
      </form>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {reviews && (
        <div>
          <h2>Reviews and Sentiment Analysis:</h2>
          <ul>
            {reviews.map((review, index) => (
              <li key={index}>
                <strong>Review:</strong> {review.text} <br />
                <strong>Sentiment:</strong> {review.sentiment}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
