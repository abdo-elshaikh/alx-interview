#!/usr/bin/node
const request = require('request');

function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body.name);
      }
    });
  });
}

function getMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, { json: true }, async (error, response, body) => {
    if (error) {
      console.error('Failed to retrieve data:', error.message);
      return;
    }

    const characterUrls = body.characters;

    for (const characterUrl of characterUrls) {
      try {
        const name = await getCharacterName(characterUrl);
        console.log(name);
      } catch (err) {
        console.error('Failed to retrieve character:', err.message);
      }
    }
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node 0-starwars_characters.js <movie_id>');
} else {
  getMovieCharacters(movieId);
}
