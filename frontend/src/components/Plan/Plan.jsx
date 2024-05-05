import React from 'react';
import styles from './Plan.module.css';

export const Plan = ({plans, setPlans}) => {
  return (
    <div className={styles.planContainer}>
      <h2>Restaurants</h2>
      {plans.map((restaurant, index) => (
        <div key={index} className={styles.restaurant}>
          <h3 key={index}>Restaurant: {restaurant.restaurant}</h3>
          <input type="date" value={restaurant.date} readOnly={true} />
          <fieldset>
          {restaurant.group.map(member => (<p>{member}</p>))}
          </fieldset>
					<button key={`button${index}`} onClick={() => {setPlans(plans.filter(x => restaurant.date !== x.date))}}>Decline</button>
        </div>
      ))}
    </div>
  );
};
