import React from "react";
import Post from "./Post";
import styles from "./styles/Posts.module.css";

export default function Posts() {
  const posts = [
    {
      id: 1,
      text: "Bajojajo",
      date: "2023-04-20T18:34:59",
      author: {
        name: "Greg",
        avatar: "http://microblog.com/users/images/Greg.png",
      },
    },
    {
      id: 2,
      text: "Ehh... good enough",
      date: "2023-07-24T22:13:12",
      author: {
        name: "Mediocrates",
        avatar: "http://microblog.com/users/images/Mediocrates.png",
      },
    },
  ];

  return (
    <div className={styles.posts}>
      {posts.map((post) => (
        <Post key={post.id} text={JSON.stringify(post)} />
      ))}
    </div>
  );
}
