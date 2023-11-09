import React from "react";
import styles from "./styles/Loading.module.css";
import { PulseLoader } from "react-spinners";

interface ILoadingProps {
  text: string;
}

export default function Loading({ text }: ILoadingProps) {
  return (
    <div className={styles.loading}>
      <div className={styles.logo}>
        <PulseLoader color="#1e9bf1" />
      </div>
      <h2 className={styles.text}>{text}</h2>
    </div>
  );
}
