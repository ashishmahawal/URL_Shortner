// pages/index.js
import { useState } from "react";
import fetch from "isomorphic-unfetch";
import styles from "../styles/Home.module.css";

const Home = () => {
  const [longUrl, setLongUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [uid, setUID] = useState("");

  const shortenUrl = async () => {
    //const long_url = "https://rapidapi.com/guides/query-parameters-fetch";
    const requestUrl = `http://localhost:8000/v1/shorten`;
    try {
      const response = await fetch(requestUrl, {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ long_url: longUrl }),
      });

      const data = await response.json();

      if (response.ok) {
        setShortUrl(data.short_url);
        setUID(data.uid);
        setLongUrl('')
      } else {
        console.error(data.error || "Failed to shorten URL");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.content}>
      <h1 className={styles.title}>Squeezy URL Shortener</h1>
        <div className="container mb-8">
          {" "}
          {/* Use tailwindcss 'container' class directly */}
          <input
            type="text"
            placeholder="Enter URL to shorten"
            value={longUrl}
            onChange={(e) => setLongUrl(e.target.value)}
            className={styles.input}
          />
          <button onClick={shortenUrl} className={styles.button}>
            Squeez URL
          </button>
        </div>
        {shortUrl && (
          <div className={"container mt-8"}>
            <p className="mb-2">Shortened URL:</p>
            <a
              href={shortUrl}
              target="_blank"
              rel="noopener noreferrer"
              className={styles.link}
            >
              {shortUrl}
            </a>
          </div>
        )}
      </div>
    </div>
  );
};

export default Home;
