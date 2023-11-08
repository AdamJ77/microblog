import React from "react";
import styles from "./styles/Post.module.css";
import IPost from "../../models/IPost";
import Avatar from "./Avatar";

interface IPostProps {
  post: IPost;
}

export default function Post({ post }: IPostProps) {
  return (
    <div className={styles.post}>
      <div className={styles.avatar}>
        <Avatar image={post.author.avatar} alt={post.author.name} />
      </div>
      <div>
        <div className={styles.header}>
          <h3>{post.author.name}</h3>
          <span>{post.created.toString()}</span>
        </div>
        <article className={styles.article}>{post.body}</article>
        <div className={styles.container}>
          {post.media.map((image, index) => (
            <a
              key={index}
              href={image}
              target="_blank"
              className={
                post.media.length % 2 === 1 && index === post.media.length - 1
                  ? styles.single
                  : styles.multiple
              }
            >
              <img src={image} className={styles.image} alt={image} />
            </a>
          ))}
        </div>
      </div>
    </div>
  );
}
