import React from "react";
import styles from "./styles/LeftBarButtons.module.css";
import TweetButton from "./TweetButton";
import Avatar from "../../common/Avatar";
import { useNavigate } from "react-router-dom";
import { useHomePageContext } from "../../../context/HomePageContext";

export default function LeftBarButtons() {
  const { user } = useHomePageContext();
  const navigate = useNavigate();

  const getTextColor = (path: string) => {
    return window.location.pathname === path
      ? styles.selected
      : styles.unselected;
  };

  const buttons = [
    {
      text: "home",
      image: `${process.env.PUBLIC_URL}/icons/home.svg`,
      colorClass: getTextColor("/"),
      onclick: () => {},
    },
    {
      text: "profile",
      image: user!.avatar,
      colorClass: getTextColor("/profile"),
      onclick: () => navigate("/profile"),
    },
  ];

  return (
    <div className={styles.buttons}>
      {buttons.map((button, index) => (
        <button key={index} onClick={button.onclick} className={styles.button}>
          <Avatar image={button.image} alt={button.text} />
          <span className={button.colorClass}>{button.text}</span>
        </button>
      ))}
      <TweetButton />
    </div>
  );
}
