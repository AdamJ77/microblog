import React, { useRef, useState } from "react";
import Avatar from "../../common/Avatar";
import styles from "./styles/PostUploader.module.css";
import {
  AVAILABLE_IMAGE_EXTENSIONS,
  AVAILABLE_VIDEO_EXTENSIONS,
} from "../../../constants";
import { uploadMultipleFiles } from "../../../utils/uploadFiles";
import axios from "axios";
import { usePostsContext } from "../../../context/PostsProvider";
import { v4 as uuidv4 } from "uuid";
import { useHomePageContext } from "../../../context/HomePageContext";

export default function PostUploader() {
  const { user } = useHomePageContext();
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const [selectedFiles, setSelectedFiles] = useState<any[]>([]);
  const { addPost } = usePostsContext();

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
    image: user!.avatar,
    alt: user!.username,
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const urls = await uploadMultipleFiles(selectedFiles);

    const text = textareaRef.current!.value;

    const preparedMedia = urls.map((url) => {
      const splitted = url.split(".");
      const ext = splitted[splitted.length - 1];

      let type = null;
      if (AVAILABLE_IMAGE_EXTENSIONS.includes(ext)) type = "image";
      else if (AVAILABLE_VIDEO_EXTENSIONS.includes(ext)) type = "video";
      else return;

      return { type, src: url };
    });

    addPost({
      id: uuidv4(),
      body: textareaRef.current!.value,
      media: urls,
      created: new Date(),
      author: {
        id: user!.id,
        name: user!.username,
        avatar: user!.avatar,
      },
    });

    const body = {
      data: {
        type: "posts",
        attributes: {
          body: text,
          media: preparedMedia,
        },
      },
    };

    const data = await axios.post(
      `${process.env.REACT_APP_SERVER_URL}/posts`,
      body,
      {
        withCredentials: true,
      }
    );

    textareaRef.current!.value = "";
    const input = document.querySelector("#file-input") as HTMLInputElement;
    input.value = "";
    setSelectedFiles([]);
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
