import React from "react";
import styles from "./styles/Post.module.css";
import IPost from "../../../models/IPost";
import Avatar from "../../common/Avatar";
import {
  calculateTimeDifference,
  formatTimeDifference,
} from "./utils/postDate";
import MediaPreview from "./MediaPreview";

interface IPostProps {
  post: IPost;
}

export default function Post({ post }: IPostProps) {
  const dateText = formatTimeDifference(
    calculateTimeDifference(new Date(), post.created)
  );

  return (
    <div className={styles.post}>
      <div className={styles.avatar}>
        <Avatar image={post.author.avatar} alt={post.author.name} />
      </div>
      <div style={{ width: "100%" }}>
        <div className={styles.header}>
          <h3>{post.author.name}</h3>
          <span className={styles.date}>{dateText}</span>
        </div>
        <article className={styles.article}>{post.body}</article>
        <MediaPreview media={post.media} />
      </div>
    </div>
  );
}
