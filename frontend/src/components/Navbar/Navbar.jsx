import React from 'react'
import styles from './Navbar.module.css'
import { BsAirplane } from "react-icons/bs";



export const Navbar = () => {

  return (
    <nav className={styles.navbar}>
      {/* <button className={styles.loginBtn}>Login</button> */}
      {/* <img className={styles.title} src='/logo192.png' alt='logo' /> */}
      <BsAirplane className={styles.icon}/>

    </nav> 
  );
  
};
