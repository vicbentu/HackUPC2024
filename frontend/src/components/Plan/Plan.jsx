import React, { useEffect, useState } from 'react';
import styles from './Plan.module.css';

export const Plan = () => {
  const [restaurants, setRestaurants] = useState([
    {
      title: "Restaurant 1",
      streetName: "Street 1",
      stars: 4,
      city: "City 1"
    },
    {
      title: "Restaurant 2",
      streetName: "Street 2",
      stars: 5,
      city: "City 2"
    },
    {
      title: "Restaurant 3",
      streetName: "Street 3",
      stars: 3,
      city: "City 3"
    }
  ]);

  useEffect(() => {
    // fetch('https://localhost:5000/getRestaurants')
    // .then((response) => response.json())
    // .then((data) => setRestaurants(data));
  }, []);

  return (
    <div className={styles.planContainer}>
      <h2>Restaurants</h2>
      {restaurants.map((restaurant, index) => (
        <div key={index} className={styles.restaurant}>
          <h3>{restaurant.title}</h3>
          <p>{restaurant.streetName}</p>
          <p>{restaurant.stars} Stars</p>
          <p>{restaurant.city}</p>
        </div>
      ))}
    </div>
  );
};