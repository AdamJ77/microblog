import React from "react";
import styles from "./styles/Avatar.module.css";

interface IAvatarProps {
  image: string;
  alt: string;
}

export default function Avatar({ image, alt }: IAvatarProps) {
  return <img src={image} alt={alt} className={styles.image} />;
}
