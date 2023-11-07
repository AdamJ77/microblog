import React from "react";
import styles from "./styles/LeftBar.module.css";
import Logo from "./Logo";
import LeftBarButtons from "./LeftBarButtons";

export default function LeftBar() {
  return (
    <div className={styles.sidebar}>
      <Logo />
      <LeftBarButtons />
    </div>
  );
}
