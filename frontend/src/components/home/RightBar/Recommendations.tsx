import React from "react";
import styles from "./styles/Recommendations.module.css";

export default function Recommendations() {
  const openPost = (id: number) => {
    console.log(`opening post ${id}`);
  };

  const recommendations = new Array(20).fill(0).map((val, index) => ({
    text: "I hope you're all as thrilled as I am about the latest developments with our Starship program. The journey to space has always been a dream of humanity, and we're taking giant leaps to make it a reality!",
    id: index,
  }));

  return (
    <div className={styles.recommendations}>
      {recommendations.map((reco, index) => (
        <button
          key={index}
          className={styles.button}
          onClick={() => openPost(reco.id)}
        >
          {reco.text}
        </button>
      ))}
    </div>
  );
}
