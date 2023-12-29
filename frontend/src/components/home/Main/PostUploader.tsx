import React, { useRef, useState } from "react";
import Avatar from "../../common/Avatar";
import styles from "./styles/PostUploader.module.css";
import {
  AVAILABLE_IMAGE_EXTENSIONS,
  AVAILABLE_VIDEO_EXTENSIONS,
} from "../../../constants";
import { uploadMultipleFiles } from "../../../utils/uploadFiles";

export default function PostUploader() {
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const [selectedFiles, setSelectedFiles] = useState<any[]>([]);

  const handleTextareaChange = () => {
    if (!textareaRef.current) return;
    textareaRef.current.style.height = "auto";
    textareaRef.current.style.height =
      textareaRef.current.scrollHeight + 10 + "px";
  };

  const prepareAcceptedFiles = () => {
    const concated = AVAILABLE_IMAGE_EXTENSIONS.concat(
      AVAILABLE_VIDEO_EXTENSIONS
    );
    const formatted = concated.map((ext) => `.${ext}`).join(", ");
    return formatted;
  };

  const isImage = (file: File) => {
    return file.type.startsWith("image/");
  };

  const removeFile = (index: number) => {
    setSelectedFiles((files) => files.filter((_, id) => id !== index));
  };

  const me = {
    image:
      "https://upload.wikimedia.org/wikipedia/commons/9/99/Elon_Musk_Colorado_2022_%28cropped2%29.jpg",
    alt: "Elon Musk",
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const urls = await uploadMultipleFiles(selectedFiles);
    console.log(urls);
  };

  return (
    <form className={styles.wrapper} onSubmit={handleSubmit}>
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
          {selectedFiles.map((file, index) => (
            <button
              key={index}
              title="remove"
              className={styles["uploaded-file-btn"]}
              onClick={(e) => {
                e.preventDefault();
                removeFile(index);
              }}
            >
              {isImage(file) ? (
                <img
                  src={URL.createObjectURL(file)}
                  className={styles["uploaded-file"]}
                />
              ) : (
                <video
                  src={URL.createObjectURL(file)}
                  className={styles["uploaded-file"]}
                  autoPlay
                  muted
                  loop
                >
                  Your browser doesn't support videos
                </video>
              )}
            </button>
          ))}
        </div>
        <label htmlFor="file-input">
          <input
            type="file"
            id="file-input"
            accept={prepareAcceptedFiles()}
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
      <button className={styles.button} type="submit">
        tweet
      </button>
    </form>
  );
}
