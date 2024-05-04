import React, { useState, useEffect } from 'react';
import styles from './VisitForm.module.css';
import RestaurantsProvider from '../../RestaurantsProvider.js';
import GustosButton from './GustosButton'; // Importa el componente GustosButton

function VisitForm({setPlans}) {
  const [city, setCity] = useState('');
  const [depDate, setDepDate] = useState('');
  const [retDate, setRetDate] = useState('');
  const [errors, setErrors] = useState({});
  const [gustos, setGustos] = useState([]);

	const isDictEmpty = (dict) => {
		for (var i in dict) return false
		return true
	}

  useEffect(() => {
    RestaurantsProvider.getAllGustos()
      .then(gustos => setGustos(gustos))
      .catch(error => console.log(error.message));
  }, []);

  const handleSubmit = (event) => {
    event.preventDefault();

    let formErrors = {};

    if (!city) {
      formErrors.city = "City is required";
    }

    if (!depDate || !retDate) {
      formErrors.date = "Date is required";
    } else if (depDate > retDate)
			formErrors.date = "Date range must be coherent"

		if (isDictEmpty(formErrors)) 
			RestaurantsProvider.getSchedule(city, depDate, retDate)
			.then(data => setPlans(data))
			.catch(error => console.log(error))

		

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
        {/* Reemplaza el select por el componente GustosButton */}
        <GustosButton gustos={gustos} />
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
}

export default VisitForm;
