import React, { useRef, useState } from "react";
import Avatar from "../../common/Avatar";
import styles from "./styles/PostUploader.module.css";

export default function PostUploader() {
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const [selectedFiles, setSelectedFiles] = useState<any[]>([]);

  const handleTextareaChange = () => {
    if (!textareaRef.current) return;
    textareaRef.current.style.height = "auto";
    textareaRef.current.style.height =
      textareaRef.current.scrollHeight + 10 + "px";
  };

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
        <textarea
          className={styles.textarea}
          placeholder="type..."
          ref={textareaRef}
          onChange={handleTextareaChange}
        ></textarea>
        <div>
          {selectedFiles.map((file) => (
            <img
              src={URL.createObjectURL(file)}
              className={styles["uploaded-image"]}
            />
          ))}
        </div>
        <label htmlFor="file-input">
          <input
            type="file"
            id="file-input"
            accept="png, jpg, mp3"
            multiple
            className={styles.fileInput}
            onChange={(e) =>
              setSelectedFiles((prev) => [...prev, ...(e.target.files as any)])
            }
          />
          <img
            src={`${process.env.PUBLIC_URL}/icons/addImage.svg`}
            className={styles.fileInputImage}
          />
        </label>
      </div>
      <button
        onClick={(e) => {
          e.preventDefault();
        }}
        className={styles.button}
        type="submit"
      >
        tweet
      </button>
    </form>
  );
}
