import React, { useEffect, useState } from 'react';
import styles from './Plan.module.css';

export const Plan = ({plans}) => {
  return (
    <div className={styles.planContainer}>
      <h2>Restaurants</h2>
      {plans.map((restaurant, index) => (
        <div key={index} className={styles.restaurant}>
          <h3>Restaurant: {restaurant.restaurant}</h3>
          <input type="date" value={restaurant.date} readOnly={true} />
          <fieldset>
          {restaurant.group.map(member => (<p>{member}</p>))}
          </fieldset>
        </div>
      ))}
    </div>
  );
};