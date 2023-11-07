import React from "react";
import styles from "./styles/LeftBarButtons.module.css";
import TweetButton from "./TweetButton";

export default function LeftBarButtons() {
  const getTextColor = (path: string) => {
    return window.location.pathname === path
      ? styles.selected
      : styles.unselected;
  };

  const buttons = [
    {
      text: "home",
      image: `${process.env.PUBLIC_URL}/home.svg`,
      colorClass: getTextColor("/"),
      onclick: () => {},
    },
    {
      text: "profile",
      image:
        "https://upload.wikimedia.org/wikipedia/commons/9/99/Elon_Musk_Colorado_2022_%28cropped2%29.jpg",
      colorClass: getTextColor("/profile"),
      onclick: () => {},
    },
  ];

  return (
    <div className={styles.buttons}>
      {buttons.map((button, index) => (
        <button key={index} onClick={button.onclick} className={styles.button}>
          <img src={button.image} alt={button.text} />
          <span className={button.colorClass}>{button.text}</span>
        </button>
      ))}
      <TweetButton />
    </div>
  );
}
