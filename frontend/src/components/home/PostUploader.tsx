import React from "react";
import Avatar from "./Avatar";
import styles from "./styles/PostUploader.module.css";

export default function PostUploader() {
  const me = {
    image:
      "https://upload.wikimedia.org/wikipedia/commons/9/99/Elon_Musk_Colorado_2022_%28cropped2%29.jpg",
    alt: "Elon Musk",
  };

  return (
    <form className={styles.wrapper}>
      <div className={styles.avatar}>
        <Avatar image={me.image} alt={me.alt} />
      </div>
      <div className={styles.inputs}>
        <textarea className={styles.textarea} placeholder="type..."></textarea>
        <label htmlFor="file-input">
          <input
            type="file"
            id="file-input"
            accept="png, jpg, mp3"
            className={styles.fileInput}
          />
          <img
            src={`${process.env.PUBLIC_URL}/addImage.svg`}
            className={styles.fileInputImage}
          />
        </label>
      </div>
      <button onClick={() => {}} className={styles.button} type="submit">
        tweet
      </button>
    </form>
  );
}
