import React, { useState } from 'react';
import styles from './VisitForm.module.css';

function VisitForm() {
  const [city, setCity] = useState('');
  const [date, setDate] = useState('');
  const [errors, setErrors] = useState({});

  const handleSubmit = (event) => {
    event.preventDefault();

    let formErrors = {};

    if (!city) {
      formErrors.city = "City is required";
    }

    if (!date) {
      formErrors.date = "Date is required";
    }

    setErrors(formErrors);

    if (Object.keys(formErrors).length === 0) {
      console.log(`Visiting ${city} on ${date}`);
    }
  };

  return (
    <div>
      <form className={styles.VisitForm} onSubmit={handleSubmit}>
      <label>
        City
        <input type="text" value={city} onChange={(e) => setCity(e.target.value)} />
        {errors.city && <p>{errors.city}</p>}
      </label>
      <label>
        Date
        <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
        {errors.date && <p>{errors.date}</p>}
      </label>
      <input type="submit" value="Submit" />
    </form>
    </div>
    

  );
}

export default VisitForm;