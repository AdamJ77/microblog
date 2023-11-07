import React from "react";
import styles from "./styles/RightBar.module.css";
import Recommendations from "./Recommendations";

export default function RightBar() {
  return (
    <section className={styles.section}>
      <div className={styles.content}>
        <h2 className={styles.h2}>posts for you</h2>
        <Recommendations />
      </div>
    </section>
  );
}
