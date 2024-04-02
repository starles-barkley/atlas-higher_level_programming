#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: node count_movies.js <API_URL>');
  process.exit(1);
}

const characterId = 18;

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    process.exit(1);
  }

  const data = JSON.parse(body);

  const moviesWithWedge = data.results.filter(movie => {
    return movie.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`);
  });

  console.log(`Number of movies with Wedge Antilles: ${moviesWithWedge.length}`);
});
