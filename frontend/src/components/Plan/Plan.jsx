import React, { useEffect, useState } from 'react';
import styles from './Plan.module.css';

export const Plan = () => {
  const [plan, setPlan] = useState([]);

  // useEffect(() => {
  //   fetch('http://localhost:5000/plan')  // Replace with your endpoint URL
  //     .then(response => response.json())
  //     .then(data => setPlan(data));
  // }, []);

  return (
    <div className={styles.planContainer}>
      <h2>Plan de Actividades</h2>
      {plan.map((activity, index) => (
        <div key={index} className={styles.activity}>
          <h3>{activity.name}</h3>
          <p>{activity.description}</p>
          <p>{activity.date}</p>
          <p>{activity.location}</p>
        </div>
      ))}
    </div>
  );
};