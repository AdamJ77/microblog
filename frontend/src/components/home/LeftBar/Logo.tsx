import React from "react";
import styles from "./styles/Logo.module.css";

export default function Logo() {
  return (
    <img
      src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Logo_of_Twitter.svg/584px-Logo_of_Twitter.svg.png"
      alt="logo"
      className={styles.logo}
    />
  );
}
