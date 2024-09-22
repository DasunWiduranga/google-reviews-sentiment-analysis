import React, { useState } from "react";
import axios from "axios";
import "./index.css";

function App() {
  const [businessName, setBusinessName] = useState("");
  const [reviews, setReviews] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleInputChange = (e) => {
    setBusinessName(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setReviews([]);
    setLoading(true);

    try {
      // Log the input business name for debugging
      console.log("Business Name Sent:", businessName);

      const response = await axios.post("http://localhost:5000/scrape", {
        businessName,
      });

      // Log the API response for debugging
      console.log("API Response:", response.data);

      if (response.data.reviews) {
        setReviews(response.data.reviews);
      } else if (response.data.error) {
        setError(response.data.error);
      } else {
        setError("Unexpected response from server");
      }
    } catch (err) {
      setError("Error fetching data. Please try again.");
      console.error("Error fetching data:", err); // Log the error
    }

    setLoading(false);
  };

  return (
    <div className="app-container">
      <h1>Google Business Reviews Scraper</h1>
      <form onSubmit={handleSubmit} className="form-container">
        <label>
          Business Name or URL:
          <input
            type="text"
            value={businessName}
            onChange={handleInputChange}
            placeholder="Enter Business Name or URL"
            required
            className="input-field"
          />
        </label>
        <button type="submit" className="submit-button">
          {loading ? "Loading..." : "Scrape Reviews"}
        </button>
      </form>

      {error && <p className="error-message">Error: {error}</p>}

      {reviews.length > 0 && (
        <div className="reviews-container">
          <h2>Reviews and Sentiment Analysis:</h2>
          <ul className="reviews-list">
            {reviews.map((review, index) => (
              <li key={index} className="review-item">
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
