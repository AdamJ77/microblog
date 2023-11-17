import React from "react";
import styles from "./styles/Search.module.css";

export default function Search() {
  return (
    <div className={styles.wrapper}>
      <input type="text" placeholder="search Y" className={styles.search} />
    </div>
  );
}
