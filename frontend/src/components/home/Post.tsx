import React from "react";
import styles from "./styles/Post.module.css";

interface IPostProps {
  text: string;
}

export default function Post({ text }: IPostProps) {
  return <div className={styles.post}>{text}</div>;
}
