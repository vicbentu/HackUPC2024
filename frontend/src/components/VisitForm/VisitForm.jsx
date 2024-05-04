import React, { useState, useEffect } from 'react';
import styles from './VisitForm.module.css';
import RestaurantsProvider from '../../RestaurantsProvider.js'

function VisitForm() {
  const [city, setCity] = useState('');
  const [depDate, setDepDate] = useState('');
  const [retDate, setRetDate] = useState('');
  const [errors, setErrors] = useState({});
	const [gustos, setGustos] = useState([]);

	useEffect(() => {RestaurantsProvider.getAllGustos().
									 then(gustos => setGustos(gustos)).
									 catch(error => console.log(error.message))}, []);
	

  const handleSubmit = (event) => {
    event.preventDefault();

    let formErrors = {};

    if (!city) {
      formErrors.city = "City is required";
    }

    if (!depDate || !retDate) {
      formErrors.date = "Date is required";
    }

    setErrors(formErrors);

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
        Departure Date
      </label>
      <input type="date" value={depDate} onChange={(e) => setDepDate(e.target.value)} />
      <label>
        Return Date
      </label>
      <input type="date" value={retDate} onChange={(e) => setRetDate(e.target.value)} />
      {errors.date && <p>{errors.date}</p>}
			<fieldset>
				{gustos.map(item => (
					<div>
					<input type="checkbox" id={item.id} value={item.val}/>
					<label htmlFor={item.id}>{item.val}</label>
					</div>
				))
				}
			</fieldset>
      <input type="submit" value="Submit" />
    </form>
    </div>
    

  );
}

export default VisitForm;
