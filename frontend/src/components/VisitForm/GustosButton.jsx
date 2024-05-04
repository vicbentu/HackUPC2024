import React, { useState } from 'react';
import styles from './GustosButton.module.css';

const GustosButton = ({ gustos }) => {
  console.log(gustos)
  const [showModal, setShowModal] = useState(false);
  const [selectedGustos, setSelectedGustos] = useState([]);

  const handleGustoClick = (gusto) => {
    if (selectedGustos.includes(gusto)) {
      setSelectedGustos(selectedGustos.filter(item => item !== gusto));
    } else {
      setSelectedGustos([...selectedGustos, gusto]);
    }
  };

  const handleCloseModal = () => {
    setShowModal(false);
  };

  return (
                    <div className={styles.mainDiv}>
                        <button className={styles.button} onClick={() => setShowModal(true)}>Seleccionar gustos</button>
                        {showModal && (
                            <div className={styles.modal}>
                                <div className={styles.modalContent}>
                                    <span className={styles.close} onClick={handleCloseModal}>&times;</span>
                                    <h2>Selecciona tus gustos</h2>
                                    <div className={styles.gustosGrid}>
                                        {gustos.map(gusto => (
                                            <div className={styles.itemDiv} key={gusto.id}>
                                                <input type="checkbox" id={gusto.id} checked={selectedGustos.includes(gusto)}
                                                onChange={() => handleGustoClick(gusto)}
                                                />
                                                <label htmlFor={gusto.id}>{gusto.val}</label>
                                            </div>
                                        ))}
                                    </div> 
                                </div> 
                            </div> 
                        )} 
                    </div> 
                );
            };

export default GustosButton;
