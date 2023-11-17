import React from "react";
import { useNavigate } from "react-router-dom";
import styles from "./styles/notFoundInfo.module.css";

export default function NotFoundInfo() {
  const navigate = useNavigate();

  return (
    <div className={styles.wrapper}>
      <img
        src={`${process.env.PUBLIC_URL}/icons/logo.png`}
        alt="logo"
        className={styles.logo}
      />
      <div>Requested resource doesn't exist!</div>
      <button onClick={() => navigate("/")} className={styles.button}>
        Bring me back to home.
      </button>
    </div>
  );
}
